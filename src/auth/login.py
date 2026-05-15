"""QA auth module â€” login feature branch."""


def login(username: str, password: str) -> bool:
    """Validate credentials (stub)."""
    if not username or not password:
        return False
    return username == "qa_user" and password == "qa_pass"


def logout(session_id: str) -> None:
    """Invalidate session (stub)."""
    print(f"Session {session_id} terminated.")
