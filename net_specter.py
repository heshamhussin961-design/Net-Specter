import socket
import sys
import threading
from queue import Queue
from datetime import datetime
from colorama import Fore, Style, init

# ---------------------------------------------------------
# Tool Name: Net-Specter v2.0 (Deep Scan Mode)
# Author: Cyber Man
# Description: Advanced Port Scanner with Banner Grabbing
# ---------------------------------------------------------

init(autoreset=True)
print_lock = threading.Lock()

def banner_logo():
    print(Fore.RED + Style.BRIGHT + """
    =============================================
     _   _      _      ____                  _            
    | \ | | ___| |_   / ___| _ __   ___  ___| |_ ___ _ __ 
    |  \| |/ _ \ __|  \___ \| '_ \ / _ \/ __| __/ _ \ '__|
    | |\  |  __/ |_    ___) | |_) |  __/ (__| ||  __/ |   
    |_| \_|\___|\__|  |____/| .__/ \___|\___|\__\___|_|   
                     v2.0 (DEEP SCAN) 💀
    =============================================
    """ + Style.RESET_ALL)

def grab_banner(s, port):
    """
    وظيفة بتحاول تسرق معلومات الخدمة (Banner)
    """
    try:
        # لو البورت ويب (80/8080) لازم نبعت طلب HTTP عشان يرد
        if port in [80, 8080, 443]:
            s.send(b'HEAD / HTTP/1.1\r\n\r\n')
        
        # بنستقبل أول 1024 بايت من الرد
        banner_data = s.recv(1024).decode().strip()
        return banner_data
    except:
        return "Unknown Service"

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # زودنا الوقت ثانية عشان نلحق ناخد الرد
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            # البورت مفتوح؟ حلو.. ادخل هات "بطاقته"
            service_banner = grab_banner(s, port)
            
            # لو معرفناش نجيب البانر، هات الاسم الافتراضي
            if not service_banner or len(service_banner) < 2:
                try:
                    service_banner = socket.getservbyport(port)
                except:
                    service_banner = "Unknown"
            else:
                # تنظيف النص عشان ميكونش طويل أوي
                service_banner = service_banner.split('\n')[0][:50]

            with print_lock:
                # طباعة النتيجة بشكل مرعب واحترافي
                print(f"{Fore.GREEN}[+] Port {port:<5} OPEN | {Fore.CYAN}{service_banner}{Style.RESET_ALL}")
        
        s.close()
            
    except:
        pass

def threader(target, q):
    while True:
        port_worker = q.get()
        scan_port(target, port_worker)
        q.task_done()

def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Usage: python net_specter.py <Target IP/Domain>")
        sys.exit()

    target_input = sys.argv[1]
    
    try:
        target_ip = socket.gethostbyname(target_input)
    except socket.gaierror:
        print(Fore.RED + "\n[!] Hostname could not be resolved.")
        sys.exit()

    banner_logo()
    print(f"[*] Target Locked: {Fore.YELLOW}{target_ip}{Style.RESET_ALL}")
    print(f"[*] Mode: {Fore.RED}Deep Banner Grabbing{Style.RESET_ALL}")
    print("-" * 60)

    q = Queue()

    # عدد الخيوط (Threads)
    for x in range(50):
        t = threading.Thread(target=threader, args=(target_ip, q))
        t.daemon = True
        t.start()

    # فحص المنافذ المهمة والشائعة (عشان ننجز)
    # ممكن تغيرها لـ range(1, 10000) لو عايز فحص شامل
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3306, 3389, 5900, 8080]
    
    # أو نستخدم الـ range العادي
    for worker in range(1, 1025): 
        q.put(worker)

    q.join()
    
    print("-" * 60)
    print(Fore.GREEN + "[✓] Deep Scan Completed.")

if __name__ == "__main__":
    main()