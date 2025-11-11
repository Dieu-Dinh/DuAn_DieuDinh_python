from ketnoi.ketnoi_mySql import create_connection

def get_all_danhmuc():
    """Lấy danh sách toàn bộ danh mục trong bảng danhmuc"""
    conn = create_connection()
    danh_sach = []
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)  # Trả về dạng dict
            sql = "SELECT id, ten_danhmuc, mo_ta, trang_thai, created_at FROM danhmuc ORDER BY id ASC"
            cursor.execute(sql)
            danh_sach = cursor.fetchall()

            if danh_sach:
                print("✅ Danh sách danh mục:")
                for dm in danh_sach:
                    print(f"ID: {dm['id']}, Tên: {dm['ten_danhmuc']}, Mô tả: {dm['mo_ta']}")
            else:
                print("⚠️ Chưa có danh mục nào trong cơ sở dữ liệu.")

        except Exception as e:
            print("❌ Lỗi khi lấy danh sách danh mục:", e)
        finally:
            cursor.close()
            conn.close()

    return danh_sach
