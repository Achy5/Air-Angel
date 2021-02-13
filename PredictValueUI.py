from tkinter import *
from tkinter import messagebox
from joblib import load
import numpy as np

regr = load("regr.joblib")
xscaler = load("xscaler.joblib")
yscaler = load("yscaler.joblib")

def Predict():
    noE.delete(0,END)
    no2E.delete(0,END)
    ozoneE.delete(0,END)
    pm10E.delete(0,END)
    try:
        arr = np.array([[float(tempE.get()),float(humE.get()),float(pressE.get())]])
        arrsc = xscaler.transform(arr)
        pr = regr.predict(arrsc)
        prinv = yscaler.inverse_transform(pr)
        noE.insert(0,round(prinv[0][0],2))
        no2E.insert(0,round(prinv[0][1],2))
        ozoneE.insert(0,round(prinv[0][2],2))
        pm10E.insert(0,round(prinv[0][3],2))
    except ValueError:
        messagebox.showinfo("Wrong Value", "Please enter float values!")

root = Tk()
root.title('Predict Value')
root.resizable(0,0)

tempL = Label(root, text = "Temp(C)")
humL = Label(root, text = "Hum(%)")
pressL = Label(root, text = "Press(hPa)")
noL = Label(root, text = "NO(ug/m3)")
no2L = Label(root, text = "NO2(ug/m3)")
ozoneL = Label(root, text = "Ozone(ug/m3)")
pm10L = Label(root, text = "PM10(ug/m3)")

nonormL = Label(root, text = "NO/NO2 norm is:%d" % 200)
o3normL = Label(root, text = "O3 norm is:%d" % 200)
pm10normL = Label(root, text = "PM10 norm is:%d" % 50)

tempE = Entry(root)
humE = Entry(root)
pressE = Entry(root)
noE = Entry(root)
no2E = Entry(root)
ozoneE = Entry(root)
pm10E = Entry(root)

tempL.grid(row=0)
humL.grid(row=1)
pressL.grid(row=2)
noL.grid(row=3)
no2L.grid(row=4)
ozoneL.grid(row=5)
pm10L.grid(row=6)

nonormL.grid(row = 3,column=2)
o3normL.grid(row = 5,column=2)
pm10normL.grid(row = 6,column=2)


tempE.grid(row=0, column= 1)
humE.grid(row=1, column= 1)
pressE.grid(row=2, column= 1)
noE.grid(row=3, column= 1)
no2E.grid(row=4, column= 1)
ozoneE.grid(row=5, column= 1)
pm10E.grid(row=6, column= 1)

b = Button(root, text="Predict", command=Predict)
b.grid(row=7)

root.mainloop()




