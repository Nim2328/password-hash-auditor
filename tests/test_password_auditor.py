
import unittest
import tempfile
import hashlib

from pathlib import Path

from src.hash_generator import generate_hash
from src.hash_analyzer import identify_hash
from src.password_auditor import load_hashes


class TestHashGenerator(unittest.TestCase):

    def test_md5_generation(self):
        result = generate_hash("password", "md5")

        expected = hashlib.md5(
            b"password"
        ).hexdigest()

        self.assertEqual(result, expected)

    def test_sha256_generation(self):
        result = generate_hash("password", "sha256")

        expected = hashlib.sha256(
            b"password"
        ).hexdigest()

        self.assertEqual(result, expected)

    def test_unsupported_algorithm(self):
        with self.assertRaises(ValueError):
            generate_hash("password", "sha1")


class TestHashAnalyzer(unittest.TestCase):

    def test_md5_identification(self):
        result = identify_hash(
            "5f4dcc3b5aa765d61d8327deb882cf99"
        )

        self.assertEqual(result, "MD5 (possible)")

    def test_sha256_identification(self):
        result = identify_hash(
            hashlib.sha256(b"password").hexdigest()
        )

        self.assertEqual(result, "SHA-256 (possible)")

    def test_invalid_hash(self):
        result = identify_hash("invalid-hash")

        self.assertEqual(result, "INVALID")

    def test_unknown_hash(self):
        result = identify_hash("abcd1234")

        self.assertEqual(result, "UNKNOWN")


class TestHashFileLoader(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.hash_file = Path(self.temp_dir.name) / "hashes.txt"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_md5_hashes(self):
        hash_value = hashlib.md5(
            b"password"
        ).hexdigest()

        self.hash_file.write_text(
            hash_value + "\n",
            encoding="utf-8"
        )

        result = load_hashes(self.hash_file, "md5")

        self.assertEqual(result, [hash_value])

    def test_remove_duplicate_hashes(self):
        hash_value = hashlib.md5(
            b"password"
        ).hexdigest()

        self.hash_file.write_text(
            f"{hash_value}\n{hash_value}\n",
            encoding="utf-8"
        )

        result = load_hashes(self.hash_file, "md5")

        self.assertEqual(len(result), 1)

    def test_reject_invalid_hash(self):
        self.hash_file.write_text(
            "not-a-valid-hash\n",
            encoding="utf-8"
        )

        with self.assertRaises(ValueError):
            load_hashes(self.hash_file, "md5")

    def test_empty_hash_file(self):
        self.hash_file.write_text(
            "",
            encoding="utf-8"
        )

        with self.assertRaises(ValueError):
            load_hashes(self.hash_file, "md5")

    def test_unsupported_algorithm(self):
        with self.assertRaises(ValueError):
            load_hashes(self.hash_file, "sha1")


if __name__ == "__main__":
    unittest.main()
