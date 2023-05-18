import tkinter

elements = []
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=150, height=100)


def calc_km():
    miles_to_km_label["text"] = abs(float(miles.get()) * 1.609)


miles = tkinter.Entry()
miles_label = tkinter.Label(text="Miles")
equalto_label = tkinter.Label(text="is equal to")
miles_to_km_label = tkinter.Label(text="0")
km_label = tkinter.Label(text="Km")
calc_button = tkinter.Button(text="Calculate", command=calc_km)

for child in window.winfo_children():
    child.grid_configure(padx=10, pady=10)
    child.config(font=("Arial", 12, "normal"))

miles.grid(column=2, row=1)
miles_label.grid(column=3, row=1, padx=30)
equalto_label.grid(column=1, row=2)
miles_to_km_label.grid(column=2, row=2)
km_label.grid(column=3, row=2)
calc_button.grid(column=2, row=3)
