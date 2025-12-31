import socket as s
import threading
from colorama import Fore, Style, init
init(autoreset=True)
while True:
    while True:
        IP = input(Fore.GREEN + "Enter IP address: ")
        if IP.count('.') != 3:
            print(Fore.RED + "Invalid IP address. Please try again.\n[!] IPv4 format: xxx.xxx.xxx.xxx where xxx is between 0-255\n")
            continue
        try:
            s.inet_aton(IP)
            break
        except s.error:
            print(Fore.RED + "Invalid IP address. Please try again.\n[!] IPv4 format: xxx.xxx.xxx.xxx where xxx is between 0-255\n")
        continue

    while True:
        try:
            MinPort = int(input(Fore.GREEN + "Enter Minimum port number: "))
            MaxPort = int(input(Fore.GREEN + "Enter Maximum port number: "))
        except ValueError:
            print(Fore.RED +"Ports must be numbers.\n")
            continue
        if 1 <= MinPort <= 65535 and 1 <= MaxPort <= 65535 and MinPort <= MaxPort:
            break
        else:
            print(Fore.RED + "Invalid port range. Ports must be between 1 and 65535, and MinPort ≤ MaxPort.\n")
        continue

    while True:
        try: 
            MaxThreads = int(input(
                f"{Fore.YELLOW}[!] Be careful: high thread counts can stress your PC\n"
                f"{Fore.GREEN}Enter maximum number of threads (suggested 100-500): "
            ))
        except ValueError:
            print(Fore.RED + "Thread count must be a positive integer.\n")
            continue
        if MaxThreads < 1:
            print(Fore.RED + "Thread count must be a positive integer.\n")
            continue
        break

    
    thread_limit = threading.Semaphore(MaxThreads)


    def scanning(IP, MinPort, MaxPort):
        print(f"==Thanks for using Nostromis Port Scanner v2==\n")
        print(f"{Fore.GREEN}Scanning IP address: {IP} from port {MinPort} to {MaxPort}\n")
        open_ports = []
        def scan_port(port):
            with thread_limit:
                sock = s.socket(s.AF_INET, s.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((IP, port))
                print(Fore.YELLOW + f"[/] Scanning port {port}...\n")
                if result == 0:
                    open_ports.append(port)
                    print(Fore.GREEN + f"[!] Port {port} is open HAHA GET COMPROMISED\n")
                sock.close()
        threads = []
        for port in range(MinPort, MaxPort + 1):
            t = threading.Thread(target=scan_port, args=(port,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

        print(Fore.GREEN + "Scanning Finished.\nThank you for using Nostromis Port Scanner v2.")
        if open_ports:
            print(Fore.CYAN + f"Open ports: {', '.join(map(str, open_ports))}")
        else:
            print(Fore.YELLOW + "No open ports found.")
        print("Follow me on GitHub: github.com/Nostromis")
        print("Follow me on X: x.com/Nostromis1")
        print("Press Enter to exit.")
        print("Press 1 to perform another scan.")

    scanning(IP, MinPort, MaxPort)
    console = input()
    if console == "":
        exit()
    elif console == "1":
        continue