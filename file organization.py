import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")

        # Set background color for the main window
        self.root.configure(bg='lightgray')

        # Center the window
        self.center_window()

        # Initialize log file path
        self.log_file_path = 'file_log.txt'

        # Create the GUI
        self.create_widgets()

    def center_window(self):
        # Get window size
        window_width = 400
        window_height = 400

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)

        # Set the dimensions of the window
        self.root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    def create_widgets(self):
        # Select Directory Button
        self.select_button = tk.Button(self.root, text="Select Directory", command=self.select_directory, bg='lightblue')
        self.select_button.pack(pady=10)

        # Directory Path Entry
        self.directory_entry = tk.Entry(self.root, width=50)
        self.directory_entry.pack(pady=5)

        # Criteria Label
        tk.Label(self.root, text="Organize by:", bg='lightgray').pack(pady=5)

        # Criteria Options
        self.criteria_var = tk.StringVar(value="type")
        tk.Radiobutton(self.root, text="File Type", variable=self.criteria_var, value="type", bg='lightgray').pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="Creation Date", variable=self.criteria_var, value="date", bg='lightgray').pack(anchor=tk.W)

        # Organize Button
        self.organize_button = tk.Button(self.root, text="Organize Files", command=self.organize_files, bg='lightgreen')
        self.organize_button.pack(pady=10)

        # Reorganize Button
        self.reorganize_button = tk.Button(self.root, text="Reorganize Files", command=self.reorganize_files, bg='lightcoral')
        self.reorganize_button.pack(pady=10)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(0, directory)

    def organize_files(self):
        directory = self.directory_entry.get()
        if not os.path.isdir(directory):
            messagebox.showerror("Error", "Please select a valid directory.")
            return

        criteria = self.criteria_var.get()
        if criteria == "type":
            self.organize_by_type(directory)
        elif criteria == "date":
            self.organize_by_date(directory)
        else:
            messagebox.showerror("Error", "Invalid criteria selected.")
            return

        messagebox.showinfo("Success", "Files organized successfully!")

    def organize_by_type(self, directory):
        with open(self.log_file_path, 'w') as log_file:
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path):
                    file_type = filename.split('.')[-1] if '.' in filename else 'unknown'
                    type_dir = os.path.join(directory, file_type)
                    if not os.path.exists(type_dir):
                        os.makedirs(type_dir)
                    shutil.move(file_path, os.path.join(type_dir, filename))
                    log_file.write(f"{file_path} -> {os.path.join(type_dir, filename)}\n")

    def organize_by_date(self, directory):
        with open(self.log_file_path, 'w') as log_file:
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path):
                    creation_time = os.path.getctime(file_path)
                    creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
                    date_dir = os.path.join(directory, creation_date)
                    if not os.path.exists(date_dir):
                        os.makedirs(date_dir)
                    shutil.move(file_path, os.path.join(date_dir, filename))
                    log_file.write(f"{file_path} -> {os.path.join(date_dir, filename)}\n")

    def reorganize_files(self):
        if not os.path.isfile(self.log_file_path):
            messagebox.showerror("Error", "No log file found. Please organize files first.")
            return

        with open(self.log_file_path, 'r') as log_file:
            lines = log_file.readlines()

        for line in lines:
            src, dst = line.strip().split(' -> ')
            if os.path.isfile(dst):
                shutil.move(dst, src)

        messagebox.showinfo("Success", "Files reorganized successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()