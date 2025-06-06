# 🔌 Advanced TCP/FTP Port Connector Tool

> A professional, modular Python tool to connect and interact with **TCP** and **FTP** servers using **Object-Oriented Programming (OOP)** principles.

---

## 🖼️ Terminal Banner

```python
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
````

When you run `main.py`, this banner will display in the terminal.

---

## 📦 Features

* 🔄 **TCP Client** — Connect, send, and receive data from any TCP port.
* 📁 **FTP Client** — Login, browse, and interact with FTP servers.
* 🧱 Modular OOP structure for scalability and maintainability.
* 🛡️ Built-in error handling and clean user prompts.
* 💻 CLI-based interface for flexibility.

---

## 🗂️ Project Structure

```
tcp_ftp_tool/
│
├── main.py                # CLI entry point
├── core/
│   ├── __init__.py
│   ├── tcp_client.py      # TCP Client Class
│   └── ftp_client.py      # FTP Client Class
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shiboshreeroy/tcp_ftp_tool.git
cd tcp_ftp_tool
```

### 2️⃣ Install Requirements

> ✅ This tool uses only Python’s standard library — no extra dependencies required!

```bash
python --version   # Ensure Python 3.x is installed
```

---

## ⚙️ Usage

### 🟢 Run the tool

```bash
python main.py
```

### ✨ Example: TCP Client

```
=== Advanced Port Connector ===
1. TCP Connect
2. FTP Connect
Choose [1/2]: 1

Enter TCP host: example.com
Enter TCP port: 80
Send (type 'exit' to quit): GET / HTTP/1.1
```

### ✨ Example: FTP Client

```
=== Advanced Port Connector ===
1. TCP Connect
2. FTP Connect
Choose [1/2]: 2

Enter FTP host: ftp.example.com
Enter FTP username (default anonymous): user
Enter FTP password (blank for anonymous): ****
```

---

## 🧠 How It Works

* `TCPClient` (in `tcp_client.py`) uses the `socket` module to manage low-level TCP connections.
* `FTPClient` (in `ftp_client.py`) wraps Python’s `ftplib` to handle authentication, listing, and command execution on FTP servers.
* `main.py` provides a command-line menu and displays the banner.

---

## 🛠️ Future Enhancements

* ✅ SFTP/FTPS support
* ✅ Save logs to files
* ✅ GUI (Tkinter / PyQT)
* ✅ Threaded port scanner

---

## 👨‍💻 Developer

**🧑‍💻 Shiboshree Roy**
Full-Stack Developer | Python, Rails, Systems & Network Tools
📫 Email: [shiboshreeroycse@gmail.com](mailto:shiboshreeroycse@gmail.com)
🌐 [GitHub](https://github.com/shiboshreeroy) | [LinkedIn](https://linkedin.com/in/shiboshree-roy)

---

## 📝 License

Licensed under the **MIT License**.
