

# PyTools

**PyTools** is a versatile Python module offering a collection of standalone utilities designed to simplify and enhance everyday development tasks. With tools ranging from time management and task scheduling to data parsing and random utility generation, PyTools is your go-to library for practical solutions.

---

## Features

- **Time Management Tools**: Countdown timers, stopwatches, and timezone conversions.
- **Browser Utilities**: Safe URL generation and form simulation.
- **Task Scheduling**: Schedule and automate tasks directly in Python.
- **Random Utilities**: Generate UUIDs, secure passwords, and unique random data.
- **CLI Utilities**: Progress bars, file processing helpers, and more.
- **Data Parsing**: Easy-to-use functions for CSV, JSON, and custom formats.
- **Math Helpers**: Duration calculations, matrix operations, and more.

---

## Installation

Clone the repository:
```bash
git clone https://github.com/Aboringai-Inc/PyTools.git
```

Navigate to the project directory and install:
```bash
cd PyTools
pip install .
```

---

## Quick Start

### Example 1: Countdown Timer
```python
from pytools.time_tools import countdown_timer

countdown_timer(10)  # Starts a 10-second countdown
```

### Example 2: Generate a Safe URL
```python
from pytools.browser_utils import generate_safe_url

url = generate_safe_url("https://example.com", {"q": "search", "page": 1})
print(url)  # Outputs: https://example.com?q=search&page=1
```

### Example 3: Task Scheduler
```python
from pytools.task_scheduler import schedule_task

def greet():
    print("Hello, World!")

schedule_task(greet, interval=10, repeat=5)  # Runs every 10 seconds, 5 times
```

---

## Modules

### Time Management
- Countdown timers, stopwatches, and timezone conversions.

### Browser Utilities
- Safe URL generation and form simulation.

### Task Scheduling
- Automate periodic function execution.

### Random Utilities
- Generate UUIDs, random subsets, and secure passwords.

### CLI Tools
- Progress bars, interactive prompts, and file processing.

### Data Parsing
- CSV and JSON parsing, custom file handling.

### Math Helpers
- Duration calculations, matrix operations, and more.

---

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Future Plans
- Add interactive documentation using `mkdocs`.
- Expand task scheduler functionalities.
- Publish the package on PyPI.
