# JVPM

This repo contains a Java Virtual Machine written in Python 3 (JVPM). To run the
program, enter the following command in the terminal:
MAC:
$ python3 

PC:
py 

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

............................................................................................................
----------------------------------------------------------------------
Ran 108 tests in 0.074s

OK

To view the results, enter the following command:
$ coverage report