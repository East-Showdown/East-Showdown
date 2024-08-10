import tkinter as tk
from tkinter import messagebox
import math

def increase_divisions(divisions, percentage):
    total_divisions = sum(divisions.values())
    new_total = math.floor(total_divisions * (1 + percentage / 100))
    
    increase_factor = new_total / total_divisions
    
    new_divisions = {k: max(0, math.floor(v * increase_factor)) for k, v in divisions.items()}
    
    discrepancy = new_total - sum(new_divisions.values())
    
    while discrepancy > 0:
        max_key = max(new_divisions, key=lambda k: divisions[k])
        new_divisions[max_key] += 1
        discrepancy -= 1
    
    increases = {k: new_divisions[k] - v for k, v in divisions.items()}
    
    return new_divisions, new_total, increases

def calculate():
    try:
        percentage = float(entry_percentage.get())
    except ValueError:
        messagebox.showerror("Error", "Enter the correct percentage value.")
        return

    selected_set = var_set.get()
    if selected_set == 1:
        divisions = divisions_set1
    else:
        divisions = divisions_set2

    new_divisions, new_total, increases = increase_divisions(divisions, percentage)
    
    result_text = "The new divisions, after being increased by {}%:\n".format(percentage)
    for k, v in new_divisions.items():
        increase = increases[k]
        result_text += "{}: {} (grew by {})\n".format(k, v, increase)
    
    total_increase = new_total - sum(divisions.values())
    result_text += "\nTotal divisions now: {} (increased by {})".format(new_total, total_increase)
    
    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, result_text)
    text_result.config(state=tk.DISABLED)

divisions_set1 = {
    "NGU batalyon": 72,
    "Artilerry divizion": 58,
    "Pechotny batalion": 36,
    "Mechanizovany batalion": 33,
    "Desantny batalion": 20,
    "Batalion t64": 18,
    "Batalion t72": 13,
    "Gornostrelkovy batalion": 7,
    "Batalion morskoy pechoty": 7,
    "SSO batalyon": 6,
    "Omega": 6,
    "Batalion academy": 5,
    "Azov": 4,
    "Tyazoly artillery divizion": 4,
    "Batalion t80": 3
}

divisions_set2 = {
    "Motostrelkovy batalion": 116,
    "Artilerisky batalion": 90,
    "Batalion t72": 47,
    "Paratroopers batalion": 27,
    "Pechotniy batalion": 24,
    "TOS batalion": 17,
    "Marines Batalion": 16,
    "Taszheliy artileriskiy batalion": 15,
    "Batalion T90": 15,
    "Vertoletni batalion": 11,
    "Spetsnaz": 7,
    "Batalion T80": 7,
    "Rosgvardiya": 5,
}

total_divisions_set1 = sum(divisions_set1.values())
total_divisions_set2 = sum(divisions_set2.values())

root = tk.Tk()
root.title("Increasing divisions")
label_percentage = tk.Label(root, text="Enter the percent of increase:")
label_percentage.pack(pady=5)
entry_percentage = tk.Entry(root)
entry_percentage.pack(pady=5)
var_set = tk.IntVar(value=1)
radio_set1 = tk.Radiobutton(root, text=f"OOB UKR_2022 ({total_divisions_set1} divisions)", variable=var_set, value=1)
radio_set1.pack(pady=5)
radio_set2 = tk.Radiobutton(root, text=f"OOB RUS_2022 ({total_divisions_set2} divisions)", variable=var_set, value=2)
radio_set2.pack(pady=5)
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=5)
text_result = tk.Text(root, height=20, width=60, state=tk.DISABLED)
text_result.pack(pady=5)
root.mainloop()
