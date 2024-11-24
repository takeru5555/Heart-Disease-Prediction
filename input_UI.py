import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def submit_data():
    # Retrieve values from the input fields
    age = age_entry.get()
    sex = sex_var.get()
    cp = cp_var.get()
    trestbps = trestbps_entry.get()
    chol = chol_entry.get()
    fbs = fbs_var.get()
    restecg = restecg_var.get()
    thalach = thalach_entry.get()
    exang = exang_var.get()
    oldpeak = oldpeak_entry.get()
    slope = slope_var.get()
    ca = ca_entry.get()
    thal = thal_var.get()

    # Display the collected data
    data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }
    
    messagebox.showinfo("Input Data", str(data))

# Create the main window
root = tk.Tk()
root.title("Heart Disease Data Input")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

# Create a style
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 10), background="#f0f0f0")
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TEntry", font=("Helvetica", 10), padding=5)

# Define the input fields with padding
tk.Label(root, text="Heart Disease Data Input", font=("Helvetica", 14, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=(10, 20))

tk.Label(root, text="Age:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
age_entry = ttk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Sex (0=Female, 1=Male):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
sex_var = tk.IntVar()
ttk.Radiobutton(root, text="Female", variable=sex_var, value=0).grid(row=2, column=1, sticky="w")
ttk.Radiobutton(root, text="Male", variable=sex_var, value=1).grid(row=2, column=1, sticky="e")

tk.Label(root, text="CP (chest pain type):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
cp_var = tk.IntVar()
ttk.Radiobutton(root, text="Type 0", variable=cp_var, value=0).grid(row=3, column=1, sticky="w")
ttk.Radiobutton(root, text="Type 1", variable=cp_var, value=1).grid(row=3, column=1, sticky="e")
ttk.Radiobutton(root, text="Type 2", variable=cp_var, value=2).grid(row=3, column=1, sticky="e")
ttk.Radiobutton(root, text="Type 3", variable=cp_var, value=3).grid(row=3, column=1, sticky="e")

tk.Label(root, text="Trestbps:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
trestbps_entry = ttk.Entry(root)
trestbps_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Chol:").grid(row=5, column=0, sticky="w", padx=10, pady=5)
chol_entry = ttk.Entry(root)
chol_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="FBS (fasting blood sugar > 120 mg/dl):").grid(row=6, column=0, sticky="w", padx=10, pady=5)
fbs_var = tk.IntVar()
ttk.Radiobutton(root, text="No", variable=fbs_var, value=0).grid(row=6, column=1, sticky="w")
ttk.Radiobutton(root, text="Yes", variable=fbs_var, value=1).grid(row=6, column=1, sticky="e")

tk.Label(root, text="Restecg (resting electrocardiographic results):").grid(row=7, column=0, sticky="w", padx=10, pady=5)
restecg_var = tk.IntVar()
ttk.Radiobutton(root, text="Normal", variable=restecg_var, value=0).grid(row=7, column=1, sticky="w")
ttk.Radiobutton(root, text="Abnormal", variable=restecg_var, value=1).grid(row=7, column=1, sticky="e")

tk.Label(root, text="Thalach (maximum heart rate achieved):").grid(row=8, column=0, sticky="w", padx=10, pady=5)
thalach_entry = ttk.Entry(root)
thalach_entry.grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="Exang (exercise induced angina):").grid(row=9, column=0, sticky="w", padx=10, pady=5)
exang_var = tk.IntVar()
ttk.Radiobutton(root, text="No", variable=exang_var, value=0).grid(row=9, column=1, sticky="w")
ttk.Radiobutton(root, text="Yes", variable=exang_var, value=1).grid(row=9, column=1, sticky="e")

tk.Label(root, text="Oldpeak:").grid(row=10, column=0, sticky="w", padx=10, pady=5)
oldpeak_entry = ttk.Entry(root)
oldpeak_entry.grid(row=10, column=1, padx=10, pady=5)

tk.Label(root, text="Slope (slope of the peak exercise ST segment):").grid(row=11, column=0, sticky="w", padx=10, pady=5)
slope_var = tk.IntVar()
ttk.Radiobutton(root, text="Up", variable=slope_var, value=0).grid(row=11, column=1, sticky="w")
ttk.Radiobutton(root, text="Flat", variable=slope_var, value=1).grid(row=11, column=1, sticky="e")
ttk.Radiobutton(root, text="Down", variable=slope_var, value=2).grid(row=11, column=1, sticky="e")

tk.Label(root, text="CA (number of major vessels):").grid(row=12, column=0, sticky="w", padx=10, pady=5)
ca_entry = ttk.Entry(root)
ca_entry.grid(row=12, column=1, padx=10, pady=5)

tk.Label(root, text="Thal (thalassemia):").grid(row=13, column=0, sticky="w", padx=10, pady=5)
thal_var = tk.IntVar()
ttk.Radiobutton(root, text="Normal", variable=thal_var, value=1).grid(row=13, column=1, sticky="w")
ttk.Radiobutton(root, text="Fixed defect", variable=thal_var, value=2).grid(row=13, column=1, sticky="e")
ttk.Radiobutton(root, text="Reversible defect", variable=thal_var, value=3).grid(row=13, column=1, sticky="e")

# Submit button
submit_button = ttk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=14, column=0, columnspan=2, pady=20)

# Start the GUI event loop
root.mainloop()
