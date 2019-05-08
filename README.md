# JVPM

This repo contains a Java Virtual Machine written in Python 3 (JVPM). To run the
program, enter the following command in the terminal, followed by the file name:
MAC:
$ python3 run_jvpm.py <file_name> 

PC:
py run_jvpm <filename> 

Unit tests for Test-Driven Development are also included. To run the tests,
enter the following command in the terminal:
MAC:
$ python3 -m unittest

PC:
py -m unittest

Code coverage tools have been employed to make sure as much of the program as 
possible is covered with tests. To generate the test code coverage, install 
coverage with the following command:
MAC:
pip3 install coverage

PC:
pip install coverage

Then run Coverage with the command:
MAC/PC:
$ coverage run -m unittest

----------------------------------------------------------------------
Ran 103 tests in 0.040s

OK

To view the results, enter the following command:
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

Linting has been acomplished via PyLint, and can be run by installing:

MAC:
pip3 install pylint

PC:
pip install pylint

and then run with the following command:

$ pylint jvpm
************* Module jvpm.op_codes
jvpm\op_codes.py:123:8: W0201: Attribute 'byte_count' defined outside __init__ (attribute-defined-outside-init)
jvpm\op_codes.py:206:14: W0613: Unused argument 'index' (unused-argument)
************* Module jvpm.test.test_class_file
jvpm\test\test_class_file.py:68:8: W0622: Redefining built-in 'bytes' (redefined-builtin)

------------------------------------------------------------------
Your code has been rated at 9.98/10 (previous run: 9.98/10, +0.00)