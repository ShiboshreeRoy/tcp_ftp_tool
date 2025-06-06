import os
import time
from core.tcp_client import TCPClient
from core.ftp_client import FTPClient

def run_tcp():
    host = input("Enter TCP host: ")
    port = int(input("Enter TCP port: "))
    client = TCPClient(host, port)
    client.connect()
    while True:
        msg = input("Send (type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        client.send(msg)
        client.receive()
    client.close()

def run_ftp():
    host = input("Enter FTP host: ")
    user = input("Enter FTP username (default anonymous): ") or "anonymous"
    passwd = input("Enter FTP password (blank for anonymous): ")
    client = FTPClient(host, user, passwd)
    client.connect()
    client.list_files()
    client.disconnect()

def print_ascii_banner():
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = (
        "\033[92m    █████╗ ██████╗  █████╗ ███╗   ██╗██████╗ ███████╗██╗   ██╗\n"
        "   ██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔════╝╚██╗ ██╔╝\n"
        "   ███████║██████╔╝███████║██╔██╗ ██║██║  ██║█████╗   ╚████╔╝ \n"
        "   ██╔══██║██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██╔══╝    ╚██╔╝  \n"
        "   ██║  ██║██║     ██║  ██║██║ ╚████║██████╔╝███████╗   ██║   \n"
        "   ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝   ╚═╝   \n"
        "\033[91m           [ Advanced Port Connector | TCP / FTP Tool ]      \n"
        "\033[94m              Dev by Shiboshree Roy               \033[0m\n"
    )

    print(banner)
    time.sleep(1)

def main():
    print_ascii_banner()
    print("\033[93m1. TCP Connect")
    print("2. FTP Connect\033[0m")
    choice = input("\033[96mChoose [1/2]: \033[0m")
    if choice == '1':
        run_tcp()
    elif choice == '2':
        run_ftp()
    else:
        print("\033[91mInvalid choice.\033[0m")
        print("\033[91mExiting...\033[0m")

if __name__ == "__main__":
    main()
