# JVPM - The Java Virtual (Python) Machine

This repo contains a Java Virtual Machine emulator written in Python 3 (JVPM).
It was a group project for MSU Denver's "Software Development Methods 
and Tools" course in Fall 2019.

The emulator is executed via the `run_jvpm` script in the root directory, 
and takes a compiled Java class file as a command line argument.
(Note that by default, MacOS users must specify `$ python3`)

    $ python run_jvpm <filename>

The following Python packages were used to monitor code quality & maintainability,
formatting, and test coverage:
- [`unittest`](https://docs.python.org/3/library/unittest.html) (Unit testing; included in default Python installation)
- [`coverage`](https://pypi.org/project/coverage/) (Unit test code coverage)
- [`pylint`](https://pypi.org/project/pylint/) (Code linting)
- [`radon`](https://pypi.org/project/radon/) (Static analysis)



You can run any of these packages from the project root directory.
The following are our most recent results.

###### Coverage
    $ coverage run -m unittest
    
    ----------------------------------------------------------------------
    Ran 103 tests in 0.040s

    OK

    $ coverage report
    Name                                  Stmts   Miss  Cover
    ---------------------------------------------------------
    jvpm\__init__.py                          0      0   100%
    jvpm\class_file.py                      100      3    97%
    jvpm\jvm_stack.py                        24      0   100%
    jvpm\method_table.py                     23      2    91%
    jvpm\op_codes.py                        348      4    99%
    jvpm\test\__init__.py                     0      0   100%
    jvpm\test\test_class_file.py             22      0   100%
    jvpm\test\test_long_double_stack.py      16      0   100%
    jvpm\test\test_method_table.py           18      0   100%
    jvpm\test\test_op_codes.py              625      0   100%
    jvpm\test\test_run_jvpm.py               19      0   100%
    jvpm\test\test_stack_empty.py             7      0   100%
    run_jvpm.py                              19      1    95%
    ---------------------------------------------------------
    TOTAL                                  1221     10    99%

###### Linting
    $ pylint jvpm
    
    ************* Module jvpm.op_codes
    \op_codes.py:123:8: W0201: Attribute 'byte_count' defined outside __init__ (attribute-defined-outside-init)
    \op_codes.py:206:14: W0613: Unused argument 'index' (unused-argument)
    ********* Module jvpm.test.test_class_file
    \test\test_class_file.py:68:8: W0622: Redefining built-in 'bytes' (redefined-builtin)

    --------------------------------------------------------------
     code has been rated at 9.98/10 (previous run: 9.98/10, +0.00)

###### Raw metrics
    $ python -m radon raw --summary jvpm

    jvpm\class_file.py
    LOC: 265
    LLOC: 119
    SLOC: 203
    ** Total **
        LOC: 2302
        LLOC: 1475
        SLOC: 1504
        Comments: 60
        Single comments: 287
        Multi: 68
        Blank: 443
        - Comment Stats
            (C % L): 3%
            (C % S): 4%
            (C + M % L): 6%
