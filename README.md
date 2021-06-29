#   TDD unittest

## Objectives:
the participants will learn:
- unittest use
- rise error
- assert types:
    - assertTrue
    - assertFalse
    - assertEqual
    - assertRises
## run test command:
   python3 test.py
run test with more details
   python3 -m unittest -v test.py

## Tasks:
### task1:
why tests 2,3 and 4 will fail and how to fix them so they will pass?

## assert types:
- assertEqual(a, b)          a == b
- assertNotEqual(a, b)       a != b
- assertTrue(x)              bool(x) is True
- assertFalse(x)             bool(x) is False
- assertIs(a, b)             a is b
- assertIsNot(a, b)          a is not b
- assertIsNone(x)            x is None
- assertIsNotNone(x)         x is not None
- assertIn(a, b)             a in b
- assertNotIn(a, b)          a not in b
- assertIsInstance(a, b)     isinstance(a, b)
- assertNotIsInstance(a, b)  not isinstance(a, b)
## for more details [unittest documentation](https://docs.python.org/3/library/unittest.html).


