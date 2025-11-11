from ketnoi.ketnoi_mySql import create_connection

def insert_danhmuc(ten_danhmuc, mo_ta=None):
    """Thêm một danh mục mới vào bảng danhmuc"""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO danhmuc (ten_danhmuc, mo_ta)
                VALUES (%s, %s)
            """
            values = (ten_danhmuc, mo_ta)
            cursor.execute(sql, values)
            conn.commit()
            print("✅ Thêm danh mục thành công!")
        except Exception as e:
            print("❌ Lỗi khi thêm danh mục:", e)
        finally:
            cursor.close()
            conn.close()
