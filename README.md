# 🔐 Password Hash Auditor

A Python-based cybersecurity tool for auditing password hashes using John the Ripper. Designed for educational purposes and authorized security testing.

## 📌 Project Overview

Password Hash Auditor automates dictionary-based password auditing through Python and John the Ripper. It validates hash files, analyzes audit results, calculates password recovery statistics, and generates TXT and CSV security reports.

## 🎯 Objectives

- Generate MD5 and SHA-256 hashes.
- Identify possible hash types.
- Perform dictionary-based password auditing.
- Integrate John the Ripper with Python.
- Identify weak and commonly used passwords.
- Calculate cracked and remaining hash statistics.
- Generate automated security reports.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Kali Linux | Testing environment |
| John the Ripper | Password auditing engine |
| MD5 | Hash testing |
| SHA-256 | Hash testing |
| RockYou | Dictionary wordlist |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
password-hash-auditor/
├── docs/
│   └── examples/
├── hashes/
│   ├── md5_hashes.txt
│   └── sha256_hashes.txt
├── reports/
│   └── .gitkeep
├── screenshots/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── hash_generator.py
│   ├── hash_analyzer.py
│   ├── password_auditor.py
│   └── report_generator.py
├── tests/
│   ├── __init__.py
│   └── test_password_auditor.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nim2328/password-hash-auditor.git
cd password-hash-auditor
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install John the Ripper

```bash
sudo apt update
sudo apt install john -y
```

### 5. Prepare the RockYou wordlist

```bash
sudo gzip -dk /usr/share/wordlists/rockyou.txt.gz
```

If it is already extracted, skip this step.

## 🚀 Usage

Run the application from the project root:

```bash
python src/main.py
```

### Main Menu

```text
========================================
       PASSWORD HASH AUDITOR
========================================

1. Audit MD5 Hashes
2. Audit SHA-256 Hashes
3. Audit All Hashes
4. View Previous TXT Report
5. View Project Information
0. Exit
```

Select an option to perform the required audit.

## ✨ Features

### 1. Hash Generation
Generate MD5 and SHA-256 hashes using Python's `hashlib` library.

### 2. Hash Analysis
Identify possible hash algorithms through hexadecimal length and format validation.

### 3. Password Auditing
Use John the Ripper to perform dictionary-based password recovery against authorized test hashes.

### 4. Automated Reporting
Generate TXT and CSV reports containing:

- Total unique hashes
- Successfully recovered hashes
- Remaining hashes
- Recovery percentage
- Security recommendations

### 5. Unit Testing
Automated tests validate hash generation, hash identification, input validation, duplicate removal, and unsupported algorithms.

## 🧪 Testing

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

**Development test result: 12/12 tests passed.**

## 📊 Sample Data

The repository includes synthetic sample hashes for MD5 and SHA-256. These are intended for controlled educational testing.

Dictionary recovery results depend on the supplied hashes and wordlist. A successful dictionary recovery does not represent a definitive measurement of real-world password strength.

## 🔒 Security Recommendations

- Avoid common and predictable passwords.
- Use unique passwords for every account.
- Use Argon2id or bcrypt for password storage.
- Generate a unique salt for each password.
- Enable Multi-Factor Authentication.
- Never store plaintext passwords.

**Security note:** MD5 and SHA-256 are not recommended for password storage. Modern applications should use dedicated password hashing algorithms such as Argon2id.

## ⚠️ Disclaimer

This project is developed strictly for educational purposes and authorized security auditing.

Only test password hashes that you own or have explicit permission to audit. Do not use this tool to access unauthorized accounts, systems, or confidential credentials.

## 👨‍💻 Author

**Nirmal Shehan**

Cybersecurity Student | Ethical Hacking | Python | Network Security

- GitHub: https://github.com/Nim2328
- LinkedIn: https://www.linkedin.com/in/nirmal-shehan-b40896387/

## ⭐ Support

If you find this project useful for learning cybersecurity, consider giving the repository a star!

---

**Project:** Password Hash Auditor  
**Category:** Cybersecurity / Ethical Hacking  
**Version:** 1.0.0
