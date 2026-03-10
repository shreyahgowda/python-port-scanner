# 🔐 Python Port Scanner

📌 Project Description

This project is a **multi-threaded port scanner built using Python**.
The tool scans a target website or IP address to identify **open ports and running services**.
Port scanning is a common technique used in **cybersecurity and penetration testing** to discover exposed network services on a system.

# 🚀 Features

* Scans ports **1–1024**
* Detects **open ports**
* Displays **service names** (HTTP, SSH, etc.)
* Uses **multithreading** for faster scanning
* Colored terminal output for better readability

# 🛠 Technologies Used

* **Python**
* **Socket Programming**
* **Multithreading** (`ThreadPoolExecutor`)
* **Colorama** (for colored terminal output)

# ▶ How to Run

# 1️⃣ Run the script
     python scanner.py

# 2️⃣ Enter the target IP or website
  Example:
          scanme.nmap.org

# 🖥 Example Output

Scanning target: scanme.nmap.org

Port 22 OPEN (ssh)
Port 80 OPEN (http)
Port 443 OPEN (https)

Scan completed

* authorized networks
* public testing servers such as `scanme.nmap.org`.
