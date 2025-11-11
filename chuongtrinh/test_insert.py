from common.insertdanhmuc import insert_danhmuc

while True:
    ten = input("Nhap vao ten danh muc:")
    mota = input("Nhap vao mo ta:")

    insert_danhmuc(ten, mota)

    con = input("Tiep tuc nhap (y) Thoat(n): ")
    if con != "y":
        break