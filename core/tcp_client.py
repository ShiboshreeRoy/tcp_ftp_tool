import socket

class TCPClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        try:
            self.sock = socket.create_connection((self.host, self.port), timeout=10)
            print(f"[+] Connected to TCP {self.host}:{self.port}")
        except Exception as e:
            print(f"[-] TCP Connection failed: {e}")

    def send(self, message: str):
        if self.sock:
            try:
                self.sock.sendall(message.encode())
                print("[+] Message sent.")
            except Exception as e:
                print(f"[-] Failed to send message: {e}")

    def receive(self, buffer_size=1024):
        if self.sock:
            try:
                data = self.sock.recv(buffer_size)
                print("[+] Received:", data.decode())
            except Exception as e:
                print(f"[-] Failed to receive data: {e}")

    def close(self):
        if self.sock:
            self.sock.close()
            print("[+] TCP connection closed.")
