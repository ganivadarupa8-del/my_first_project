import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# ================= DATABASE =================
def connect():
    return sqlite3.connect("erp.db")

def create_tables():
    con = connect()
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier (id INTEGER PRIMARY KEY, name TEXT, address TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, name TEXT, qty INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS work (id INTEGER PRIMARY KEY, name TEXT, status TEXT)")

    con.commit()
    con.close()

# ================= LOGIN =================
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("ERP Login")

        tk.Label(root, text="ERP SYSTEM", font=("Arial", 16)).pack(pady=10)

        self.user = tk.Entry(root)
        self.user.pack()

        self.password = tk.Entry(root, show="*")
        self.password.pack()

        tk.Button(root, text="Login", command=self.check_login).pack(pady=10)

    def check_login(self):
        if self.user.get() == "admin" and self.password.get() == "admin":
            self.root.destroy()
            dashboard()
        else:
            messagebox.showerror("Error", "Invalid Login")

# ================= DASHBOARD =================
def dashboard():
    win = tk.Tk()
    win.title("Dashboard")

    tk.Button(win, text="Supplier Module", width=20, command=supplier_window).pack(pady=10)
    tk.Button(win, text="Item Module", width=20, command=item_window).pack(pady=10)
    tk.Button(win, text="Work Module", width=20, command=work_window).pack(pady=10)

    win.mainloop()

# ================= SUPPLIER =================
def supplier_window():
    win = tk.Toplevel()
    win.title("Supplier")

    id_var = tk.StringVar()
    name_var = tk.StringVar()
    addr_var = tk.StringVar()

    tk.Label(win, text="ID").grid(row=0, column=0)
    tk.Entry(win, textvariable=id_var).grid(row=0, column=1)

    tk.Label(win, text="Name").grid(row=1, column=0)
    tk.Entry(win, textvariable=name_var).grid(row=1, column=1)

    tk.Label(win, text="Address").grid(row=2, column=0)
    tk.Entry(win, textvariable=addr_var).grid(row=2, column=1)

    tree = ttk.Treeview(win, columns=("ID", "Name", "Address"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Address", text="Address")
    tree.grid(row=5, column=0, columnspan=3)

    def save():
        con = connect()
        cur = con.cursor()
        cur.execute("INSERT INTO supplier VALUES(?,?,?)",
                    (id_var.get(), name_var.get(), addr_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Saved")

    def load():
        for row in tree.get_children():
            tree.delete(row)

        con = connect()
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM supplier"):
            tree.insert("", tk.END, values=row)
        con.close()

    def delete():
        con = connect()
        cur = con.cursor()
        cur.execute("DELETE FROM supplier WHERE id=?", (id_var.get(),))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Deleted")

    tk.Button(win, text="Save", command=save).grid(row=3, column=0)
    tk.Button(win, text="View", command=load).grid(row=3, column=1)
    tk.Button(win, text="Delete", command=delete).grid(row=3, column=2)

# ================= ITEM =================
def item_window():
    win = tk.Toplevel()
    win.title("Item")

    id_var = tk.StringVar()
    name_var = tk.StringVar()
    qty_var = tk.StringVar()

    tk.Label(win, text="ID").grid(row=0, column=0)
    tk.Entry(win, textvariable=id_var).grid(row=0, column=1)

    tk.Label(win, text="Name").grid(row=1, column=0)
    tk.Entry(win, textvariable=name_var).grid(row=1, column=1)

    tk.Label(win, text="Qty").grid(row=2, column=0)
    tk.Entry(win, textvariable=qty_var).grid(row=2, column=1)

    tree = ttk.Treeview(win, columns=("ID", "Name", "Qty"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Qty", text="Qty")
    tree.grid(row=5, column=0, columnspan=3)

    def save():
        con = connect()
        cur = con.cursor()
        cur.execute("INSERT INTO item VALUES(?,?,?)",
                    (id_var.get(), name_var.get(), qty_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Saved")

    def load():
        for row in tree.get_children():
            tree.delete(row)

        con = connect()
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM item"):
            tree.insert("", tk.END, values=row)
        con.close()

    def delete():
        con = connect()
        cur = con.cursor()
        cur.execute("DELETE FROM item WHERE id=?", (id_var.get(),))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Deleted")

    tk.Button(win, text="Save", command=save).grid(row=3, column=0)
    tk.Button(win, text="View", command=load).grid(row=3, column=1)
    tk.Button(win, text="Delete", command=delete).grid(row=3, column=2)

# ================= WORK =================
def work_window():
    win = tk.Toplevel()
    win.title("Work")

    id_var = tk.StringVar()
    name_var = tk.StringVar()
    status_var = tk.StringVar()

    tk.Label(win, text="ID").grid(row=0, column=0)
    tk.Entry(win, textvariable=id_var).grid(row=0, column=1)

    tk.Label(win, text="Name").grid(row=1, column=0)
    tk.Entry(win, textvariable=name_var).grid(row=1, column=1)

    tk.Label(win, text="Status").grid(row=2, column=0)
    tk.Entry(win, textvariable=status_var).grid(row=2, column=1)

    tree = ttk.Treeview(win, columns=("ID", "Name", "Status"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Status", text="Status")
    tree.grid(row=5, column=0, columnspan=3)

    def save():
        con = connect()
        cur = con.cursor()
        cur.execute("INSERT INTO work VALUES(?,?,?)",
                    (id_var.get(), name_var.get(), status_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Saved")

    def load():
        for row in tree.get_children():
            tree.delete(row)

        con = connect()
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM work"):
            tree.insert("", tk.END, values=row)
        con.close()

    def delete():
        con = connect()
        cur = con.cursor()
        cur.execute("DELETE FROM work WHERE id=?", (id_var.get(),))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Deleted")

    tk.Button(win, text="Save", command=save).grid(row=3, column=0)
    tk.Button(win, text="View", command=load).grid(row=3, column=1)
    tk.Button(win, text="Delete", command=delete).grid(row=3, column=2)

# ================= MAIN =================
create_tables()

root = tk.Tk()
Login(root)
root.mainloop()