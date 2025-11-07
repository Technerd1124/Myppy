# lab_experiments_1_to_5.py
# Covers Experiments 1–5
# Author: Generated for user
# Compact, functional, and readable version

import math

# -------------------------
# Experiment 1
# -------------------------

# Q1
def exp1_q1_intro(name, age, course):
    print(f"Name: {name}\nAge: {age}\nCourse: {course}")

# Q2
def exp1_q2_circle(radius):
    area = math.pi * radius**2
    circum = 2 * math.pi * radius
    print(f"Area={area:.2f}, Circumference={circum:.2f}")

# Q3
def exp1_q3_rectangle(l, b):
    area = l * b
    peri = 2 * (l + b)
    print(f"Area={area}, Perimeter={peri}")

# -------------------------
# Experiment 2
# -------------------------

# Q1 Even/Odd
def exp2_q1_even_odd(n):
    print("Even" if n % 2 == 0 else "Odd")

# Q2 Prime check
def exp2_q2_prime(n):
    if n < 2: print("Not Prime"); return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: print("Not Prime"); return
    print("Prime")

# Q3 Greater among three
def exp2_q3_greater(a,b,c):
    print(f"Greatest: {max(a,b,c)}")

# Q4 Character check
def exp2_q4_char(ch):
    if ch.isalpha():
        if ch.lower() in "aeiou":
            print("Alphabet & Vowel")
        else:
            print("Alphabet but not Vowel")
    else:
        print("Not an alphabet")

# Q5 Voting eligibility
def exp2_q5_vote(age):
    print("Eligible" if age >= 18 else "Not Eligible")

# Q6 Leap year
def exp2_q6_leap(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print("Leap Year")
    else:
        print("Not Leap Year")

# Q7 Positive/Negative/Zero
def exp2_q7_sign(n):
    print("Positive" if n > 0 else "Negative" if n < 0 else "Zero")

# Q8 Square root
def exp2_q8_sqrt(n):
    print(f"Sqrt={n**0.5:.2f}")

# Q9 Divisible by 5
def exp2_q9_div5(n):
    print("Divisible" if n % 5 == 0 else "Not Divisible")

# Q10 Grade of student
def exp2_q10_grade(marks):
    if marks >= 90: g="A"
    elif marks >= 75: g="B"
    elif marks >= 60: g="C"
    elif marks >= 40: g="D"
    else: g="Fail"
    print(f"Grade: {g}")

# -------------------------
# Experiment 3
# -------------------------

# Q1 10 natural numbers
def exp3_q1_naturals():
    for i in range(1,11): print(i, end=' ')
    print()

# Q2 Numbers till range
def exp3_q2_till(n):
    for i in range(1,n+1): print(i, end=' ')
    print()

# Q3 Even 1–20
def exp3_q3_even():
    for i in range(2,21,2): print(i, end=' ')
    print()

# Q4 Odd 1–20
def exp3_q4_odd():
    for i in range(1,21,2): print(i, end=' ')
    print()

# Q5 Table
def exp3_q5_table(n):
    for i in range(1,11): print(f"{n} x {i} = {n*i}")

# Q6 Sum first 15
def exp3_q6_sum15():
    print(sum(range(1,16)))

# Q7 Prime (while)
def exp3_q7_prime_while(n):
    i=2
    while i<=n//2:
        if n%i==0: print("Not Prime"); return
        i+=1
    print("Prime")

# Q8 Sum till 0
def exp3_q8_sum_till0():
    s=0
    while True:
        n=int(input("Enter number (0 to stop): "))
        if n==0: break
        s+=n
    print("Sum=",s)

# Q9 Factorial while
def exp3_q9_fact(n):
    f=1; i=1
    while i<=n:
        f*=i; i+=1
    print("Factorial=",f)

# Q10 Pattern *
def exp3_q10_pattern(n):
    for i in range(1,n+1):
        print("*"*i)

# -------------------------
# Experiment 4 – Tuples
# -------------------------

def exp4_q1_add_tuple(t):
    print("Sum=", sum(t))

def exp4_q2_clear_tuple(t):
    t=()
    print("Cleared tuple:", t)

def exp4_q3_remove_elem(t, val):
    l=list(t)
    if val in l: l.remove(val)
    print(tuple(l))

def exp4_q4_remove_dups(t):
    print(tuple(set(t)))

def exp4_q5_add_elem(t, val):
    print(t+(val,))

# -------------------------
# Experiment 5 – Lists
# -------------------------

def exp5_q1_create_list():
    l=[1,2,3,4]; print(l)

def exp5_q2_add_item(l, item):
    l.append(item); print(l)

def exp5_q3_remove_item(l, item):
    if item in l: l.remove(item)
    print(l)

def exp5_q4_update_list(l, idx, val):
    if 0<=idx<len(l): l[idx]=val
    print(l)

def exp5_q5_delete_list(l):
    del l
    print("List deleted")

# -------------------------
# Demo Main
# -------------------------

def main():
    print("Demo few outputs:")
    exp1_q1_intro("Dhanshri", 20, "BCA")
    exp1_q2_circle(5)
    exp2_q2_prime(11)
    exp3_q5_table(5)
    exp4_q4_remove_dups((1,2,2,3))
    exp5_q2_add_item([1,2,3], 4)

if __name__ == "__main__":
    main()



# lab_experiments_6_to_9.py
# Programs: Experiments 6, 7, 8, 9 (compact, organized as functions)
# Author: Generated for user
# Usage: import this file or run directly. Call functions as needed.

import math
import random
import time
import calendar
import functools
import operator
from typing import List, Tuple, Iterable

# -------------------------
# Experiment 6
# -------------------------

def exp6_q1_area_circle_math(radius: float) -> float:
    """Area of a circle using math.pi"""
    return math.pi * radius * radius

def exp6_q2_sqrt(n: float) -> float:
    """Square root using math.sqrt"""
    return math.sqrt(n)

def exp6_q3_factorial(n: int) -> int:
    """Factorial using math.factorial (handles n>=0)"""
    return math.factorial(n)

def exp6_q4_power(base: float, exp: float) -> float:
    """Power function"""
    return pow(base, exp)

def exp6_q5_random_numbers(count: int = 1, a: int = 0, b: int = 100) -> List[int]:
    """Return a list of random integers in [a,b]"""
    return [random.randint(a, b) for _ in range(count)]

def exp6_q6_print_time() -> str:
    """Return current local time string"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def exp6_q7_letter_indices(s: str) -> List[Tuple[int, str]]:
    """
    Return list of (index, letter) for each char in string s.
    Example use: find upper/lower positions.
    """
    return list(enumerate(s))

def exp6_q8_random_float_list(count: int = 5) -> List[float]:
    """Return list of random floats between 0 and 1"""
    return [random.random() for _ in range(count)]

def exp6_q9_print_calendar(year: int, month: int = None) -> str:
    """Return calendar: whole year if month is None, else specific month"""
    if month is None:
        return calendar.calendar(year)
    else:
        return calendar.month(year, month)

def exp6_q10_gcd(a: int, b: int) -> int:
    """GCD using math.gcd"""
    return math.gcd(a, b)

def exp6_q11_greetings(name: str) -> str:
    """Simple greeting"""
    return f"Hello, {name}! Have a great day."

def exp6_q12_power_repeat(base: float, exp: int) -> float:
    """Repeat of power; shows exponentiation by repeated multiplication"""
    result = 1.0
    for _ in range(abs(int(exp))):
        result *= base
    return result if exp >= 0 else 1.0 / result

def exp6_q13_area_circle(radius: float) -> float:
    """Another area-of-circle implementation (duplicate Q1)"""
    return 3.141592653589793 * radius * radius

def exp6_q14_arithmetic_ops(a: float, b: float) -> dict:
    """Return a dict of basic arithmetic operations"""
    return {
        'add': a + b,
        'sub': a - b,
        'mul': a * b,
        'div': a / b if b != 0 else None,
        'floor_div': a // b if b != 0 else None,
        'mod': a % b if b != 0 else None,
        'pow': a ** b
    }

def exp6_q15_min_max_avg(nums: Iterable[float]) -> dict:
    """Return min, max and average of numbers; empty returns None"""
    nums_list = list(nums)
    if not nums_list:
        return {'min': None, 'max': None, 'avg': None}
    return {'min': min(nums_list), 'max': max(nums_list), 'avg': sum(nums_list) / len(nums_list)}

def exp6_q16_factorial_loop(n: int) -> int:
    """Factorial implemented with loop"""
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def exp6_q17_squares(n: int) -> List[int]:
    """Return squares of numbers from 1..n"""
    return [i*i for i in range(1, n+1)]

def exp6_q18_multiplication(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

def exp6_q19_math_test(sample: List[float]) -> dict:
    """
    Example 'math test' operations: return count, mean, variance (population)
    Adaptable to other 'tests'—keeps it general.
    """
    if not sample:
        return {'count': 0, 'mean': None, 'variance': None}
    n = len(sample)
    mean = sum(sample) / n
    variance = sum((x - mean)**2 for x in sample) / n
    return {'count': n, 'mean': mean, 'variance': variance}

# -------------------------
# Experiment 7
# (Document had blanks; include placeholder functions)
# -------------------------

def exp7_placeholder_note():
    """Experiment 7 had no specific questions in the provided document."""
    return "Experiment 7: no tasks listed in the uploaded document."

# -------------------------
# Experiment 8: Exceptions
# -------------------------

def exp8_q1_basic_exception_handling(dividend: float, divisor: float) -> str:
    """Demonstrate try/except for division."""
    try:
        result = dividend / divisor
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero."
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"

def exp8_q2_multiple_exceptions(x: str, index: int, divisor: int) -> dict:
    """
    Demonstrate multiple exceptions: conversion, index and division.
    Returns a dict summarizing outcomes or errors.
    """
    out = {}
    try:
        num = int(x); out['converted'] = num
        arr = [10, 20, 30]; out['access'] = arr[index]
        out['divide'] = arr[0] // divisor
    except ValueError as e:
        out['error'] = f"ValueError: {e}"
    except IndexError as e:
        out['error'] = f"IndexError: {e}"
    except ZeroDivisionError as e:
        out['error'] = f"ZeroDivisionError: {e}"
    except Exception as e:
        out['error'] = f"{type(e).__name__}: {e}"
    return out

def exp8_q3_exception_hierarchy_demo(obj) -> str:
    """
    Demonstrates raising appropriate exception types and catching base Exception.
    """
    try:
        if obj is None:
            raise ValueError("Received None")
        if isinstance(obj, (int, float)) and obj < 0:
            raise ArithmeticError("Negative number not allowed here")
        return "OK"
    except ArithmeticError as ae:
        return f"ArithmeticError: {ae}"
    except ValueError as ve:
        return f"ValueError: {ve}"
    except Exception as e:
        return f"Other Exception: {e}"

def exp8_q4_raise_manual(x: int) -> int:
    """Raise exception manually if x not in expected range."""
    if not (0 <= x <= 100):
        raise ValueError("x must be between 0 and 100")
    return x

def exp8_q5_assert_demo(x: int) -> str:
    """Demonstrate assert usage."""
    try:
        assert x >= 0, "x must be non-negative"
        return f"x is valid: {x}"
    except AssertionError as e:
        return f"AssertionError: {e}"

# -------------------------
# Experiment 9: pandas & plotting & data work (representative functions)
# Note: This file doesn't import heavy libs like pandas/matplotlib unless requested.
# We'll provide simple functions that show the intended operations without plotting.
# If you want real plots or dataframe operations, I can add them (pandas/matplotlib).
# -------------------------

def exp9_q1_create_list_from_temps(temps: List[float]) -> List[float]:
    """Example for plotting: return list ready to plot (identity)."""
    return temps

def exp9_q2_linspace_sin(n: int = 100) -> Tuple[List[float], List[float]]:
    """Create x (linspace) and y = sin(x) arrays without numpy: simple approx."""
    # create n points in [0, 2*pi]
    xs = [2*math.pi*i/(n-1) for i in range(n)]
    ys = [math.sin(x) for x in xs]
    return xs, ys

def exp9_q3_scatter_data(x_values: List[float], y_values: List[float]) -> List[Tuple[float, float]]:
    """Return paired data for scatter plotting."""
    return list(zip(x_values, y_values))

def exp9_q4_create_age_bins(ages: List[int], bins: List[int]) -> dict:
    """
    Return counts in bins. bins is a list of bin edges, e.g. [0,18,30,45,60,100]
    """
    counts = {f"{bins[i]}-{bins[i+1]-1}": 0 for i in range(len(bins)-1)}
    for a in ages:
        for i in range(len(bins)-1):
            if bins[i] <= a < bins[i+1]:
                counts[f"{bins[i]}-{bins[i+1]-1}"] += 1
                break
    return counts

def exp9_q5_groupby_count(items: Iterable[str]) -> dict:
    """Count occurrences (like groupby/ value_counts)."""
    d = {}
    for item in items:
        d[item] = d.get(item, 0) + 1
    return d

def exp9_q6_loc_iloc_demo(data: List[dict], idx: int) -> dict:
    """
    Demonstrate simple indexing of list-of-dicts like DataFrame loc/iloc:
    - iloc analog: index by integer position.
    """
    if idx < 0 or idx >= len(data):
        raise IndexError("index out of range")
    return data[idx]

def exp9_q7_merge_two_lists_as_rows(list1: List, list2: List) -> List[Tuple]:
    """Return merged rows (zip) similar to merging two dataframes side-by-side"""
    return list(zip(list1, list2))

def exp9_q8_apply_example(seq: Iterable, func) -> List:
    """Apply func to each element (like pandas apply)"""
    return [func(x) for x in seq]

def exp9_q9_split_fullname(fullname: str) -> Tuple[str, str]:
    """Split full name into first and last (simple)"""
    parts = fullname.strip().split()
    if len(parts) == 0:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], " ".join(parts[1:])

def exp9_q10_plotting_placeholder():
    """Placeholder: plotting requires matplotlib; user can ask to enable plots."""
    return "Plotting requires matplotlib; ask if you want plotting added."

# -------------------------
# Utilities / Demo main
# -------------------------

def main():
    # Demo calls (small set). Uncomment or adjust as needed.
    print("Demo outputs (Experiment 6 samples):")
    print("Area circle (r=3):", exp6_q1_area_circle_math(3))
    print("Sqrt(16):", exp6_q2_sqrt(16))
    print("Factorial(5):", exp6_q3_factorial(5))
    print("Random ints (3):", exp6_q5_random_numbers(3, 1, 10))
    print("Current time:", exp6_q6_print_time())
    print("GCD(54,24):", exp6_q10_gcd(54, 24))
    print("Arithmetic ops 10 and 3:", exp6_q14_arithmetic_ops(10, 3))
    print()
    print("Experiment 8 exception demos:")
    print("Divide 10/0:", exp8_q1_basic_exception_handling(10, 0))
    print("Raise manual (x=200):", end=" ")
    try:
        print(exp8_q4_raise_manual(200))
    except Exception as e:
        print(repr(e))
    print()
    print("Experiment 9 small demos:")
    xs, ys = exp9_q2_linspace_sin(10)
    print("sin sample:", ys[:5])

if __name__ == "__main__":
    main()

