import tkinter as tk
import numpy as np

class WTAInputGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("WTA Input Generator")

        self.num_neurons = tk.IntVar(value=10)
        self.radius = tk.DoubleVar(value=0.5)
        self.mean = tk.DoubleVar(value=0)
        self.std_dev = tk.DoubleVar(value=0.2)

        self.create_widgets()

    def create_widgets(self):
        # Number of neurons
        tk.Label(self.master, text="Number of neurons:").grid(row=0, column=0)
        tk.Entry(self.master, textvariable=self.num_neurons).grid(row=0, column=1)

        # Radius
        tk.Label(self.master, text="Radius:").grid(row=1, column=0)
        tk.Entry(self.master, textvariable=self.radius).grid(row=1, column=1)

        # Mean
        tk.Label(self.master, text="Mean:").grid(row=2, column=0)
        tk.Entry(self.master, textvariable=self.mean).grid(row=2, column=1)

        # Standard deviation
        tk.Label(self.master, text="Standard deviation:").grid(row=3, column=0)
        tk.Entry(self.master, textvariable=self.std_dev).grid(row=3, column=1)

        # Generate input button
        tk.Button(self.master, text="Generate Input", command=self.generate_input).grid(row=4, column=0, columnspan=2)

        # Save input to file button
        tk.Button(self.master, text="Save Input to File", command=self.save_to_file).grid(row=5, column=0, columnspan=2)

    def generate_input(self):
        num_neurons = self.num_neurons.get()
        radius = self.radius.get()
        mean = self.mean.get()
        std_dev = self.std_dev.get()

        # Generate input data
        input_data = np.random.normal(mean, std_dev, size=(num_neurons, 2))
        input_data = radius * input_data / np.linalg.norm(input_data, axis=1)[:, np.newaxis]

        self.input_data = input_data

    def save_to_file(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt")

        if filename:
            with open(filename, "w") as f:
                for row in self.input_data:
                    f.write(f"[{row[0]}, {row[1]}]\n")


root = tk.Tk()
app = WTAInputGenerator(root)
root.mainloop()

