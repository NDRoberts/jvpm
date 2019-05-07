"""this is a test for op_codes"""
# utilizes NumPy package to handle 32 bit int over/underflow in Java
import unittest
from unittest.mock import patch, call
import numpy
from jvpm.op_codes import *
from jvpm.jvm_stack import *
from jvpm.run_jvpm import *

numpy.warnings.filterwarnings("ignore")


class TestOpCodes(unittest.TestCase):
    test = Jvpm()

    """this class tests the op_codes class"""
    # @patch('builtins.print')
    # def test_op_codes(self, mock_patch):
    #     """this method performs the op code test"""
    #     op_code = OpCodes()
    #     op_code.parse_codes(143)

    def test_aload(self):
        """tests the aload opcode method"""
        
        length = len(self.test.stack.local_array)
        for i in range(0, length):
            aload(self.test, i)
            self.assertEqual(self.test.stack.peek(), self.test.stack.local_array[i])

    # def test_not_implmented(self):
    #     """this method tests the OpCodes class"""
    #     self.assertEqual(OpCodes().interpret(0), 'not implemented')

    def test_iconst_m1(self):
        """tests iconst_m1 method, expected value -1"""
        iconst_m1(self.test)
        self.assertEqual(self.test.stack.peek(), -1)

    def test_iconst_0(self):
        """tests iconst_0 method, expected value 0"""
        iconst_0(self.test)
        self.assertEqual(self.test.stack.peek(), 0)

    def test_iconst_1(self):
        """tests iconst_1 method, expected value 1"""        
        iconst_1(self.test)
        self.assertEqual(self.test.stack.peek(), 1)

    def test_iconst_2(self):
        """tests iconst_2 method, expected value 2"""        
        iconst_2(self.test)
        self.assertEqual(self.test.stack.peek(), 2)

    def test_iconst_3(self):
        """tests iconst_3 method, expected value 3"""        
        iconst_3(self.test)
        self.assertEqual(self.test.stack.peek(), 3)

    def test_iconst_4(self):
        """tests iconst_4 method, expected value 4"""        
        iconst_4(self.test)
        self.assertEqual(self.test.stack.peek(), 4)

    def test_iconst_5(self):
        """tests iconst_5 method, expected value 5"""        
        iconst_5(self.test)
        self.assertEqual(self.test.stack.peek(), 5)

    def test_iinc(self):
        """tests iinc method"""        
        length = len(self.test.stack.local_array)
        for i in range(0, length):
            iinc(self.test, i, i)
            self.test.stack.local_array[i] = i
            self.assertEqual(self.test.stack.local_array[i], i)

    def test_istore(self):
        """tests istore method"""        
        length = len(self.test.stack.local_array)
        self.test.stack.push_op(3)
        self.test.stack.push_op(2)
        self.test.stack.push_op(1)
        self.test.stack.push_op(0)
        for i in range(0, length):
            istore(self.test, i)
            self.assertEqual(self.test.stack.local_array[i], i)

    def test_istore_0(self):
        """tests istore_0 method"""
        self.test.stack.push_op(0)
        istore_0(self.test)
        self.assertEqual(self.test.stack.local_array[0], 0)

    def test_istore_1(self):
        """tests istore_1 method"""
        self.test.stack.push_op(1)
        istore_1(self.test)
        self.assertEqual(self.test.stack.local_array[1], 1)

    def test_istore_2(self):
        """test istore_2 method"""
        self.test.stack.push_op(2)
        istore_2(self.test)
        self.assertEqual(self.test.stack.local_array[2], 2)

    def test_istore_3(self):
        """tests istore_3 method"""
        
        self.test.stack.push_op(3)
        istore_3(self.test)
        self.assertEqual(self.test.stack.local_array[3], 3)

    def test_lstore(self):
        """tests the lstore method for 64 bit longs"""
        
        length = len(self.test.stack.local_array)
        self.test.stack.push_op(numpy.int64(3), push_twice)
        self.test.stack.push_op(numpy.int64(2), push_twice)
        self.test.stack.push_op(numpy.int64(1), push_twice)
        self.test.stack.push_op(numpy.int64(0), push_twice)
        for i in range(0, length):
            lstore(self.test, i)
            self.assertEqual(self.test.stack.local_array[i], numpy.int64(i))

    def test_fstore(self):
        """tests the fstore method for 32 bit floats"""
        
        length = len(self.test.stack.local_array)
        self.test.stack.push_op(numpy.float32(3), push_twice)
        self.test.stack.push_op(numpy.float32(2), push_twice)
        self.test.stack.push_op(numpy.float32(1), push_twice)
        self.test.stack.push_op(numpy.float32(0), push_twice)
        for i in range(0, length):
            fstore(self.test, i)
            self.assertEqual(self.test.stack.local_array[i], numpy.float32(i))

    def test_lstore_0(self):
        """tests the lstore_0 opcode for 64 bit longs"""
        
        self.test.stack.push_op(numpy.int64(0), push_twice)
        lstore_0(self.test)
        self.assertEqual(self.test.stack.local_array[0], 0)

    def test_lstore_1(self):
        """tests the lstore_1 opcode for 64 bit longs"""
        
        self.test.stack.push_op(numpy.int64(1), push_twice)
        lstore_1(self.test)
        self.assertEqual(self.test.stack.local_array[1], 1)

    def test_lstore_2(self):
        """tests the lstore_2 opcode for 64 bit longs"""
        
        self.test.stack.push_op(numpy.int64(2), push_twice)
        lstore_2(self.test)
        self.assertEqual(self.test.stack.local_array[2], 2)

    def test_lstore_3(self):
        """tests the lstore_3 opcode for 64 bit longs"""
        
        self.test.stack.push_op(numpy.int64(3), push_twice)
        lstore_3(self.test)
        self.assertEqual(self.test.stack.local_array[3], 3)

    def test_fstore_0(self):
        """tests the fstore_0 opcode for 32 bit floats"""
        
        self.test.stack.push_op(numpy.int64(0), push_twice)
        fstore_0(self.test)
        self.assertEqual(self.test.stack.local_array[0], 0)

    def test_fstore_1(self):
        """tests the lstore_1 opcode for 32 bit floats"""
        
        self.test.stack.push_op(numpy.float32(1), push_twice)
        fstore_1(self.test)
        self.assertEqual(self.test.stack.local_array[1], 1)

    def test_fstore_2(self):
        """tests the fstore_2 opcode for 32 bit floats"""
        
        self.test.stack.push_op(numpy.float32(2), push_twice)
        fstore_2(self.test)
        self.assertEqual(self.test.stack.local_array[2], 2)

    def test_fstore_3(self):
        """tests the fstore_3 opcode for 32 bit floats"""
        
        self.test.stack.push_op(numpy.float32(3), push_twice)
        fstore_3(self.test)
        self.assertEqual(self.test.stack.local_array[3], 3)

    def test_iload(self):
        """tests iload method"""
        
        #tests every load index from 0 to length
        length = len(self.test.stack.local_array)
        for i in range(0, length):
            iload(self.test, i)
            self.assertEqual(self.test.stack.peek(), self.test.stack.local_array[i])

    def test_iload_0(self):
        """tests iload_0 opcode"""
        
        iload_0(self.test)
        self.assertEqual(self.test.stack.peek(), self.test.stack.local_array[0])

    def test_iload_1(self):
        """tests iload_1 opcode"""
        
        iload_1(self.test)
        self.assertEqual(self.test.stack.peek(), self.test.stack.local_array[1])

    def test_iload_2(self):
        """tests iload_2 opcode"""
        
        iload_2(self.test)
        self.assertEqual(self.test.stack.peek(), self.test.stack.local_array[2])

    def test_iload_3(self):
        """tests iload_3 opcode"""
        
        iload_3(self.test)
        self.assertEqual(self.test.stack.peek(), self.test.stack.local_array[3])

    # def test_mph1(self):
    #     """tests mph1 method"""
    #     self.assertEqual(1 + 1, 2)
    #     with self.assertRaises(KeyError):
    #         OpCodes().interpret(1)

    # def test_new(self):
    #     """tests new method"""        
    #     new(test)

    def test_add_subtract(self):
        """tests the iadd and isub opcodes"""
        self.test.stack.push_op(numpy.int32(2000000000))
        self.test.stack.push_op(numpy.int32(1000000000))
        iadd(self.test)
        self.assertEqual(self.test.stack.peek(), -1294967296)
        self.test.stack.push_op(numpy.int32(10))
        self.test.stack.push_op(numpy.int32(3))
        isub(self.test)
        self.assertEqual(self.test.stack.peek(), 7)

    def test_multiply(self):
        """tests the imul opcode"""
        self.test.stack.push_op(numpy.int32(2000000000))
        self.test.stack.push_op(numpy.int32(1000000000))
        imul(self.test)
        self.assertEqual(self.test.stack.peek(), 1321730048)

    def test_divide(self):
        """tests the idiv opcode"""
        self.test.stack.push_op(numpy.int32(128))
        self.test.stack.push_op(numpy.int32(-3))
        idiv(self.test)
        self.assertEqual(self.test.stack.peek(), -42)

    def test_mod(self):
        """tests the irem opcode"""
        self.test.stack.push_op(numpy.int32(128))
        self.test.stack.push_op(numpy.int32(-3))
        irem(self.test)
        self.assertEqual(self.test.stack.peek(), 2)

    def test_iand(self):
        """ Test the iand (Integer And) opcode """
        # iand (240 & 15) should produce (0)
        self.test.stack.push_op(240)
        self.test.stack.push_op(15)
        iand(self.test)
        self.assertEqual(self.test.stack.pop_op(), 0)
        # iand (43,690 & 50,790) should produce (33314)
        self.test.stack.push_op(43690)
        self.test.stack.push_op(50790)
        iand(self.test)
        self.assertEqual(self.test.stack.pop_op(), 33314)
        # iand (-2,147,483,647 & -1) should produce (-2,147,483,647)
        self.test.stack.push_op(-2147483647)
        self.test.stack.push_op(-1)
        iand(self.test)
        self.assertEqual(self.test.stack.pop_op(), -2147483647)

    def test_ineg(self):
        """ Test the ineg (Integer Negate) opcode """
        # ineg(254) should produce (-255)
        self.test.stack.push_op(254)
        ineg(self.test)
        self.assertEqual(self.test.stack.pop_op(), -255)
        # ineg(0) should produce (-1)
        self.test.stack.push_op(0)
        ineg(self.test)
        self.assertEqual(self.test.stack.pop_op(), -1)
        # ineg(2,147,483,647) sould produce (-2,147,483,648)
        self.test.stack.push_op(2147483647)
        ineg(self.test)
        self.assertEqual(self.test.stack.pop_op(), -2147483648)

    def test_ior(self):
        """ Test the ior (Integer Or) opcode """
        # ior(240 | 15) should produce (255)
        self.test.stack.push_op(240)
        self.test.stack.push_op(15)
        ior(self.test)
        self.assertEqual(self.test.stack.pop_op(), 255)
        # ior(2,147,483,647 | -2,147,483,648) should produce (-1)
        self.test.stack.push_op(2147483647)
        self.test.stack.push_op(-2147483648)
        ior(self.test)
        self.assertEqual(self.test.stack.pop_op(), -1)

    def test_ixor(self):
        """ Test the ixor (Integer Exclusive Or) opcode """
        # ixor(255 ^ 129) should produce (126)
        self.test.stack.push_op(255)
        self.test.stack.push_op(129)
        ixor(self.test)
        self.assertEqual(self.test.stack.peek(), 126)

    def test_ishl(self):
        """ Test the ishl (Integer Shift Left) opcode """
        self.test.stack.push_op(0)
        self.test.stack.push_op(0)
        ishl(self.test)
        self.assertEqual(self.test.stack.pop_op(), 0)

        self.test.stack.push_op(1)
        self.test.stack.push_op(1)
        ishl(self.test)
        self.assertEqual(self.test.stack.pop_op(), 2)

        self.test.stack.push_op(1)
        self.test.stack.push_op(3)
        ishl(self.test)
        self.assertEqual(self.test.stack.pop_op(), 8)

        self.test.stack.push_op(1)
        self.test.stack.push_op(8)
        ishl(self.test)
        self.assertEqual(self.test.stack.pop_op(), 256)

        self.test.stack.push_op(8)
        self.test.stack.push_op(4)
        ishl(self.test)
        self.assertEqual(self.test.stack.pop_op(), 128)

        self.test.stack.push_op(16)
        self.test.stack.push_op(2)
        ishl(self.test)
        self.assertEqual(self.test.stack.pop_op(), 64)

    def test_ishr(self):
        """ Test the ishr (Integer Arithmetic Shift Right) opcode """
        self.test.stack.push_op(0)
        self.test.stack.push_op(0)
        ishr(self.test)
        self.assertEqual(self.test.stack.pop_op(), 0)

        self.test.stack.push_op(8)
        self.test.stack.push_op(3)
        ishr(self.test)
        self.assertEqual(self.test.stack.pop_op(), 1)

        self.test.stack.push_op(256)
        self.test.stack.push_op(6)
        ishr(self.test)
        self.assertEqual(self.test.stack.pop_op(), 4)
        self.test.stack.push_op(16)
        self.test.stack.push_op(3)
        ishr(self.test)
        self.assertEqual(self.test.stack.pop_op(), 2)

        self.test.stack.push_op(32)
        self.test.stack.push_op(2)
        ishr(self.test)
        self.assertEqual(self.test.stack.pop_op(), 8)

        self.test.stack.push_op(16)
        self.test.stack.push_op(2)
        ishr(self.test)
        self.assertEqual(self.test.stack.pop_op(), 4)

    def test_iushr(self):
        """ Test the iushr (Logical Shift Right) opcode """
        # iushr(255 >>> 2) should produce (63)
        self.test.stack.push_op(255)
        self.test.stack.push_op(2)
        iushr(self.test)
        self.assertEqual(self.test.stack.pop_op(), 63)
        # iushr(-1 >> 4) should produce (268,435,455)
        self.test.stack.push_op(-1)
        self.test.stack.push_op(4)
        iushr(self.test)
        self.assertEqual(self.test.stack.pop_op(), 268435455)

    def test_i2b(self):
        """Test conversion of integer to byte dawg"""
        self.test.stack.push_op(42)
        i2b(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int8)

    def test_i2c(self):
        """Test conversion of integer to byte"""
        self.test.stack.push_op(33)
        i2c(self.test)
        assert isinstance(self.test.stack.peek(), str)

    def test_i2d(self):
        """Test conversion of integer to double"""
        self.test.stack.push_op(42)
        i2d(self.test)
        assert isinstance(self.test.stack.peek(), numpy.float64)

    def test_i2f(self):
        """Test conversion of integer to float"""
        self.test.stack.push_op(42)
        i2f(self.test)
        assert isinstance(self.test.stack.peek(), numpy.float32)

    def test_i2l(self):
        """Test conversion of integer to long"""
        self.test.stack.push_op(42)
        i2l(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)

    def test_i2s(self):
        """Test conversion of integer to short"""
        self.test.stack.push_op(42)
        i2s(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int16)

    def test_dup(self):
        """Test dup"""
        self.test.stack.push_op(15)
        dup(self.test)
        self.assertEqual(self.test.stack.pop_op(), 15)
        self.assertEqual(self.test.stack.pop_op(), 15)

        self.test.stack.push_op(0)
        dup(self.test)
        self.assertEqual(self.test.stack.pop_op(), 0)
        self.assertEqual(self.test.stack.pop_op(), 0)

        self.test.stack.push_op('foo')
        dup(self.test)
        self.assertEqual(self.test.stack.pop_op(), 'foo')
        self.assertEqual(self.test.stack.pop_op(), 'foo')

    def test_lload(self):
        """tests lload method"""
        
        #tests every load index from 0 to length
        length = len(self.test.stack.local_array)
        for i in range(0, length):
            lload(self.test, i)
            self.assertEqual(self.test.stack.pop_op(pop_twice), self.test.stack.local_array[i])

    def test_lload_0(self):
        """tests iload_0 opcode"""
        
        lload_0(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), self.test.stack.local_array[0])

    def test_lload_1(self):
        """tests iload_1 opcode"""
        
        lload_1(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), self.test.stack.local_array[1])

    def test_lload_2(self):
        """tests iload_2 opcode"""
        
        lload_2(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), self.test.stack.local_array[2])

    def test_lload_3(self):
        """tests iload_3 opcode"""
        
        lload_3(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), self.test.stack.local_array[3])

    def test_lshl(self):
        """Test lshl (long shift left)"""
        self.test.stack.push_op(2, push_twice)
        self.test.stack.push_op(2)
        lshl(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(self.test.stack.pop_op(pop_twice), numpy.int64(8))

        self.test.stack.push_op(2, push_twice)
        self.test.stack.push_op(66)
        lshl(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(self.test.stack.pop_op(pop_twice), numpy.int64(8))

    def test_lshr(self):
        """Test lshr (long shift right)"""
        self.test.stack.push_op(42, push_twice)
        self.test.stack.push_op(3)
        lshr(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(self.test.stack.pop_op(pop_twice), numpy.int64(5))

        self.test.stack.push_op(2, push_twice)
        self.test.stack.push_op(66)
        lshr(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(self.test.stack.pop_op(pop_twice), numpy.int64(0))

        self.test.stack.push_op(-15, push_twice)
        self.test.stack.push_op(2)

        lshr(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(self.test.stack.pop_op(pop_twice), numpy.int64(-4))

    def test_land(self):
        """Test land (logical bitwise long AND)"""
        self.test.stack.push_op(42)
        i2l(self.test)
        self.test.stack.push_op(6)
        i2l(self.test)
        land(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(self.test.stack.pop_op(pop_twice), numpy.int64(2))

    def test_lcmp(self):
        """Test lcmp (compare 2 longs)"""
        self.test.stack.push_op(41)
        i2l(self.test)
        self.test.stack.push_op(42)
        i2l(self.test)
        lcmp(self.test)
        self.assertEqual(self.test.stack.pop_op(), -1)

        self.test.stack.push_op(43)
        i2l(self.test)
        self.test.stack.push_op(42)
        i2l(self.test)

        lcmp(self.test)
        self.assertEqual(self.test.stack.pop_op(), 1)

        self.test.stack.push_op(42)
        i2l(self.test)
        self.test.stack.push_op(42)
        i2l(self.test)
        lcmp(self.test)
        self.assertEqual(self.test.stack.pop_op(), 0)

    def test_lxor(self):
        """test lxor (long exclusive or)"""
        self.test.stack.push_op(7)
        i2l(self.test)
        self.test.stack.push_op(6)
        i2l(self.test)
        lxor(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(self.test.stack.pop_op(pop_twice), numpy.int64(1))

        self.test.stack.push_op(-7)
        i2l(self.test)
        self.test.stack.push_op(-6)
        i2l(self.test)
        lxor(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(self.test.stack.pop_op(pop_twice), numpy.int64(3))

        self.test.stack.push_op(-7)
        i2l(self.test)
        self.test.stack.push_op(6)
        i2l(self.test)
        lxor(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(self.test.stack.pop_op(pop_twice), numpy.int64(-1))

    def test_fcmpg(self):
        """Test fcmpg (compare 2 floats)"""
        self.test.stack.push_op(1/7)
        i2f(self.test)
        self.test.stack.push_op(1/3)
        i2f(self.test)
        fcmpg(self.test)
        self.assertEqual(self.test.stack.pop_op(), -1)

        self.test.stack.push_op(1/3)
        i2f(self.test)
        self.test.stack.push_op(1/7)
        i2f(self.test)
        fcmpg(self.test)
        self.assertEqual(self.test.stack.pop_op(), 1)

        self.test.stack.push_op(1/7)
        i2f(self.test)
        self.test.stack.push_op(1/7)
        i2f(self.test)
        fcmpg(self.test)
        self.assertEqual(self.test.stack.pop_op(), 0)

        self.test.stack.push_op(numpy.nan)
        self.test.stack.push_op(1/7)
        i2f(self.test)
        fcmpg(self.test)
        self.assertEqual(self.test.stack.pop_op(), 1)

        self.test.stack.push_op(1/7)
        self.test.stack.push_op(numpy.nan)
        i2f(self.test)
        fcmpg(self.test)
        self.assertEqual(self.test.stack.pop_op(), 1)

    def test_fcmpl(self):
        """Test fcmpl (compare 2 floats)"""
        self.test.stack.push_op(1/7)
        i2f(self.test)
        self.test.stack.push_op(1/3)
        i2f(self.test)
        fcmpl(self.test)
        self.assertEqual(self.test.stack.pop_op(), -1)

        self.test.stack.push_op(1/3)
        i2f(self.test)
        self.test.stack.push_op(1/7)
        i2f(self.test)
        fcmpl(self.test)
        self.assertEqual(self.test.stack.pop_op(), 1)

        self.test.stack.push_op(1/7)
        i2f(self.test)
        self.test.stack.push_op(1/7)
        i2f(self.test)
        fcmpl(self.test)
        self.assertEqual(self.test.stack.pop_op(), 0)

        self.test.stack.push_op(numpy.nan)
        self.test.stack.push_op(1/7)
        i2f(self.test)
        fcmpl(self.test)
        self.assertEqual(self.test.stack.pop_op(), -1)

        self.test.stack.push_op(1/7)
        self.test.stack.push_op(numpy.nan)
        i2f(self.test)
        fcmpl(self.test)
        self.assertEqual(self.test.stack.pop_op(), -1)

    def test_fneg(self):
        """test fneg (negate a float)"""
        self.test.stack.push_op(1/7)
        i2f(self.test)
        fneg(self.test)
        self.assertEqual(self.test.stack.pop_op(), numpy.float32(-1/7))

        self.test.stack.push_op(float("inf"))
        i2f(self.test)
        fneg(self.test)
        numpy.isneginf(self.test.stack.pop_op())

        self.test.stack.push_op(float("-inf"))
        i2f(self.test)
        fneg(self.test)
        numpy.isposinf(self.test.stack.pop_op())

        self.test.stack.push_op(0)
        i2f(self.test)
        fneg(self.test)
        numpy.negative(self.test.stack.pop_op())

        self.test.stack.push_op(numpy.nan)
        fneg(self.test)
        numpy.isnan(self.test.stack.pop_op())

    def test_fload(self):
        """tests fload method"""
        #tests every load index from 0 to length
        length = len(self.test.stack.local_array)
        for i in range(0, length):
            fload(self.test, i)
            self.assertEqual(self.test.stack.pop_op(), self.test.stack.local_array[i])

    def test_fload_0(self):
        """tests iload_0 opcode"""
        fload_0(self.test)
        self.assertEqual(self.test.stack.pop_op(), self.test.stack.local_array[0])

    def test_fload_1(self):
        """tests fload_1 opcode"""
        fload_1(self.test)
        self.assertEqual(self.test.stack.pop_op(), self.test.stack.local_array[1])

    def test_fload_2(self):
        """tests fload_2 opcode"""
        fload_2(self.test)
        self.assertEqual(self.test.stack.pop_op(), self.test.stack.local_array[2])

    def test_fload_3(self):
        """tests fload_3 opcode"""
        fload_3(self.test)
        self.assertEqual(self.test.stack.pop_op(), self.test.stack.local_array[3])

    def test_lconst_0(self):
        """test lconst_0 (pushes 0L to the stack)"""
        lconst_0(self.test)
        self.assertEqual(numpy.int64(0), self.test.stack.pop_op(pop_twice))

    def test_lconst_1(self):
        """test lconst_1 (pushes 1L to the stack)"""
        lconst_1(self.test)
        self.assertEqual(numpy.int64(1), self.test.stack.pop_op(pop_twice))

    def test_fconst_0(self):
        """test fconst_0 (pushes 0F to the stack)"""
        fconst_0(self.test)
        self.assertEqual(numpy.float32(0), self.test.stack.pop_op())

    def test_fconst_1(self):
        """test fconst_1 (pushes 1F to the stack)"""
        fconst_1(self.test)
        self.assertEqual(numpy.float32(1), self.test.stack.pop_op())

    def test_fconst_2(self):
        """test fconst_2 (pushes 2F to the stack)"""
        fconst_2(self.test)
        self.assertEqual(numpy.float32(2), self.test.stack.pop_op())

    def test_l2d(self):
        """test l2d (long to double)"""
        lconst_1(self.test)
        l2d(self.test)
        assert isinstance(self.test.stack.peek(), numpy.float64)
        self.assertEqual(numpy.float64(1), self.test.stack.pop_op(pop_twice))

    def test_l2f(self):
        """test l2d (long to float)"""
        lconst_1(self.test)
        l2f(self.test)
        assert isinstance(self.test.stack.peek(), numpy.float32)
        self.assertEqual(numpy.float32(1), self.test.stack.pop_op())

    def test_l2i(self):
        """test l2i (long to int)"""
        lconst_1(self.test)
        l2i(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int32)
        self.assertEqual(numpy.int(1), self.test.stack.pop_op())

    def test_f2d(self):
        """test f2d (float to double)"""
        fconst_1(self.test)
        f2d(self.test)
        assert isinstance(self.test.stack.peek(), numpy.float64)
        self.assertEqual(numpy.float64(1), self.test.stack.pop_op(pop_twice))

    def test_f2i(self):
        """test f2i (float to integer)"""
        fconst_1(self.test)
        f2i(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int32)
        self.assertEqual(numpy.int(1), self.test.stack.pop_op())

    def test_f2l(self):
        """test f2l (float to long)"""
        fconst_1(self.test)
        f2l(self.test)
        assert isinstance(self.test.stack.peek(), numpy.int64)
        self.assertEqual(numpy.int64(1), self.test.stack.pop_op(pop_twice))

    def test_fadd(self):
        """tests the fadd opcodes"""
        self.test.stack.push_op(numpy.float32(0.0))
        self.test.stack.push_op(numpy.float32(0.0))
        fadd(self.test)
        self.assertEqual(self.test.stack.peek(), 0.0)
        self.test.stack.push_op(numpy.float32(2.0))
        self.test.stack.push_op(numpy.float32(1.0))
        fadd(self.test)
        self.assertEqual(self.test.stack.peek(), 3.0)
        self.test.stack.push_op(numpy.float32(2.15))
        self.test.stack.push_op(numpy.float32(1.40))
        fadd(self.test)
        self.assertAlmostEqual(self.test.stack.peek(), 3.55, places=2)

    def test_fsub(self):
        """tests the fsub opcodes"""
        self.test.stack.push_op(numpy.float32(0.0))
        self.test.stack.push_op(numpy.float32(0.0))
        fsub(self.test)
        self.assertEqual(self.test.stack.peek(), 0.0)
        self.test.stack.push_op(numpy.float32(5.0))
        self.test.stack.push_op(numpy.float32(2.0))
        fsub(self.test)
        self.assertEqual(self.test.stack.peek(), 3.0)

    def test_fmul(self):
        """tests the fmul opcode"""
        self.test.stack.push_op(numpy.float32(2.0))
        self.test.stack.push_op(numpy.float32(3.0))
        fmul(self.test)
        self.assertEqual(self.test.stack.peek(), 6.0)
        self.test.stack.push_op(numpy.float32(2.0))
        self.test.stack.push_op(numpy.float32(3.0))
        fmul(self.test)
        self.assertEqual(self.test.stack.peek(), 6.0)

    def test_fdiv(self):
        """tests the fdiv opcode"""
        self.test.stack.push_op(numpy.float32(4.0))
        self.test.stack.push_op(numpy.float32(2.0))
        fdiv(self.test)
        self.assertEqual(self.test.stack.peek(), 2.0)

    def test_frem(self):
        """tests the irem opcode"""
        self.test.stack.push_op(numpy.float32(0.0))
        self.test.stack.push_op(numpy.float32(0.0))
        frem(self.test)
        self.assertEqual(self.test.stack.peek(), 0.0)
        self.test.stack.push_op(numpy.float32(5.0))
        self.test.stack.push_op(numpy.float32(5.0))
        frem(self.test)
        self.assertEqual(self.test.stack.peek(), 0.0)

    def test_ladd(self):
        """tests the ladd opcodes"""
        self.test.stack.push_op(numpy.int64(0), push_twice)
        self.test.stack.push_op(numpy.int64(0), push_twice)
        ladd(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 0)
        self.test.stack.push_op(numpy.int64(2), push_twice)
        self.test.stack.push_op(numpy.int64(1), push_twice)
        ladd(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 3)
        self.test.stack.push_op(numpy.int64(2), push_twice)
        self.test.stack.push_op(numpy.int64(4), push_twice)
        ladd(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 6)

    def test_lsub(self):
        """tests the lsub opcodes"""
        self.test.stack.push_op(numpy.int64(0), push_twice)
        self.test.stack.push_op(numpy.int64(0), push_twice)
        lsub(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 0)
        self.test.stack.push_op(numpy.int64(5), push_twice)
        self.test.stack.push_op(numpy.int64(2), push_twice)
        lsub(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 3)

    def test_lmul(self):
        """tests the lmul opcode"""
        self.test.stack.push_op(numpy.int64(2), push_twice)
        self.test.stack.push_op(numpy.int64(3), push_twice)
        lmul(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 6)
        self.test.stack.push_op(numpy.int64(-2), push_twice)
        self.test.stack.push_op(numpy.int64(-3), push_twice)
        lmul(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 6)

    def test_ldiv(self):
        """tests the ldiv opcode"""
        self.test.stack.push_op(numpy.int64(4), push_twice)
        self.test.stack.push_op(numpy.int64(2), push_twice)
        ldiv(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 2)
        self.test.stack.push_op(numpy.int64(-4), push_twice)
        self.test.stack.push_op(numpy.int64(2), push_twice)
        ldiv(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), -2)

    def test_lrem(self):
        """tests the lrem opcode"""
        self.test.stack.push_op(numpy.int64(0), push_twice)
        self.test.stack.push_op(numpy.int64(0), push_twice)
        lrem(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 0)
        self.test.stack.push_op(numpy.int64(5), push_twice)
        self.test.stack.push_op(numpy.int64(5), push_twice)
        lrem(self.test)
        self.assertEqual(self.test.stack.pop_op(pop_twice), 0)
