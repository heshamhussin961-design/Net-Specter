# 🕸️ Net-Specter

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

**Net-Specter** is an advanced, multi-threaded network scanner designed for penetration testers and cybersecurity enthusiasts. Unlike simple port scanners, Net-Specter performs **Deep Banner Grabbing** to identify running services, versions, and operating systems specifics.

## ⚡ Key Features

* **🚀 Turbo Mode:** Utilizes Multi-threading (100+ threads) to scan thousands of ports in seconds.
* **🕵️ Deep Inspection:** Performs full Banner Grabbing to detect service versions (e.g., Apache 2.4, OpenSSH 8.0).
* **🎨 Smart UI:** Color-coded terminal output for easy reading and analysis.
* **🛡️ Error Handling:** Auto-skips filtered ports and timeouts to maintain speed.
* **🌐 DNS Resolution:** Automatically resolves Domain Names to IP addresses.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Net-Specter.git](https://github.com/YOUR_USERNAME/Net-Specter.git)
    cd Net-Specter
    ```

2.  **Install dependencies:**
    ```bash
    pip install colorama
    ```

## 🛠️ Usage

Simply run the script with the target IP or Domain:

```bash
python net_specter.py <TARGET>
