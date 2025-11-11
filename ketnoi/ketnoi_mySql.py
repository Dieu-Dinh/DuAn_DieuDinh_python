import mysql.connector
from mysql.connector import Error

def create_connection():
    """Tạo kết nối đến MySQL Database"""
    try:
        connection = mysql.connector.connect(
            host='localhost',       # hoặc 127.0.0.1
            user='root',            # tài khoản MySQL
            password='',  # thay bằng mật khẩu thật
            database='quanlythuocankhang'    # thay bằng tên CSDL bạn đã tạo
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
