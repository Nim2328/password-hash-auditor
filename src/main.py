
from pathlib import Path

from password_auditor import (
    audit_hash_file,
    display_results,
    WORDLIST,
    PROJECT_ROOT,
)

from report_generator import generate_reports


# Project configuration
HASH_FILES = {
    "1": ("md5", PROJECT_ROOT / "hashes" / "md5_hashes.txt"),
    "2": ("sha256", PROJECT_ROOT / "hashes" / "sha256_hashes.txt"),
}


def display_banner():
    print("\n")
    print("=" * 55)
    print("              PASSWORD HASH AUDITOR")
    print("=" * 55)
    print("       Cybersecurity | Ethical Hacking Lab")
    print("=" * 55)


def display_menu():
    print("\n[ MAIN MENU ]")
    print("-" * 40)
    print("1. Audit MD5 Hashes")
    print("2. Audit SHA-256 Hashes")
    print("3. Audit All Hashes")
    print("4. View Previous TXT Report")
    print("5. View Project Information")
    print("0. Exit")
    print("-" * 40)


def run_audit(algorithms):
    """Run selected audits and generate reports."""

    results = []

    for algorithm, hash_file in algorithms:

        try:
            result = audit_hash_file(
                algorithm,
                hash_file,
                WORDLIST
            )

            display_results(result)
            results.append(result)

        except Exception as error:
            print(
                f"\n[ERROR] {algorithm.upper()} audit failed: {error}"
            )

    if results:
        try:
            generate_reports(results)

        except (OSError, ValueError) as error:
            print(f"\n[REPORT ERROR] {error}")

    else:
        print("\n[!] No successful audit results available.")


def view_previous_report():
    """Display the previously generated TXT report."""

    report_path = (
        PROJECT_ROOT / "reports" / "security_audit_report.txt"
    )

    if not report_path.is_file():
        print("\n[!] No previous report found.")
        return

    print("\n" + "=" * 55)
    print("           PREVIOUS SECURITY REPORT")
    print("=" * 55)

    print(report_path.read_text(encoding="utf-8"))

    print("=" * 55)


def display_project_information():
    print("\n" + "=" * 45)
    print("          PROJECT INFORMATION")
    print("=" * 45)

    print("Project Name : Password Hash Auditor")
    print("Version      : 1.0")
    print("Language     : Python")
    print("Platform     : Kali Linux")
    print("Engine       : John the Ripper")
    print("Algorithms   : MD5, SHA-256")
    print("Reports      : TXT, CSV")
    print("Purpose      : Authorized password auditing")

    print("=" * 45)


def main():
    display_banner()

    while True:

        display_menu()

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            run_audit([HASH_FILES["1"]])

        elif choice == "2":
            run_audit([HASH_FILES["2"]])

        elif choice == "3":
            run_audit([
                HASH_FILES["1"],
                HASH_FILES["2"],
            ])

        elif choice == "4":
            view_previous_report()

        elif choice == "5":
            display_project_information()

        elif choice == "0":
            print("\n[*] Exiting Password Hash Auditor.")
            print("[+] Thank you for using the tool!\n")
            break

        else:
            print("\n[!] Invalid option. Please try again.")


if __name__ == "__main__":
    main()
