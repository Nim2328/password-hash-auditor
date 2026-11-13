
import csv
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"


def generate_txt_report(results):
    """Generate a professional text audit report."""

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    total = sum(item["total"] for item in results)
    cracked = sum(item["cracked"] for item in results)
    remaining = sum(item["remaining"] for item in results)

    recovery_rate = (
        (cracked / total) * 100 if total else 0
    )

    timestamp = datetime.now().astimezone()

    report_path = REPORTS_DIR / "security_audit_report.txt"

    with report_path.open("w", encoding="utf-8") as file:

        file.write("=" * 55 + "\n")
        file.write("          PASSWORD HASH AUDIT REPORT\n")
        file.write("=" * 55 + "\n\n")

        file.write(
            f"Generated At : {timestamp.isoformat(timespec='seconds')}\n"
        )

        file.write("Project      : Password Hash Auditor\n")
        file.write("Assessment   : Authorized Lab Testing\n\n")

        file.write("-" * 55 + "\n")
        file.write("AUDIT SUMMARY\n")
        file.write("-" * 55 + "\n")

        file.write(f"Total Hashes       : {total}\n")
        file.write(f"Cracked Hashes     : {cracked}\n")
        file.write(f"Remaining Hashes   : {remaining}\n")
        file.write(f"Recovery Rate      : {recovery_rate:.2f}%\n\n")

        file.write("-" * 55 + "\n")
        file.write("ALGORITHM RESULTS\n")
        file.write("-" * 55 + "\n")

        for item in results:
            file.write(f"\nAlgorithm       : {item['algorithm']}\n")
            file.write(f"Total           : {item['total']}\n")
            file.write(f"Cracked         : {item['cracked']}\n")
            file.write(f"Remaining       : {item['remaining']}\n")
            file.write(f"Recovery Rate   : {item['percentage']:.2f}%\n")

        file.write("\n" + "-" * 55 + "\n")
        file.write("SECURITY RECOMMENDATIONS\n")
        file.write("-" * 55 + "\n")

        recommendations = [
            "Avoid common and predictable passwords.",
            "Use unique passwords for every account.",
            "Use Argon2id or bcrypt for password storage.",
            "Use unique salts for password hashes.",
            "Enable Multi-Factor Authentication.",
            "Never store plaintext passwords.",
        ]

        for index, recommendation in enumerate(
            recommendations, start=1
        ):
            file.write(f"{index}. {recommendation}\n")

        file.write("\n")
        file.write("Note: Recovery rate measures dictionary recovery,\n")
        file.write("not an absolute measure of password strength.\n")

        file.write("\n" + "=" * 55 + "\n")
        file.write("             END OF REPORT\n")
        file.write("=" * 55 + "\n")

    return report_path


def generate_csv_report(results):
    """Export individual algorithm results as CSV."""

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report_path = REPORTS_DIR / "security_audit_report.csv"

    fieldnames = [
        "algorithm",
        "total",
        "cracked",
        "remaining",
        "percentage",
        "audit_status",
    ]

    with report_path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for item in results:
            writer.writerow({
                "algorithm": item["algorithm"],
                "total": item["total"],
                "cracked": item["cracked"],
                "remaining": item["remaining"],
                "percentage": item["percentage"],
                "audit_status": (
                    "Completed" if item["total"] > 0 else "Empty"
                ),
            })

    return report_path


def generate_reports(results):
    """Generate all supported report formats."""

    if not results:
        raise ValueError("No audit results available")

    txt_path = generate_txt_report(results)
    csv_path = generate_csv_report(results)

    print("\n[+] Reports generated successfully!")
    print(f"[+] TXT Report : {txt_path}")
    print(f"[+] CSV Report : {csv_path}")
