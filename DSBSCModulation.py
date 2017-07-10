#!/usr/bin/env python
# -*- coding: utf-8 -*-

__date__ = '10.10.2016'
__author__ = 'cemonatk'

from numpy import cos,pi,sin,arange
from matplotlib.pyplot import plot,show,title,subplot,suptitle,xlabel,imshow
from matplotlib.image import imread
from Tkinter import *

def DSBSCModulate(fm,fc,aralik):
    suptitle('Analog-Lab')
    t = arange(1,aralik)
    tc = cos(2*pi*fc*t)
    ms = sin(2*pi*fm*t)
    DSB = tc*ms
    subplot(2,2,1)
    plot(tc)
    title('Carrier Wave')
    subplot(2,2,2)
    plot(ms)
    title('message Sinyali')
    subplot(2,1,2)
    plot(DSB)
    title('DSB-SC Modulasyonu')
    show()

def AmModulation():
    pass

def Show():
    img = imread('picture.jpg')
    imshow(img)
    title('MATLAB Kullanmayi Acilen Birakman Gerek...')
    show()

def StrToFloat():
    carrier = 1.0/float(carrierfreq.get())
    message = 1.0/float(messagefreq.get())
    try:
        aralik = int(aralik.get())
    except:
        aralik = 360
    DsbscCiz(message, carrier, aralik)

kok = Tk()
kok.title("Analog-Lab")

carrierfreq = StringVar()
e = Entry(kok, textvariable=carrierfreq)
e.pack()
carrierfreq.set("Carrier Freq")

messagefreq = StringVar()
e = Entry(kok, textvariable=messagefreq)
e.pack()
messagefreq.set("message freq")

aralik = StringVar()
e = Entry(kok, textvariable=aralik)
e.pack()
aralik.set("Aralık(360 varsayılan)")

Button(kok, text='Draw DSB-SC', height=2, width=35, command=StrToFloat).pack()
Button(kok, text='Gizli Suprizi Goster', height=2, width=35, command=Show).pack()
Button(kok, text='Exit', command=kok.destroy).pack()
kok.mainloop()

Button(kok, text='Draw DSB-SC', height=2, width=35, command=lambda: DSBSCModulate(messagefreq,carrier,range)).pack()
