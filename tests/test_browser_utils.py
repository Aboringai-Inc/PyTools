import unittest
from pytools.browser_utils import generate_safe_url

class TestBrowserUtils(unittest.TestCase):

    def test_generate_safe_url(self):
        """Test URL generation with encoded parameters."""
        base_url = "https://example.com"
        params = {"q": "hello world", "page": 1}
        result = generate_safe_url(base_url, params)
        self.assertEqual(result, "https://example.com?q=hello+world&page=1")

if __name__ == "__main__":
    unittest.main()
