"""this is a test for op_codes"""
import unittest
from unittest.mock import patch, call
import numpy
from jvpm.op_codes import iadd, isub
from jvpm.op_codes import imul
from jvpm.op_codes import idiv, irem
from jvpm.op_codes import OpCodes
numpy.warnings.filterwarnings("ignore")


class TestOpCodes(unittest.TestCase):
    """this class tests the op_codes class"""
    @patch('builtins.print')
    def test_op_codes(self, mock_patch):
        """this method performs the op code test"""
        op_code = OpCodes()
        op_code.parse_codes(0)
        self.assertEqual(mock_patch.mock_calls,
                         [call('istore_1'),
                          call('iconst_1'),
                          call('iconst_1'),
                          call('iconst_1'),
                          call('iconst_1'),
                          call('iconst_1'),
                          call('aload_0'),
                          call('invokespecial'),
                          call('return'),
                          call('iconst_1'),
                          call('istore_1'),
                          call('iinc'),
                          call('return')])

    def test_not_implmented(self):
        """this method tests the OpCodes class"""
        self.assertEqual(OpCodes().interpret(0), 'not implemented')

    def test_mph1(self):
        """a"""
        self.assertEqual(1 + 1, 2)
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)

    def test_add_subtract(self):
        """tests the iadd and isub opcodes"""
        op_code = OpCodes()
        op_code.stack.push_op(numpy.int32(2000000000))
        op_code.stack.push_op(numpy.int32(1000000000))

        iadd(op_code)
        self.assertEqual(op_code.stack.peek(), -1294967296)
        self.assertEqual(op_code.byte_count, 1)
        op_code.stack.push_op(numpy.int32(10))
        op_code.stack.push_op(numpy.int32(3))
        isub(op_code)
        self.assertEqual(op_code.stack.peek(), 7)
        self.assertEqual(op_code.byte_count, 2)
    def test_multiply(self):
        """tests the imul opcode"""
        op_code = OpCodes()
        op_code.stack.push_op(numpy.int32(2000000000))
        op_code.stack.push_op(numpy.int32(1000000000))

        imul(op_code)
        self.assertEqual(op_code.stack.peek(), 1321730048)
        self.assertEqual(op_code.byte_count, 1)
    def test_divide(self):
        """tests the idiv opcode"""
        op_code = OpCodes()
        op_code.stack.push_op(numpy.int32(128))
        op_code.stack.push_op(numpy.int32(-3))

        idiv(op_code)
        self.assertEqual(op_code.stack.peek(), -42)
        self.assertEqual(op_code.byte_count, 1)
    def test_mod(self):
        """tests the irem opcode"""
        op_code = OpCodes()
        op_code.stack.push_op(numpy.int32(128))
        op_code.stack.push_op(numpy.int32(-3))

        irem(op_code)
        self.assertEqual(op_code.stack.peek(), 2)
        self.assertEqual(op_code.byte_count, 1)

def test_iand(self):
    # Test the iand opcode using 240 (1111 0000) and 15 (0000 1111)
    # Expected result: 0 (0000 0000)
    ops = OpCodes()
    ops.stack.push_op(240)
    ops.stack.push_op(15)
    iand(ops)
    self.assertEqual(ops.stack.peek(), 0)
    self.assertEqual(ops.byte_count, 1)

def test_ineg(self):
    # Test the ineg opcode using 14 (1110)
    # Expected result: 1 (0001)
    ops = OpCodes()
    ops.stack.push_op(240)
    ineg(ops)
    self.assertEqual((ops.stack.peek(), 14)
    self.assertEqual(ops.byte_count, 1)

def test_ior(self):\
    # Test the ior opcode using 240 (1111 0000) and 15 (0000 1111)
    # Expected result: 255 (1111 1111)
    ops = OpCodes()
    ops.stack.push_op(240)
    ops.stack.push_op(15)
    ior(ops)
    self.assertEqual(ops.stack.peek(), 255)
    self.assertEqual(ops.byte_count, 1)

def test_ixor(self):
    # Test the ixor opcode using 255 (1111 1111) and 81 (1000 0001)
    # Expected result: 126 (0111 1110)
    ops = OpCodes()
    ops.stack.push_op(255)
    ops.stack.push_op(81)
    ixor(ops)
    self.assertEqual(ops.stack.peek(), 126)
    self.assertEqual(ops.byte_count, 1)
