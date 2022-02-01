from doctest import master
import tkinter as ui
import time

window = ui.Tk()
window.title ("Jam Digital")


def update_clock():
    jam = time.strftime("%I")
    menit = time.strftime("%M")
    detik = time.strftime("%S")
    am_atau_pm = time.strftime("%p")
    time_text = jam + ":" + menit + ":" + detik + " " + am_atau_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)


digital_clock_lbl = ui.Label(window, text="00:00:00", font="Helvetica 72 bold", bg="gray", fg="white")
digital_clock_lbl.pack()

update_clock()

window.mainloop()