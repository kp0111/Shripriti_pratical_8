#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Plotter")

        # Variables
        self.graph_type_var = tk.StringVar()
        self.graph_type_var.set("Bar Chart")

        # Dropdown menu for selecting graph type
        graph_type_label = tk.Label(root, text="Select Graph Type:")
        graph_type_dropdown = ttk.Combobox(root, textvariable=self.graph_type_var, values=["Bar Chart", "Pie Chart", "Scatter Plot"])

        # Entry for entering data
        data_label = tk.Label(root, text="Enter Data (comma-separated):")
        self.data_entry = tk.Entry(root)

        # Button to plot graph
        plot_button = tk.Button(root, text="Plot Graph", command=self.plot_graph)

        # Matplotlib figure
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.subplot = self.figure.add_subplot(111)

        # Matplotlib canvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Layout
        graph_type_label.pack(pady=10)
        graph_type_dropdown.pack(pady=10)
        data_label.pack(pady=10)
        self.data_entry.pack(pady=10)
        plot_button.pack(pady=10)

    def plot_graph(self):
        data_str = self.data_entry.get()
        data = [float(x.strip()) for x in data_str.split(',')]

        self.subplot.clear()

        if self.graph_type_var.get() == "Bar Chart":
            self.subplot.bar(range(len(data)), data)
        elif self.graph_type_var.get() == "Pie Chart":
            self.subplot.pie(data, labels=[f'Data {i+1}' for i in range(len(data))], autopct='%1.1f%%')
        elif self.graph_type_var.get() == "Scatter Plot":
            self.subplot.scatter(range(len(data)), data)

        self.subplot.set_title(self.graph_type_var.get())
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()


# In[ ]:




