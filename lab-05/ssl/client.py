import socket
import ssl
import threading

# ===== Thông tin server =====
server_address = ("localhost", 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode("utf-8"))
    except Exception as e:
        print("Lỗi nhận dữ liệu:", e)
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng")

# ===== Tạo client socket =====
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

ssl_socket = context.wrap_socket(
    client_socket,
    server_hostname="localhost"
)

ssl_socket.connect(("localhost", 12345))

# ===== Thiết lập kết nối SSL =====
ssl_socket = context.wrap_socket(
    client_socket,
    server_hostname="localhost"
)

ssl_socket.connect(server_address)
print("Đã kết nối tới server")

# ===== Luồng nhận dữ liệu =====
receive_thread = threading.Thread(
    target=receive_data,
    args=(ssl_socket,),
    daemon=True
)
receive_thread.start()

# ===== Gửi dữ liệu lên server =====
try:
    while True:
        message = input("Nhập tin nhắn: ")
        if message.lower() == "exit":
            break
        ssl_socket.send(message.encode("utf-8"))
except KeyboardInterrupt:
    print("\nThoát chương trình")
finally:
    ssl_socket.close()
