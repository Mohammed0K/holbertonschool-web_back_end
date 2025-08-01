# Python - Async Comprehension

This project covers the concepts of **asynchronous execution** and **asynchronous programming** in Python, focusing on async generators, async comprehensions, and measuring asynchronous run times.

## Learning Objectives

- Write asynchronous generators in Python
- Use async comprehensions to collect data asynchronously
- Type-annotate generators and asynchronous functions
- Measure the runtime of asynchronous code

## Requirements

- Python 3.9
- Code style: pycodestyle (v2.5.x)
- All files end with a new line
- Modules and functions have full docstrings
- All functions and coroutines must be type-annotated

---

## Tasks

### 0. Async Generator

**File:** `0-async_generator.py`

Write a coroutine called `async_generator` that takes no arguments.  
It should loop 10 times, asynchronously wait 1 second each time, and yield a random number between 0 and 10.

Example:
```
python
import asyncio
async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
```


### 1. Async Comprehensions
File: 1-async_comprehension.py

Import async_generator from the previous task and write a coroutine called async_comprehension that collects 10 random numbers using an async comprehension over async_generator, and returns the list.

Example:
```
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
```

### 2. Run time for four parallel comprehensions
File: 2-measure_runtime.py

Import async_comprehension and write a coroutine called measure_runtime that executes async_comprehension four times in parallel using asyncio.gather.
It should measure the total runtime and return it.

Example:
```
import asyncio
measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    print(await measure_runtime())

asyncio.run(main())
```

---

## Usage
Each file can be run with the corresponding test script (e.g., 0-main.py, 1-main.py, 2-main.py), or you can import and use the coroutines in your own code.

---

## Author

Mohammed Alqabas

















