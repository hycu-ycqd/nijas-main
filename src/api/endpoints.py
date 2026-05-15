"""QA REST API endpoint definitions â€” api feature branch."""
ENDPOINTS = {
    "health":   "/api/v1/health",
    "users":    "/api/v1/users",
    "items":    "/api/v1/items",
    "search":   "/api/v1/search",
    "export":   "/api/v1/export",
}


def get_endpoint(name: str) -> str:
    return ENDPOINTS.get(name, "/api/v1/unknown")
