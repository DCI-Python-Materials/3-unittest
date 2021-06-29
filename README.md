#   TDD unittest

## Objectives:
the participants will learn:
- unittest use
- rise error
- test custom message
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
### task2: 
write a function named get_first_letter_list which will take string parameter and return a list of first letter of each word on the parameter 
this sentence as an example "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
### task3:
write a test function for the previous task which will check the following:
- function should rise TypeError in case the parameter is empty or not a string
- the result of the function should be correct

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


