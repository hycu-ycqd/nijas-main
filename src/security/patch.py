"""QA security patch â€” hotfix branch."""
import hashlib
import os


def hash_password(password: str) -> str:
    salt = os.urandom(16).hex()
    digest = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{digest}"


def verify_password(password: str, stored_hash: str) -> bool:
    salt, digest = stored_hash.split(":", 1)
    return hashlib.sha256((salt + password).encode()).hexdigest() == digest
