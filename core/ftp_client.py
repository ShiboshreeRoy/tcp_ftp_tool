from ftplib import FTP

class FTPClient:
    def __init__(self, host: str, user: str = 'anonymous', passwd: str = ''):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.ftp = FTP()

    def connect(self):
        try:
            self.ftp.connect(self.host, 21, timeout=10)
            self.ftp.login(self.user, self.passwd)
            print(f"[+] Logged in to FTP {self.host} as {self.user}")
        except Exception as e:
            print(f"[-] FTP Connection failed: {e}")

    def list_files(self):
        try:
            files = self.ftp.nlst()
            print("[+] Files:")
            for file in files:
                print(" -", file)
        except Exception as e:
            print(f"[-] Failed to list files: {e}")

    def disconnect(self):
        try:
            self.ftp.quit()
            print("[+] FTP connection closed.")
        except:
            pass
