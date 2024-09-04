import tkinter as tk
from tkinter import messagebox

def calculate_increase():
    try:
        factories = int(factory_entry.get())
        military_factories = int(military_entry.get())
        percentage = float(percentage_entry.get())
        
        factory_increase = factories * (percentage / 100)
        military_increase = military_factories * (percentage / 100)
        
        new_factories = factories + factory_increase
        new_military_factories = military_factories + military_increase
        
        factory_increase = round(factory_increase, 0)
        military_increase = round(military_increase, 0)
        new_factories = round(new_factories, 0)
        new_military_factories = round(new_military_factories, 0)
        
        result_text = (
            f"Industral_complex: {new_factories} ({factory_increase} increased)\n"
            f"Arms_factory: {new_military_factories} ({military_increase} increased)"
        )
        result_label.config(text=result_text)
    
    except ValueError:
        messagebox.showerror("Error", "Enter the correct value.")

def apply_preset(preset):
    if preset == "Preset 2":
        factory_entry.delete(0, tk.END)
        factory_entry.insert(0, "109")
        military_entry.delete(0, tk.END)
        military_entry.insert(0, "60")
    elif preset == "Preset 1":
        factory_entry.delete(0, tk.END)
        factory_entry.insert(0, "241")
        military_entry.delete(0, tk.END)
        military_entry.insert(0, "195")

root = tk.Tk()
root.title("Buildings")
tk.Label(root, text="Industral_complex:").grid(row=0, column=0, padx=10, pady=10)
factory_entry = tk.Entry(root)
factory_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Label(root, text="Arms_factory:").grid(row=1, column=0, padx=10, pady=10)
military_entry = tk.Entry(root)
military_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Label(root, text="Percent of increase:").grid(row=2, column=0, padx=10, pady=10)
percentage_entry = tk.Entry(root)
percentage_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Calculate", command=calculate_increase).grid(row=3, column=0, columnspan=2, pady=10)
preset_frame = tk.Frame(root)
preset_frame.grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(preset_frame, text="RUS_preset", command=lambda: apply_preset("Preset 1")).pack(side=tk.LEFT, padx=5)
tk.Button(preset_frame, text="UKR_preset", command=lambda: apply_preset("Preset 2")).pack(side=tk.LEFT, padx=5)
result_frame = tk.Frame(root, borderwidth=2, relief="groove")
result_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
result_label = tk.Label(result_frame, text="Result")
result_label.pack(padx=10, pady=5)
root.mainloop()
