from tkinter import *
import csv
from ReadSensorsAndPredict import ReadAllSensors
import time
import os
from tkinter import messagebox
import math

flag = 0
r = 1
c = 0
fromCOUNT = ""
pm10SUM = 0

nocounter = 0
no2counter = 0
o3counter = 0
pm10counter = 0

nonorm = 200
pm10norm = 50
o3norm = 200

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_closing():
    global nocounter,no2counter,o3counter,pm10counter
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        with open("counters.csv","a") as f:
            writer = csv.writer(f, delimiter = ',')
            writer.writerow(["From:%s" % fromCOUNT, "To:%s" % time.strftime("%c"),
                    "NOcounter:%d" % nocounter, "NO2counter:%d" % no2counter,
                    "O3counter:%d" % o3counter, "PM10counter:%d" % pm10counter])
        root.destroy()

def Callback():
    global r,c,nocounter,no2counter,o3counter,pm10counter,nonorm,pm10norm,o3norm,fromCOUNT,pm10SUM,flag
    
    vals = ReadAllSensors()
    if isinstance(vals,list) == False:
        if math.isnan(vals):
            root.after(1000,Callback)
            return
    
    date = Entry(frame)
    date.insert(0,vals[0])
    date.configure(state='readonly')
    date.grid(row=r,column=c)

    c+= 1
        
    temp = Entry(frame)
    temp.insert(0,vals[1])
    temp.configure(state='readonly')
    temp.grid(row=r,column=c)

    c+= 1
        
    hum = Entry(frame)
    hum.insert(0,vals[2])
    hum.configure(state='readonly')
    hum.grid(row=r,column=c)

    c+= 1
        
    press = Entry(frame)
    press.insert(0,vals[3])
    press.configure(state='readonly')
    press.grid(row=r,column=c)

    c+= 1
    
    no = Entry(frame)
    if vals[4] > nonorm:
        flag=1
        no.insert(0,"%.2f" % vals[4] + "(HIGH!)")
        nocounter+=1
        noover.delete(0,END)
        noover.insert(0,'%d' % nocounter)
    else:
        no.insert(0,vals[4])
    no.configure(state='readonly')
    no.grid(row=r,column=c)

    c+= 1
    
    no2 = Entry(frame)
    if vals[5] > nonorm:
        flag=1
        no2.insert(0,"%.2f" % vals[5] + "(HIGH!)")
        no2counter+=1
        no2over.delete(0,END)
        no2over.insert(0,'%d' % no2counter)
    else:
        no2.insert(0,vals[5])
    no2.configure(state='readonly')
    no2.grid(row=r,column=c)

    c+= 1
    
    ozone = Entry(frame)
    if vals[6] > o3norm:
        flag=1
        ozone.insert(0,"%.2f" % vals[6] + "(HIGH!)")
        o3counter+=1
        o3over.delete(0,END)
        o3over.insert(0,'%d' % o3counter)
    else:
        ozone.insert(0,vals[6])
    ozone.configure(state='readonly')
    ozone.grid(row=r,column=c)

    c+= 1

    pm10 = Entry(frame)
    pm10SUM+=vals[7]
    if r % 24 == 0:
        pm10DAY = pm10SUM / 24
        if pm10DAY > pm10norm:
            flag=1
            pm10.insert(0,"%.2f" % vals[7] + "(%.2f)HIGH!" % pm10DAY)
            pm10counter+=1
            pm10over.delete(0,END)
            pm10over.insert(0,'%d' % pm10counter)
            pm10SUM = 0
        else:
            pm10.insert(0,"%.2f" % vals[7] + "(%.2f)" % pm10DAY)
    else:
        pm10.insert(0,vals[7])
    pm10.configure(state='readonly')
    pm10.grid(row=r,column=c)

    if r==1:
        fromCOUNT = vals[0] # first line so we know from when the counter started

    r+= 1
    c = 0

    with open("output.csv","a") as f:
                    writer = csv.writer(f, delimiter = ',')
                    a = [date.get(),temp.get(),hum.get(),press.get(),no.get(),no2.get(),ozone.get(),pm10.get()]
                    writer.writerow(a)

    if flag==1:
        with open("exceeds.csv","a") as f:
            writer = csv.writer(f, delimiter = ',')
            b = [date.get(),temp.get(),hum.get(),press.get(),no.get(),no2.get(),ozone.get(),pm10.get()]
            writer.writerow(b)
            
    flag=0

    root.after(5000,Callback)
    
root = Tk()
root.title('Grid View')
root.resizable(0,0)

canvas = Canvas(root)
frame = Frame(canvas)
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)
vsb.grid(row=0,column=8)

date = Entry(root)
date.insert(0,'Date_Time')
date.configure(state='readonly')
date.grid(row=0,column=0)

temp = Entry(root)
temp.insert(0,'T(C)')
temp.configure(state='readonly')
temp.grid(row=0,column=1)

hum = Entry(root)
hum.insert(0,'H(%)')
hum.configure(state='readonly')
hum.grid(row=0,column=2)

press = Entry(root)
press.insert(0,'P(hPa)')
press.configure(state='readonly')
press.grid(row=0,column=3)

no = Entry(root)
no.insert(0,'NO(ug/m3)')
no.configure(state='readonly')
no.grid(row=0,column=4)

no2 = Entry(root)
no2.insert(0,'NO2(ug/m3)')
no2.configure(state='readonly')
no2.grid(row=0,column=5)

o3 = Entry(root)
o3.insert(0,'O3(ug/m3)')
o3.configure(state='readonly')
o3.grid(row=0,column=6)

pm10 = Entry(root)
pm10.insert(0,'PM10(ug/m3)')
pm10.configure(state='readonly')
pm10.grid(row=0,column=7)

possibleovers = Entry(root)
possibleovers.insert(0,'Possible exceedances counts:')
possibleovers.configure(state='readonly')
possibleovers.grid(row=2,column=0,columnspan=4,sticky=E+W)

noover = Entry(root)
noover.insert(0,'%d' % nocounter)
noover.grid(row=2,column=4)

no2over = Entry(root)
no2over.insert(0,'%d' % no2counter)
no2over.grid(row=2,column=5)

o3over = Entry(root)
o3over.insert(0,'%d' % o3counter)
o3over.grid(row=2,column=6)

pm10over = Entry(root)
pm10over.insert(0,'%d'% pm10counter)
pm10over.grid(row=2,column=7)

canvas.grid(row=1,column=0,columnspan = 8,sticky=E+W)

root.update()
canvas.create_window((0,0),
                     window=frame, anchor="nw")
frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))


Callback()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
