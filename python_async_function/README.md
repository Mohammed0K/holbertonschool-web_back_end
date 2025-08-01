# Python Async Function Project

This project demonstrates asynchronous programming in Python using the `asyncio` and `random` modules.  
It covers the basics of coroutines, running multiple tasks concurrently, measuring runtime, and using `asyncio.Task`.

---

## **Project Structure**

python_async_function/

├── 0-basic_async_syntax.py

├── 1-concurrent_coroutines.py

├── 2-measure_runtime.py

├── 3-tasks.py

├── 4-tasks.py

├── 0-main.py

├── 1-main.py

├── 2-main.py

├── 3-main.py

└── 4-main.py


---

## **Tasks**

### 0. The basics of async
- **File:** `0-basic_async_syntax.py`
- **Description:**  
  Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (default 10), waits for a random delay between 0 and `max_delay` seconds (using floats), and returns the delay.
- **Usage Example:**
  
```
  python
  import asyncio
  wait_random = __import__('0-basic_async_syntax').wait_random
  print(asyncio.run(wait_random()))
  print(asyncio.run(wait_random(5)))
```

1. Let's execute multiple coroutines at the same time with async
File: 1-concurrent_coroutines.py

Description:
Write an async routine wait_n that takes two integers n and max_delay, spawns wait_random n times concurrently, and returns the list of delays in ascending order (by completion time, without using sort()).

Usage Example:
```
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n
print(asyncio.run(wait_n(5, 5)))
```

2. Measure the runtime
File: 2-measure_runtime.py

Description:
Create a measure_time function that measures the average total execution time for wait_n(n, max_delay) using the time module.

Usage Example:

```
measure_time = __import__('2-measure_runtime').measure_time
print(measure_time(5, 9))
```

3. Tasks
File: 3-tasks.py

Description:
Write a function task_wait_random that returns an asyncio.Task for wait_random(max_delay).

Usage Example:
```
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random
async def test(max_delay: int):
    task = task_wait_random(max_delay)
    await task
    print(type(task))
asyncio.run(test(5))
```

4. Tasks (Multiple Tasks)
File: 4-tasks.py

Description:
Write task_wait_n, similar to wait_n, but using task_wait_random to create the tasks.

Usage Example:
```
import asyncio
task_wait_n = __import__('4-tasks').task_wait_n
print(asyncio.run(task_wait_n(5, 6)))
```

---

Requirements
All Python files use the #!/usr/bin/env python3 shebang.

All modules and functions are documented with docstrings.

All functions and coroutines use type annotations.

All code is PEP8 compliant.

Only the standard library is used (asyncio, random, time, typing).

Each file can be run independently and tested using the provided *-main.py files.

How to Test
You can use the provided *-main.py files to test each module individually.
Example:

```
chmod +x *.py
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
```

Or run any file directly with Python:

```
python3 0-main.py
python3 1-main.py
```

---

# Author
```
Mohammed Alqabas
```

