# 🔐 Password Hash Auditor

A beginner-friendly cybersecurity project for auditing password hashes using Python and John the Ripper.



\


## 📌 Project Overview

Password Hash Auditor is a Python-based cybersecurity tool designed to analyze password hashes and identify weak passwords through dictionary-based password auditing.

The project integrates John the Ripper with Python to automate hash auditing, analyze results, calculate recovery statistics, and generate security reports.

This project is developed for educational purposes and authorized security testing.

## 🎯 Objectives

- Generate MD5 and SHA-256 password hashes.
- Identify possible hash types.
- Perform dictionary-based password auditing.
- Integrate John the Ripper with Python.
- Identify weak and commonly used passwords.
- Calculate cracked and remaining hash statistics.
- Generate automated TXT and CSV reports.
- Provide a simple command-line interface.

## 🛠️ Technologies Used

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| Python          | Main programming language |
| Kali Linux      | Testing environment       |
| John the Ripper | Password hash auditing    |
| MD5             | Hash testing              |
| SHA-256         | Hash testing              |
| RockYou         | Dictionary wordlist       |
| Git & GitHub    | Version control           |

## 📂 Project Structure

```text
password-hash-auditor/
│
├── docs/
│   └── examples/
│       ├── md5_sample.txt
│       └── sha256_sample.txt
│
├── hashes/
│   ├── md5_hashes.txt
│   └── sha256_hashes.txt
│
├── reports/
│   └── .gitkeep
│
├── screenshots/
│
├── scripts/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── hash_generator.py
│   ├── hash_analyzer.py
│   ├── password_auditor.py
│   └── report_generator.py
│
├── tests/
│   ├── __init__.py
│   └── test_password_auditor.py
│
├── wordlists/
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/password-hash-auditor.git

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

Verify installation:

```bash
john
```

### 5. Prepare the RockYou wordlist

```bash
sudo gzip -dk /usr/share/wordlists/rockyou.txt.gz
```

If the wordlist is already extracted, this step can be skipped.

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

[ MAIN MENU ]

1. Audit MD5 Hashes
2. Audit SHA-256 Hashes
3. Audit All Hashes
4. View Previous TXT Report
5. View Project Information
0. Exit
```

Select an option to perform the required password hash audit.

## 📊 Features

### 1. Hash Generation

Generate MD5 and SHA-256 hashes using Python's hashlib library.

### 2. Hash Analysis

Identify possible hash algorithms using hexadecimal hash lengths and format validation.

### 3. Password Auditing

Use John the Ripper to perform dictionary-based password recovery against authorized test hashes.

### 4. Automated Reporting

Generate security reports containing:

- Total unique hashes
- Successfully recovered hashes
- Remaining hashes
- Recovery percentage
- Security recommendations

### 5. Report Export

Reports are generated in:

```text
reports/
├── security_audit_report.txt
└── security_audit_report.csv
```

## 🧪 Testing

Run automated unit tests:

```bash
python -m unittest discover -s tests -v
```

The project includes 12 unit tests covering:

- MD5 hash generation
- SHA-256 hash generation
- Hash identification
- Invalid hash detection
- Duplicate hash removal
- Empty hash file validation
- Unsupported algorithm handling

**Latest test result: 12/12 tests passed.**

## 📈 Sample Audit Results

The initial local lab dataset produced the following results:

| Algorithm   |  Total | Cracked | Remaining |
| ----------- | -----: | ------: | --------: |
| MD5         |     10 |      10 |         0 |
| SHA-256     |     11 |      10 |         1 |
| **Overall** | **21** |  **20** |     **1** |

Overall dictionary recovery rate: **95.24%**

These are results from a synthetic educational dataset, not a benchmark of real-world password security.

## 🔒 Security Recommendations

- Avoid common and predictable passwords.
- Use unique passwords for every account.
- Use Argon2id or bcrypt for password storage.
- Use unique salts for password hashes.
- Enable Multi-Factor Authentication.
- Never store plaintext passwords.

**Security note:** MD5 and SHA-256 are not recommended for password storage. Modern password-storage systems should use dedicated password hashing algorithms such as Argon2id.

## ⚠️ Disclaimer

This project is developed strictly for educational purposes and authorized security auditing.

Only use password hashes that you own or have explicit permission to test.

Do not use this tool to access unauthorized accounts, systems, or confidential credentials.

## 👨‍💻 Author

**Nirmal Shehan**

Cybersecurity Student | Ethical Hacking | Python | Network Security

GitHub: [https://github.com/nim2328](https://github.com/nim2328)

LinkedIn: [https://www.linkedin.com/in/nirmal-shehan-b40896387/](https://www.linkedin.com/in/nirmal-shehan-b40896387/)

## ⭐ Support

If you find this project useful for learning cybersecurity, consider giving the repository a star!

---

**Project:** Password Hash Auditor
**Category:** Cybersecurity / Ethical Hacking
**Version:** 1.0.0
