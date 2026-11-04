import requests


class ApiClient:
    """Minimal API client; configure base URL and auth after API review."""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, path: str, **kwargs):
        return self.session.get(
            f"{self.base_url}/{path.lstrip('/')}",
            timeout=self.timeout,
            **kwargs,
        )
