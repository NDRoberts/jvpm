"""this is a test for Scanner"""
# Disables pylint error W0611, unused mock patch import
# pylint: disable=W0611
import unittest
from unittest.mock import patch
from jvpm.op_codes import OpCodes
from jvpm.method_table import *
from run_jvpm import Jvpm

class TestScanner(unittest.TestCase):
    """ Class to test the scanner methods and method_table.py"""
    test = Jvpm('jvpm/Java/Test.class')
    # def test_scanner(self):
    #     """method to test the scanner"""
    #     stack = OpCodes()
    #     stack.stack.push_op(0)
    #     stack.stack.push_op(0)
    #     scanner(stack)
    #     self.assertEqual(stack.stack.pop_op(), 'scanner')

    # def test_next_int(self):
    #     """method to test the scanner"""
    #     stack = OpCodes()
    #     stack.stack.push_op(0)
    #     with patch("builtins.input", side_effect=["10"]):
    #         next_int(stack)
    #     self.assertEqual(stack.stack.pop_op(), 10)

    def test_println(self):
        """ Test the println method which prints the top
        item from the stack.
        """
        self.test.stack.push_op(10)
        self.assertEqual(println(self.test), 10)

    def test_next_int(self):
        """ Test the next_int method. """
        self.test.stack.push_op(0)
        with patch("builtins.input", side_effect=["10"]):
            next_int(self.test)
        self.assertEqual(self.test.stack.pop_op(), 10)
