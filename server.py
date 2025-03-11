import socket
import signal
import sys

def create_response():
    response_body = "Hello, World!"
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{response_body}"
    )
    return response.encode()

def run_server(host='', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f'Server running on port {port}...')
        
        while True:
            try:
                client_socket, client_address = server_socket.accept()
                print(f"Connection from {client_address}")
                
                # 接收请求（但不处理内容）
                client_socket.recv(1024)
                
                # 发送响应
                response = create_response()
                client_socket.sendall(response)
                
                # 关闭客户端连接
                client_socket.close()
                
            except Exception as e:
                print(f"Error handling client: {e}")
                continue
                
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    # 设置信号处理
    signal.signal(signal.SIGTERM, lambda signo, frame: sys.exit(0))
    run_server() 