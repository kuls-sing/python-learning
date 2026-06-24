# Python Learning Progress Summary
**Learner:** Kulwant Singh  
**Goal:** Automation/QA Python Developer → Data Science transition  
**Started:** Early 2026 | **Last Updated:** 2026-06-24

---

## Career Roadmap

| Phase | Goal | Timeline |
|---|---|---|
| Phase 1 | Core Python (complete) | Done |
| Phase 2 | Automation/QA specialization | ~4-5 months from start |
| Phase 3 | Data Science transition | ~10-18 months from start |

---

## Topics Completed

### Basics
| # | Topic | Key Concepts |
|---|---|---|
| 1 | Environment Setup | Python 3.10.12, VS Code, WSL Ubuntu |
| 2 | Hello World | `print()`, strings, running `.py` files |
| 3 | Variables | string, int, assignment operator |
| 4 | Data Types | str, int, float, bool, `type()`, type conversion |
| 5 | String Operations | concatenation, `len()`, `.upper()`, `.lower()`, `.replace()`, f-strings, `strip()` |
| 6 | User Input | `input()`, type conversion from string |
| 7 | Conditions | `if/else`, `elif`, comparison operators |
| 8 | Loops | `for`, `range()`, `while`, `continue` |
| 9 | Lists | indexing, `append()`, `remove()`, slicing |
| 10 | Functions | `def`, parameters, `return`, default parameters |
| 11 | Dictionaries | key-value pairs, `.items()`, dictionary of lists |
| 12 | File I/O | `"w"/"r"/"a"` modes, `with open()`, `enumerate()` |
| 13 | Modules | `import`, `random`, `os` module |

### Intermediate
| # | Topic | Key Concepts |
|---|---|---|
| 14 | Project — Contact Book | add/view/search, save to file, load on startup |
| 15 | Error Handling | `try/except`, `ValueError`, `IndexError`, `KeyboardInterrupt` |
| 16 | OOP | `class`, `__init__`, `self`, `__str__`, mutable default arg trap |
| 17 | Inheritance | `class Dog(Animal)`, method overriding, `super().__init__()` |
| 18 | Encapsulation | private attributes `__attr`, getters/setters |
| 19 | Comprehensive Quiz | Scored 17/20 |

### Advanced (In Progress)
| # | Topic | Key Concepts |
|---|---|---|
| 20 | List Comprehensions | `[expr for item in iterable if condition]` |
| 21 | Lambda Functions | `lambda params: expression`, default params, implicit return |
| 22 | `map()` | returns map object, convert with `list()`, use with lambda |

---

## Files Created
```
~/python_learning/
├── hello.py
├── variables.py
├── datatypes.py
├── strings.py
├── user_input.py
├── conditions.py
├── loops.py
├── lists.py
├── functions.py
├── dictionaries.py
├── file_io.py
├── modules.py
├── contact_book.py
├── bank_account.py
├── bank_account_1.py
├── student.py
├── oop.py
├── inheritance.py
├── inheritance_1.py
├── list_comprehension.py
└── lambda.py
```

---

## 2-Week Sprint Plan (Started 2026-06-24, 6 hrs/day)

| Day | Topic | Status |
|---|---|---|
| Day 1 | List comprehensions + Lambda + map() | Done |
| Day 2 | Git & GitHub | In Progress |
| Day 3 | pytest basics | Pending |
| Day 4 | pytest intermediate + fixtures | Pending |
| Day 5 | requests library + APIs | Pending |
| Day 6-7 | Selenium basics | Pending |
| Day 8 | Selenium intermediate | Pending |
| Day 9 | SQL basics | Pending |
| Day 10-11 | Project 1 — Automation test suite | Pending |
| Day 12-13 | Project 2 — API test framework | Pending |
| Day 14 | Interview prep — Python QA questions | Pending |

---

## Key Things to Remember
- `strip()` removes ALL whitespace from both ends, not just `\n`
- `random.randint(a, b)` is **inclusive** on both ends
- Never use mutable defaults in functions: use `None` instead of `grades=[]`
- Lambda is for one-liners only — use `def` for complex logic
- `map()` returns a map object — always wrap with `list()`
- Clean variable names matter in interviews (spelling counts!)
