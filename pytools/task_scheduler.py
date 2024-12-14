import threading
import time

def schedule_task(function, interval, repeat=1):
    """Schedules a task to run at fixed intervals."""
    def task_runner():
        for _ in range(repeat):
            function()
            time.sleep(interval)

    thread = threading.Thread(target=task_runner)
    thread.start()
