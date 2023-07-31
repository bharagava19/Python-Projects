import tkinter as tk
from tkinter import messagebox

class ContactManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Management App")
        self.geometry("400x300")

        self.contacts = []
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Contact Management App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.phone_label = tk.Label(self, text="Phone:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack()

        self.add_button = tk.Button(self, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.contact_listbox = tk.Listbox(self, width=50)
        self.contact_listbox.pack(pady=10)

        self.delete_button = tk.Button(self, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

        self.refresh_button = tk.Button(self, text="Refresh List", command=self.refresh_list)
        self.refresh_button.pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Error", "Name and phone cannot be empty.")
            return

        contact = f"{name} - {phone}"
        self.contacts.append(contact)
        self.contact_listbox.insert(tk.END, contact)

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Error", "Please select a contact to delete.")
            return

        index = selected_index[0]
        contact = self.contact_listbox.get(index)
        self.contact_listbox.delete(index)
        self.contacts.remove(contact)

    def refresh_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact)

if __name__ == "__main__":
    app = ContactManagementApp()
    app.mainloop()
