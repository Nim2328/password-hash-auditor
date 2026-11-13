
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Project configuration
PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"

# Allow imports from the src directory
sys.path.insert(0, str(Path(__file__).resolve().parent))

from report_generator import generate_reports


WORDLIST = Path("/usr/share/wordlists/rockyou.txt")

HASH_FORMATS = {
    "md5": {
        "john_format": "Raw-MD5",
        "length": 32,
    },
    "sha256": {
        "john_format": "Raw-SHA256",
        "length": 64,
    },
}


def load_hashes(hash_file, algorithm):
    """Load and validate unique hexadecimal hashes."""

    if algorithm not in HASH_FORMATS:
        raise ValueError("Unsupported hashing algorithm")

    hash_path = Path(hash_file)

    if not hash_path.is_file():
        raise FileNotFoundError(
            f"Hash file not found: {hash_path}"
        )

    expected_length = HASH_FORMATS[algorithm]["length"]

    hashes = []

    for line_number, line in enumerate(
        hash_path.read_text(encoding="utf-8").splitlines(),
        start=1
    ):
        value = line.strip().lower()

        if not value:
            continue

        if (
            len(value) != expected_length
            or not re.fullmatch(r"[0-9a-f]+", value)
        ):
            raise ValueError(
                f"Invalid {algorithm.upper()} hash "
                f"at line {line_number}"
            )

        hashes.append(value)

    # Remove duplicate hashes
    unique_hashes = list(dict.fromkeys(hashes))

    if not unique_hashes:
        raise ValueError("No valid hashes found")

    return unique_hashes


def audit_hash_file(algorithm, hash_file, wordlist=WORDLIST):
    """Perform password auditing using John the Ripper."""

    algorithm = algorithm.lower()

    if algorithm not in HASH_FORMATS:
        raise ValueError("Unsupported algorithm")

    john = shutil.which("john")

    if not john:
        raise RuntimeError(
            "John the Ripper is not installed"
        )

    wordlist = Path(wordlist)

    if not wordlist.is_file():
        raise FileNotFoundError(
            f"Wordlist not found: {wordlist}"
        )

    hash_path = Path(hash_file).resolve()

    hashes = load_hashes(hash_path, algorithm)

    REPORTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    pot_file = REPORTS_DIR / f"{algorithm}_audit.pot"

    format_name = HASH_FORMATS[algorithm]["john_format"]

    command = [
        john,
        f"--format={format_name}",
        f"--wordlist={wordlist}",
        f"--pot={pot_file}",
        str(hash_path),
    ]

    print(f"\n[*] Starting {algorithm.upper()} audit...")
    print(f"[*] Unique hashes: {len(hashes)}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=600
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        raise RuntimeError(
            f"John audit failed: {result.stderr}"
        )

    # Retrieve results without displaying plaintext passwords
    show_command = [
        john,
        "--show=left",
        f"--format={format_name}",
        f"--pot={pot_file}",
        str(hash_path),
    ]

    show_result = subprocess.run(
        show_command,
        capture_output=True,
        text=True,
        timeout=60
    )

    if show_result.returncode != 0:
        raise RuntimeError(
            "Failed to retrieve John audit results"
        )

    summary = (
        show_result.stdout
        + "\n"
        + show_result.stderr
    )

    match = re.search(
        r"(\d+)\s+password hashes? cracked,\s*(\d+)\s+left",
        summary,
        re.IGNORECASE
    )

    if not match:
        raise RuntimeError(
            "Could not parse John audit summary"
        )

    cracked = int(match.group(1))
    remaining = int(match.group(2))

    total = len(hashes)

    # Validate the result counts
    if cracked + remaining != total:
        raise RuntimeError(
            f"Hash count mismatch: expected {total}, "
            f"John reported {cracked + remaining}"
        )

    percentage = (
        (cracked / total) * 100
        if total > 0 else 0
    )

    return {
        "algorithm": algorithm.upper(),
        "total": total,
        "cracked": cracked,
        "remaining": remaining,
        "percentage": round(percentage, 2),
    }


def display_results(result):
    """Display audit statistics."""

    print("\n" + "=" * 45)
    print("          PASSWORD AUDIT RESULT")
    print("=" * 45)

    print(f"Algorithm       : {result['algorithm']}")
    print(f"Total Hashes    : {result['total']}")
    print(f"Cracked Hashes  : {result['cracked']}")
    print(f"Remaining       : {result['remaining']}")
    print(f"Recovery Rate   : {result['percentage']}%")

    print("=" * 45)


def main():
    """Run MD5 and SHA-256 audits and generate reports."""

    audit_configs = [
        (
            "md5",
            PROJECT_ROOT / "hashes" / "md5_hashes.txt"
        ),
        (
            "sha256",
            PROJECT_ROOT / "hashes" / "sha256_hashes.txt"
        ),
    ]

    results = []

    print("\n========================================")
    print("       PASSWORD HASH AUDITOR")
    print("========================================")

    for algorithm, hash_file in audit_configs:

        try:
            result = audit_hash_file(
                algorithm,
                hash_file,
                WORDLIST
            )

            display_results(result)

            results.append(result)

        except (
            ValueError,
            FileNotFoundError,
            RuntimeError,
            subprocess.TimeoutExpired
        ) as error:

            print(
                f"\n[ERROR] {algorithm.upper()}: {error}"
            )

        except OSError as error:

            print(
                f"\n[SYSTEM ERROR] {error}"
            )

    # Generate reports if at least one audit succeeded
    if results:

        try:
            generate_reports(results)

        except (OSError, ValueError) as error:

            print(
                f"\n[REPORT ERROR] {error}"
            )

    else:
        print("\n[!] No successful audits. Reports not generated.")

    print("\n[*] Password auditing process finished.")


if __name__ == "__main__":
    main()
