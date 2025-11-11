import tkinter as tk
from tkinter import ttk, messagebox

from common.insertdanhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
from common.delete_danhmuc import delete_danhmuc
from common.get_danhmuc import get_all_danhmuc


# ======== HÀM XỬ LÝ ========

def chon_danhmuc(event):
    """Khi chọn 1 hàng trong bảng -> hiển thị thông tin lên ô nhập"""
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")
    entry_id.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)
    entry_id.insert(0, values[0])
    entry_ten.insert(0, values[1])
    entry_mota.insert(0, values[2])


def load_data():
    """Tải danh sách danh mục vào Treeview"""
    for row in tree.get_children():
        tree.delete(row)
    data = get_all_danhmuc()
    for item in data:
        tree.insert("", "end", values=(item["id"], item["ten_danhmuc"], item["mo_ta"]))


def lam_moi():
    """Làm mới toàn bộ giao diện"""
    entry_id.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)
    load_data()


def them_danhmuc():
    """Thêm danh mục mới"""
    ten = entry_ten.get().strip()
    mo_ta = entry_mota.get().strip()

    if not ten:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục!")
        return

    insert_danhmuc(ten, mo_ta)
    messagebox.showinfo("Thành công", f"Đã thêm danh mục '{ten}'!")
    lam_moi()


def sua_danhmuc():
    """Cập nhật danh mục"""
    id_ = entry_id.get().strip()
    ten = entry_ten.get().strip()
    mo_ta = entry_mota.get().strip()

    if not id_:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng chọn danh mục cần sửa!")
        return

    update_danhmuc(id_, ten, mo_ta)
    messagebox.showinfo("Thành công", f"Đã cập nhật danh mục ID {id_}")
    lam_moi()


def xoa_danhmuc():
    """Xóa danh mục"""
    id_ = entry_id.get().strip()

    if not id_:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng chọn danh mục cần xóa!")
        return

    if messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa danh mục ID {id_}?"):
        delete_danhmuc(id_)
        messagebox.showinfo("Thành công", f"Đã xóa danh mục ID {id_}")
        lam_moi()


# ======== GIAO DIỆN CHÍNH ========

root = tk.Tk()
root.title("📂 Quản lý Danh Mục")
root.geometry("800x500")
root.configure(bg="#F4F6F8")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#1976D2", foreground="white")
style.configure("Treeview", font=("Arial", 10), rowheight=28)

# --- Khung nhập liệu ---
frame_input = tk.LabelFrame(root, text="Thông tin danh mục", font=("Arial", 11, "bold"), bg="#F4F6F8")
frame_input.pack(padx=15, pady=10, fill="x")

tk.Label(frame_input, text="ID:", bg="#F4F6F8", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_id = tk.Entry(frame_input, width=10)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Tên danh mục:", bg="#F4F6F8", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_ten = tk.Entry(frame_input, width=25)
entry_ten.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:", bg="#F4F6F8", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_mota = tk.Entry(frame_input, width=50)
entry_mota.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")

# --- Nút chức năng ---
frame_btn = tk.Frame(root, bg="#F4F6F8")
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="➕ Thêm", command=them_danhmuc,
           bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=12).grid(row=0, column=0, padx=8)
tk.Button(frame_btn, text="✏️ Sửa", command=sua_danhmuc,
           bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=12).grid(row=0, column=1, padx=8)
tk.Button(frame_btn, text="🗑️ Xóa", command=xoa_danhmuc,
           bg="#E53935", fg="white", font=("Arial", 10, "bold"), width=12).grid(row=0, column=2, padx=8)
tk.Button(frame_btn, text="🔄 Làm mới", command=lam_moi,
           bg="#FF9800", fg="white", font=("Arial", 10, "bold"), width=12).grid(row=0, column=3, padx=8)

# --- Bảng danh sách ---
frame_table = tk.Frame(root)
frame_table.pack(padx=15, pady=10, fill="both", expand=True)

columns = ("ID", "Tên danh mục", "Mô tả")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=10)

# Cấu hình tiêu đề và căn giữa
tree.heading("ID", text="ID", anchor="center")
tree.heading("Tên danh mục", text="Tên danh mục", anchor="center")
tree.heading("Mô tả", text="Mô tả", anchor="center")

tree.column("ID", width=80, anchor="center")
tree.column("Tên danh mục", width=200, anchor="center")
tree.column("Mô tả", width=400, anchor="center")

tree.pack(fill="both", expand=True)
tree.bind("<ButtonRelease-1>", chon_danhmuc)

# --- Tải dữ liệu ban đầu ---
load_data()

root.mainloop()
