#!/usr/bin/python
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Scrollbar

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("1920x1080")

        # Bottone per selezionare la cartella
        self.btn_select_folder = tk.Button(root, text="Seleziona Cartella", command=self.select_folder)
        self.btn_select_folder.pack(pady=10)

        # Lista file
        self.file_listbox = Listbox(root, width=80, height=15)
        self.file_listbox.pack(pady=10)

        # Scrollbar
        self.scrollbar = Scrollbar(root, command=self.file_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.file_listbox.config(yscrollcommand=self.scrollbar.set)

        # Pulsanti per operazioni sui file
        self.btn_open = tk.Button(root, text="Apri", command=self.open_file)
        self.btn_open.pack(pady=5)

        self.btn_delete = tk.Button(root, text="Elimina", command=self.delete_file)
        self.btn_delete.pack(pady=5)

        self.btn_copy = tk.Button(root, text="Copia in...", command=self.copy_file)
        self.btn_copy.pack(pady=5)

        self.btn_move = tk.Button(root, text="Sposta in...", command=self.move_file)
        self.btn_move.pack(pady=5)

        self.current_folder = ""

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.current_folder = folder
            self.list_files()

    def list_files(self):
        self.file_listbox.delete(0, tk.END)
        for file in os.listdir(self.current_folder):
            self.file_listbox.insert(tk.END, file)

    def get_selected_file(self):
        try:
            index = self.file_listbox.curselection()[0]
            return os.path.join(self.current_folder, self.file_listbox.get(index))
        except IndexError:
            messagebox.showwarning("Attenzione", "Seleziona un file!")
            return None

    def open_file(self):
        file_path = self.get_selected_file()
        if file_path:
            os.startfile(file_path)

    def delete_file(self):
        file_path = self.get_selected_file()
        if file_path:
            if messagebox.askyesno("Conferma", f"Vuoi eliminare {file_path}?"):
                os.remove(file_path)
                self.list_files()

    def copy_file(self):
        file_path = self.get_selected_file()
        if file_path:
            dest = filedialog.askdirectory()
            if dest:
                shutil.copy(file_path, dest)
                messagebox.showinfo("Successo", "File copiato con successo!")

    def move_file(self):
        file_path = self.get_selected_file()
        if file_path:
            dest = filedialog.askdirectory()
            if dest:
                shutil.move(file_path, dest)
                self.list_files()
                messagebox.showinfo("Successo", "File spostato con successo!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
