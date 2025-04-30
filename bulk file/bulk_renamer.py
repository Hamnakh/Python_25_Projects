import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

class BulkRenamer:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk File Renamer")
        self.root.geometry("600x400")
        
        # Variables
        self.folder_path = tk.StringVar()
        self.prefix = tk.StringVar()
        self.suffix = tk.StringVar()
        self.start_number = tk.StringVar(value="1")
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Folder Selection
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=10)
        
        tk.Label(folder_frame, text="Select Folder:").pack(side=tk.LEFT)
        tk.Entry(folder_frame, textvariable=self.folder_path, width=50).pack(side=tk.LEFT, padx=5)
        tk.Button(folder_frame, text="Browse", command=self.browse_folder).pack(side=tk.LEFT)
        
        # Renaming Options
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=10)
        
        tk.Label(options_frame, text="Prefix:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(options_frame, textvariable=self.prefix).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(options_frame, text="Suffix:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(options_frame, textvariable=self.suffix).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(options_frame, text="Start Number:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(options_frame, textvariable=self.start_number).grid(row=2, column=1, padx=5, pady=5)
        
        # Rename Button
        tk.Button(self.root, text="Rename Files", command=self.rename_files, 
                 bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=20)
        
    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
            
    def rename_files(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showerror("Error", "Please select a folder first!")
            return
            
        try:
            start_num = int(self.start_number.get())
            files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            files.sort()
            
            for i, file in enumerate(files, start=start_num):
                old_path = os.path.join(folder, file)
                file_ext = os.path.splitext(file)[1]
                new_name = f"{self.prefix.get()}{i}{self.suffix.get()}{file_ext}"
                new_path = os.path.join(folder, new_name)
                
                try:
                    os.rename(old_path, new_path)
                except Exception as e:
                    messagebox.showerror("Error", f"Error renaming {file}: {str(e)}")
                    return
                    
            messagebox.showinfo("Success", "Files renamed successfully!")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for start number!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BulkRenamer(root)
    root.mainloop() 