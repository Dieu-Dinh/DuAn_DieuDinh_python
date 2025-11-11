from ketnoi.ketnoi_mySql import create_connection

def delete_danhmuc(danhmuc_id):
    """Xóa danh mục theo ID"""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM danhmuc WHERE id = %s"
            cursor.execute(sql, (danhmuc_id,))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã xóa danh mục có ID = {danhmuc_id}")
            else:
                print(f"⚠️ Không tìm thấy danh mục có ID = {danhmuc_id}")

        except Exception as e:
            print("❌ Lỗi khi xóa danh mục:", e)
        finally:
            cursor.close()
            conn.close()
