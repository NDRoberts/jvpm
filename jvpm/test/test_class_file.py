"""Test the instantiation and methods of the JVPM's ClassFile"""
import unittest
from unittest.mock import mock_open, patch
from jvpm.class_file import *


class TestClassFile(unittest.TestCase):
    """this class tests the ClassFileClass"""

    def setUp(self):

        mocko = mock_open(read_data=(
            b'\xca\xfe\xba\xbe\x00\x00\x00\x38\x00\x1d\x0a\x00\x06\x00\x0f\x09' +
            b'\x00\x10\x00\x11\x08\x00\x12\x0a\x00\x13\x00\x14\x07\x00\x15\x07' +
            b'\x00\x16\x01\x00\x06\x3c\x69\x6e\x69\x74\x3e\x01\x00\x03\x28\x29' +
            b'\x56\x01\x00\x04\x43\x6f\x64\x65\x01\x00\x0f\x4c\x69\x6e\x65\x4e' +
            b'\x75\x6d\x62\x65\x72\x54\x61\x62\x6c\x65\x01\x00\x04\x6d\x61\x69' +
            b'\x6e\x01\x00\x16\x28\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67' +
            b'\x2f\x53\x74\x72\x69\x6e\x67\x3b\x29\x56\x01\x00\x0a\x53\x6f\x75' +
            b'\x72\x63\x65\x46\x69\x6c\x65\x01\x00\x0f\x48\x65\x6c\x6c\x6f\x57' +
            b'\x6f\x72\x6c\x64\x2e\x6a\x61\x76\x61\x0c\x00\x07\x00\x08\x07\x00' +
            b'\x17\x0c\x00\x18\x00\x19\x01\x00\x0d\x48\x65\x6c\x6c\x6f\x2c\x20' +
            b'\x57\x6f\x72\x6c\x64\x21\x07\x00\x1a\x0c\x00\x1b\x00\x1c\x01\x00' +
            b'\x0a\x48\x65\x6c\x6c\x6f\x57\x6f\x72\x6c\x64\x01\x00\x10\x6a\x61' +
            b'\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x4f\x62\x6a\x65\x63\x74\x01\x00' +
            b'\x10\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x79\x73\x74\x65' +
            b'\x6d\x01\x00\x03\x6f\x75\x74\x01\x00\x15\x4c\x6a\x61\x76\x61\x2f' +
            b'\x69\x6f\x2f\x50\x72\x69\x6e\x74\x53\x74\x72\x65\x61\x6d\x3b\x01' +
            b'\x00\x13\x6a\x61\x76\x61\x2f\x69\x6f\x2f\x50\x72\x69\x6e\x74\x53' +
            b'\x74\x72\x65\x61\x6d\x01\x00\x07\x70\x72\x69\x6e\x74\x6c\x6e\x01' +
            b'\x00\x15\x28\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74' +
            b'\x72\x69\x6e\x67\x3b\x29\x56\x00\x21\x00\x05\x00\x06\x00\x00\x00' +
            b'\x00\x00\x02\x00\x01\x00\x07\x00\x08\x00\x01\x00\x09\x00\x00\x00' +
            b'\x1d\x00\x01\x00\x01\x00\x00\x00\x05\x2a\xb7\x00\x01\xb1\x00\x00' +
            b'\x00\x01\x00\x0a\x00\x00\x00\x06\x00\x01\x00\x00\x00\x01\x00\x09' +
            b'\x00\x0b\x00\x0c\x00\x01\x00\x09\x00\x00\x00\x25\x00\x02\x00\x01' +
            b'\x00\x00\x00\x09\xb2\x00\x02\x12\x03\xb6\x00\x04\xb1\x00\x00\x00' +
            b'\x01\x00\x0a\x00\x00\x00\x0a\x00\x02\x00\x00\x00\x03\x00\x08\x00' +
            b'\x04\x00\x01\x00\x0d\x00\x00\x00\x02\x00\x0e'
        ))

        with patch('__main__.open', mocko):
            self.class_file = ClassFile('jvpm/Java/HelloWorld.class')


    def test_fixed_values(self):
        """Check the set values of the Magic number and the Major and Minor version."""
        self.assertEqual(self.class_file.magic, b'\xca\xfe\xba\xbe')
        self.assertEqual(self.class_file.minor, 0)
        self.assertEqual(self.class_file.major, 56)

    def test_val_counts(self):
        """ Check that the counts for Constant Pool, Interfaces, Fields, Methods, 
        and Attributes match counts given by invoking javap.
        """
        self.assertEqual(self.class_file.pool_count, 29)
        self.assertEqual(self.class_file.interfaces_count, 0)
        self.assertEqual(self.class_file.fields_count, 0)
        self.assertEqual(self.class_file.methods_count, 2)
        self.assertEqual(self.class_file.class_attributes_count, 1)

    def test_get_u8(self):
        """ Test the get_u8 method. """
        self.class_file.offset = 0
        bytes = get_u8(self.class_file)
        self.assertEqual(bytes, b'\xca\xfe\xba\xbe\x00\x00\x00\x38')


    # def setUp(self):
    #     """set up the test"""
    #     mock_object = mock_open(
    #         read_data=b'\xca\xfe\xba\xbe\x00\x00\x00\x34\x00\x0f\x0a\x00\x03\x00\x0c\x07' +
    #         b'\x00\x0d\x07\x00\x0e\x01\x00\x06\x3c\x69\x6e\x69\x74\x3e\x01\x00' +
    #         b'\x03\x28\x29\x56\x01\x00\x04\x43\x6f\x64\x65\x01\x00\x0f\x4c\x69' +
    #         b'\x6d\x61\x69\x6e\x01\x00\x16\x28\x5b\x4c\x6a\x61\x76\x61\x2f\x6c' +
    #         b'\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x29\x56\x01\x00\x0a' +
    #         b'\x53\x6f\x75\x72\x63\x65\x46\x69\x6c\x65\x01\x00\x0b\x73\x69\x6d' +
    #         b'\x53\x6f\x75\x72\x63\x65\x46\x69\x6c\x65\x01\x00\x0b\x73\x69\x6d' +
    #         b'\x70\x6c\x65\x2e\x6a\x61\x76\x61\x0c\x00\x04\x00\x05\x01\x00\x04' +
    #         b'\x74\x65\x73\x74\x01\x00\x10\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67' +
    #         b'\x2f\x4f\x62\x6a\x65\x63\x74\x00\x20\x00\x02\x00\x03\x00\x00\x00' +
    #         b'\x00\x00\x02\x00\x00\x00\x04\x00\x05\x00\x01\x00\x06\x00\x00\x00' +
    #         b'\x1d\x00\x01\x00\x01\x00\x00\x00\x05\x2a\xb7\x00\x01\xb1\x00\x00' +
    #         b'\x00\x01\x00\x07\x00\x00\x00\x06\x00\x01\x00\x00\x00\x01\x00\x08' +
    #         b'\x00\x08\x00\x09\x00\x01\x00\x06\x00\x00\x00\x1e\x00\x01\x00\x02' +
    #         b'\x00\x00\x00\x06\x04\x3c\x84\x01\x01\xb1\x00\x00\x00\x01\x00\x07' +
    #         b'\x00\x00\x00\x06\x00\x01\x00\x00\x00\x01\x00\x01\x00\x0a\x00\x00' +
    #         b'\x00\x02\x00\x0b')
    #     with patch('builtins.open', mock_object):
    #         self.class_file = ClassFile('jvpm/Test.class')

    # def test_magic(self):
    #     """tests the get_magic method"""
    #     self.assertEqual(self.class_file.get_magic(), b'\xCA\xFE\xBA\xBE')

    # def test_minor(self):
    #     """tests the get_minor method"""
    #     self.assertEqual(self.class_file.get_minor(), b"\x00\x00")

    # def test_major(self):
    #     """tests the get_major method"""
    #     self.assertEqual(self.class_file.get_major(), b'\x004')

    # def test_constant_pool_count(self):
    #     """tests the get_constant_pool_count method"""
    #     self.assertEqual(
    #         self.class_file.get_constant_pool_count(),
    #         b"\x00\x0f")
