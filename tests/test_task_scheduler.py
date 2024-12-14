import unittest
from pytools.task_scheduler import schedule_task
import time

class TestTaskScheduler(unittest.TestCase):

    def test_schedule_task(self):
        """Test if a scheduled task runs the correct number of times."""
        self.counter = 0

        def increment_counter():
            self.counter += 1

        schedule_task(increment_counter, interval=1, repeat=3)
        time.sleep(4)  # Wait for all scheduled tasks to finish
        self.assertEqual(self.counter, 3)

if __name__ == "__main__":
    unittest.main()
