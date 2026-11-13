
def identify_hash(hash_value: str) -> str:
    """Identify likely hash types by hexadecimal length."""

    value = hash_value.strip().lower()

    if not value:
        return "INVALID"

    if not all(char in "0123456789abcdef" for char in value):
        return "INVALID"

    if len(value) == 32:
        return "MD5 (possible)"

    if len(value) == 64:
        return "SHA-256 (possible)"

    return "UNKNOWN"


if __name__ == "__main__":
    samples = [
        "ea4d8fcd176bc4c1585d198480bef351",
        "03f7188cbee8b567760b6167d388fef83216a6434bb91664d8ca53b8d69ff28d",
    ]

    for item in samples:
        print(f"{item} -> {identify_hash(item)}")
