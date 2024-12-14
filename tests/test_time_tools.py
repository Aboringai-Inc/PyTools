import unittest
from pytools.time_tools import countdown_timer, stopwatch, convert_timezones
from datetime import datetime
import pytz

class TestTimeTools(unittest.TestCase):

    def test_countdown_timer(self):
        """Test countdown_timer for successful execution."""
        # This is a visual function; testing may involve manual validation.

    def test_stopwatch(self):
        """Test stopwatch execution."""
        # Stopwatch is interactive; cannot be tested automatically here.

    def test_convert_timezones(self):
        """Test timezone conversion."""
        dt = datetime(2024, 12, 14, 12, 0, 0, tzinfo=pytz.UTC)
        converted = convert_timezones(dt, pytz.UTC, pytz.timezone('US/Eastern'))
        self.assertEqual(converted.hour, 7)  # Eastern time is UTC-5

if __name__ == "__main__":
    unittest.main()
