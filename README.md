# HUBAXRCE
# SSH Brute Forcer - Hubax Tool

A fucking fast and efficient SSH brute force tool written in Python. This shit uses multi-threading to blast through password lists and crack SSH logins like a goddamn wrecking ball. Perfect for pentesting and red team engagements.

## Features

- **Multi-threaded as fuck** - Blast through passwords with configurable thread count
- **Clean output** - Color-coded results so you know what the hell is happening
- **Smart stopping** - Stops immediately when valid credentials are found
- **Error handling** - Handles network issues and timeouts without crashing
- **Easy to use** - Simple command-line interface anyone can figure out

## Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Dependencies

Install the required packages:

```bash
pip install paramiko colorama
```

Or if you're using requirements.txt:

```bash
pip install -r requirements.txt
```

Where `requirements.txt` contains:
```
paramiko>=2.11.0
colorama>=0.4.6
```

### Clone the Repository

```bash
git clone https://github.com/n0merc/HUBAXRCE.git
cd ssh-brute-forcer
```

## Usage

### Basic Syntax

```bash
python ssh_brute.py -t TARGET_IP -u USERNAME -w WORDLIST
```

### Full Options

```bash
python ssh_brute.py -t 192.168.1.100 -u root -w passwords.txt -p 2222 -th 20 -to 5
```

### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-t`, `--target` | Target host IP address (REQUIRED) | - |
| `-u`, `--user` | Username to brute force (REQUIRED) | - |
| `-w`, `--wordlist` | Password wordlist file (REQUIRED) | - |
| `-p`, `--port` | SSH port number | 22 |
| `-th`, `--threads` | Number of concurrent threads | 10 |
| `-to`, `--timeout` | Connection timeout in seconds | 5 |

### Example Commands

**Basic attack:**
```bash
python ssh_brute.py -t 10.0.0.5 -u admin -w rockyou.txt
```

**Custom port and more threads:**
```bash
python ssh_brute.py -t 192.168.1.100 -u root -w passwords.txt -p 2222 -th 50
```

**With custom timeout:**
```bash
python ssh_brute.py -t 10.10.10.10 -u ubuntu -w common_passwords.txt -to 3
```

## Wordlists

You'll need a password wordlist. Here are some good ones:

- **rockyou.txt** - Classic and effective
- **darkc0de.txt** - Another solid choice
- **Common passwords** from SecLists
- Create your own with tools like Crunch or Cewl

## How It Works

1. **Loads the wordlist** - Reads passwords from your specified file
2. **Creates threads** - Spawns multiple worker threads for parallel attacks
3. **Attempts connections** - Each thread tries SSH authentication with different passwords
4. **Reports success** - Immediately stops and reports when valid credentials are found
5. **Handles failures** - Gracefully handles failed attempts and network issues



```
[*] Starting SSH brute force on 192.168.1.100:22
[*] Username: root
[*] Threads: 10
[-] Failed: root:password123
[-] Failed: root:admin
[-] Failed: root:123456
[+] FUCKING SUCCESS! root:toor works on 192.168.1.100:22
```

## Legal Disclaimer

**This tool is for authorized security testing and educational purposes only.** You are responsible for your own actions. Using this tool against systems you don't own or have explicit permission to test is illegal and unethical. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Contributing

Found a bug? Want to add features? Fork this shit and submit a pull request. Make sure your code doesn't suck.

## License

MIT License - Do whatever the fuck you want with it, but don't blame me when you get caught.

## Support

For issues, questions, or just to say what's up, open an issue on GitHub. No hand-holding though - figure basic shit out yourself.

---

**Made with ❤️ (and a lot of profanity) by the Hubax Team**
