import os
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict, Counter

# git clone --depth 1 --branch main https://github.com/github/advisory-database.git

advisory_dir = 'advisory-database/advisories/github-reviewed'

def process_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = json.load(f)
        affected_packages = content.get('affected', [])
        for package_info in affected_packages:
            if package_info.get('package', {}).get('ecosystem') == 'npm':
                cwe_ids = content.get('database_specific', {}).get(
                    'cwe_ids', ['Unknown'])
                cwe_id = cwe_ids[0] if cwe_ids else 'Unknown'
                cve_aliases = content.get('aliases', [])
                cve_id = cve_aliases[0] if cve_aliases else 'Unknown'
                cve_title = content.get('summary', 'Unknown')
                year = content.get('published', 'Unknown')[:4]
                return year, cwe_id, cve_title, cve_id
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

file_paths = [os.path.join(root, file) for root, dirs, files in os.walk(
    advisory_dir) for file in files if file.endswith('.json')]

# CWE data
data = defaultdict(lambda: defaultdict(list))

with ThreadPoolExecutor() as executor:
    futures = {executor.submit(process_file, file_path)
                               : file_path for file_path in file_paths}
    for future in as_completed(futures):
        result = future.result()
        if result:
            year, cwe_id, cve_title, cve_id = result
            data[year][cwe_id].append((cve_title, cve_id))

output_path = 'cwe_analysis.html'
with open(output_path, 'w') as out_file:
    out_file.write("""
    <html>
    <head>
        <style>
            .collapsible {
                background-color: #777;
                color: white;
                cursor: pointer;
                padding: 18px;
                width: 100%;
                border: none;
                text-align: left;
                outline: none;
                font-size: 15px;
            }

            .active, .collapsible:hover {
                background-color: #555;
            }

            .content {
                padding: 0 18px;
                display: none;
                overflow: hidden;
                background-color: #f1f1f1;
            }

            .hide-btn {
                background-color: #f44336;
                color: white;
                padding: 10px 20px;
                border: none;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 12px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
    """)

    for year, cwes in sorted(data.items()):
        cwe_counts = Counter({cwe: len(entries)
                             for cwe, entries in cwes.items()})
        top_5_cwes = [cwe for cwe, count in cwe_counts.most_common(5)]
        top_5_text = ', '.join(top_5_cwes)
        out_file.write(f"<h2>Year: {year} (Top 5 CWEs: {top_5_text})</h2>")

        for cwe_id, entries in sorted(cwes.items(), key=lambda item: len(item[1]), reverse=True):
            if len(entries) < 4:  # Skip CWEs with fewer than 5 CVEs
                continue
            num_cves = len(entries)
            entries_html = ''.join(
                f"<li>{cve_id} - {cve_title}</li>" for cve_title, cve_id in entries)

            out_file.write(f"""
            <div class="cwe-section">
                <button type="button" class="collapsible">CWE ID: {cwe_id} ({num_cves} CVEs)</button>
                <button type="button" class="hide-btn" onclick="hideSection(this.parentNode)">Hide Section</button>
                <div class="content">
                    <ul>
                        {entries_html}
                    </ul>
                </div>
            </div>
            """)

    out_file.write("""
    <script>
        var coll = document.getElementsByClassName("collapsible");
        for (var i = 0; i < coll.length; i++) {
            coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var content = this.nextElementSibling.nextElementSibling;
                if (content.style.display === "block") {
                    content.style.display = "none";
                } else {
                    content.style.display = "block";
                }
            });
        }

        function hideSection(section) {
            section.style.display = 'none';
        }
    </script>
    </body>
    </html>
    """)

print(f"Analysis completed. '{output_path}' ")
