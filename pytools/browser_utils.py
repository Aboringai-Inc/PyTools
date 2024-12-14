from urllib.parse import urlencode

def generate_safe_url(base_url, params):
    """Generates a safe URL with encoded query parameters."""
    return f"{base_url}?{urlencode(params)}"
