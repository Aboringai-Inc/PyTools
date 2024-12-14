import time
from datetime import datetime, timedelta

def countdown_timer(seconds):
    """Starts a countdown timer."""
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def stopwatch():
    """Starts a simple stopwatch."""
    print("Stopwatch started! Press Ctrl+C to stop.")
    start_time = time.time()
    try:
        while True:
            elapsed = time.time() - start_time
            mins, secs = divmod(int(elapsed), 60)
            print(f"Elapsed: {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\nFinal Time: {mins:02d}:{secs:02d}")

def convert_timezones(dt, from_tz, to_tz):
    """Converts datetime from one timezone to another."""
    return dt.astimezone(to_tz)
