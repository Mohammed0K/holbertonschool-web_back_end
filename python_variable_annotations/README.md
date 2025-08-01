# Python - Variable Annotations

## Overview

This project focuses on mastering **type annotations** in Python, including how to specify variable and function types, understand duck typing, and perform static type checking with `mypy`.

---

## General Requirements

- All code is written in **Python 3.9**.
- Each file starts with:
  ```python
  #!/usr/bin/env python3
  ```
- Follow the [pycodestyle](https://pycodestyle.pycqa.org/en/latest/) style guide.
- Every module, class, and function must include a meaningful **docstring** explaining its purpose.
- All files must be **executable** and end with a new line.
- Each task is implemented in its own file.
- All solutions have been tested using the provided `main.py` files for each task.

---

## Tasks List

### Mandatory Tasks

1. **add**
    - Write a function `add` that takes two floats and returns their sum.
    - Use type annotations for parameters and return value.

2. **concat**
    - Write a function `concat` that takes two strings and returns their concatenation.
    - Use type annotations.

3. **floor**
    - Write a function `floor` that takes a float and returns its floor as an integer.
    - Use type annotations.

4. **to_str**
    - Write a function `to_str` that converts a float to a string.
    - Use type annotations.

5. **Define Variables**
    - Define the following variables with type annotations:
        - `a`: int = 1
        - `pi`: float = 3.14
        - `i_understand_annotations`: bool = True
        - `school`: str = "Holberton"

6. **sum_list**
    - Write a function that takes a list of floats and returns their sum as a float.
    - Use the correct type from `typing`.

7. **sum_mixed_list**
    - Write a function that takes a list of ints and floats and returns their sum as a float.
    - Use `Union` from `typing`.

8. **to_kv**
    - Write a function that takes a string and an int or float, and returns a tuple containing the string and the square of the number (as a float).
    - Use `Tuple` and `Union` from `typing`.

9. **make_multiplier**
    - Write a function that takes a float and returns a function that multiplies a float by that value.
    - Use `Callable` from `typing`.

10. **element_length**
    - Write a function with the proper annotations that takes an iterable of sequences and returns a list of tuples with the element and its length.

11. **safe_first_element**
    - Write a function that returns the first element of a sequence or `None` if the sequence is empty.
    - Use `Optional` and `Any` from `typing`.

12. **safely_get_value**
    - Write a function with generic type annotations to get a value from a mapping (dictionary) safely.
    - Use `TypeVar`, `Union`, `Mapping`, and `Any` from `typing`.

13. **zoom_array (type checking)**
    - Annotate the provided function, make any necessary changes, and ensure it passes `mypy` checks.
    - Use `Tuple`, `List`, and `Any` from `typing`.

---

## How to Run

- Make each file executable (if on Linux/Mac):
  ```sh
  chmod +x filename.py
  ```
- Run the main file for each task to test your solution:
  ```sh
  ./0-main.py
  ./1-main.py
  # ...and so on
  ```
- Use `mypy` for static type checking:
  ```sh
  mypy filename.py
  ```

---

## References

- [Python Typing Documentation](https://docs.python.org/3/library/typing.html)
- [MyPy Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

---

## Author

Mohammed Alqabas
