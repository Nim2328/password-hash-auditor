
import hashlib


SUPPORTED_ALGORITHMS = ("md5", "sha256")


def generate_hash(password: str, algorithm: str) -> str:
    """Generate a hash for an explicitly supplied lab password."""

    algorithm = algorithm.lower()

    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError("Unsupported hashing algorithm.")

    password_bytes = password.encode("utf-8")

    if algorithm == "md5":
        return hashlib.md5(password_bytes).hexdigest()

    return hashlib.sha256(password_bytes).hexdigest()


if __name__ == "__main__":
    test_password = "welcome123"

    for algorithm in SUPPORTED_ALGORITHMS:
        result = generate_hash(test_password, algorithm)
        print(f"{algorithm.upper()}: {result}")
