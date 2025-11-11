from common.update_danhmuc import update_danhmuc

while True:
    madanhmuc = input("Nhap ma danh muc: ")
    ten = input("Nhap vao ten danh muc:")
    mota = input("Nhap vao mo ta:")

    update_danhmuc(madanhmuc, ten, mota)

    con = input("Tiep tuc nhap (y) Thoat(n): ")
    if con != "y":
        break