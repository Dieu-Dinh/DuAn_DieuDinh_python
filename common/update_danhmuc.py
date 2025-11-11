from ketnoi.ketnoi_mySql import create_connection

def update_danhmuc(danhmuc_id, ten_moi=None, mo_ta_moi=None):
    """Cập nhật tên và mô tả danh mục theo ID"""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()

            # Tạo câu SQL động (chỉ cập nhật trường có giá trị)
            sql = "UPDATE danhmuc SET "
            params = []

            if ten_moi is not None:
                sql += "ten_danhmuc = %s, "
                params.append(ten_moi)

            if mo_ta_moi is not None:
                sql += "mo_ta = %s, "
                params.append(mo_ta_moi)

            # Xóa dấu ',' thừa ở cuối chuỗi
            sql = sql.rstrip(", ")
            sql += " WHERE id = %s"
            params.append(danhmuc_id)

            cursor.execute(sql, tuple(params))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã cập nhật danh mục ID = {danhmuc_id}")
            else:
                print(f"⚠️ Không tìm thấy danh mục có ID = {danhmuc_id}")

        except Exception as e:
            print("❌ Lỗi khi cập nhật danh mục:", e)
        finally:
            cursor.close()
            conn.close()
