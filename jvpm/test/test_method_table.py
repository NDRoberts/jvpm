"""Test method emulation functions in the Method Table."""
# Disables pylint "unused wildcard import" error
# pylint: disable=W0614

import unittest
from unittest.mock import patch
from jvpm.method_table import println, next_int
from run_jvpm import Jvpm


class TestMethods(unittest.TestCase):
    """Battery of tests for methods found in MethodTable."""

    def setUp(self):
        self.tdd_object = Jvpm("jvpm/Java/Test.class")

    def test_println(self):
        """Test the println method which prints the top
        item from the stack.
        """
        self.tdd_object.stack.push_op(10)
        self.assertEqual(println(self.tdd_object), 10)

    def test_next_int(self):
        """ Test the next_int method. """
        self.tdd_object.stack.push_op(0)
        with patch("builtins.input", side_effect=["10"]):
            next_int(self.tdd_object)
        self.assertEqual(self.tdd_object.stack.pop_op(), 10)

    def test_init(self):
        """Will test the init method which takes the top two elements
        off the stack, then pushes a scanner object onto it.
        """
        self.tdd_object.stack.push_op(1)
        self.tdd_object.stack.push_op(1)
        # init(self.test)

    # def test_close(self):
    #    self.tdd_object.stack.push_op('File')
    #    self.assertEqual(self.tdd_object.stack.peek(), 'File')
    #    close = {
    #        "class_name": 'Object',
    #        "method_name": 'close',
    #        "method_descriptor": '][',
    #    }
    #    self.tdd_object.nmt.call(close)
    #    self.assertIsNone(self.tdd_object.stack.peek())
