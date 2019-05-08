"""Test the class and methods of the main JVPM running module."""

import sys
import unittest
from run_jvpm import Jvpm
from unittest.mock import Mock, mock_open, patch, call

class TestRunJvpm(unittest.TestCase):

    def test_direct_class(self):
        test = Jvpm('jvpm/Java/HelloWorld.class')
        self.assertIsInstance(test, Jvpm)
    
    def test_use_sysarg(self):
        test_args = ["run_jvpm.py","jvpm/Java/HelloWorld.class"]
        with patch.object(sys, 'argv', test_args):
            test = Jvpm()
            self.assertIsInstance(test, Jvpm)
    
    def test_no_args(self):
        test_args = ["run_jvpm.py"]
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit) as bad_construction:
                Jvpm()
        self.assertEqual(bad_construction.exception.code, 'BIG STUPID FAIL')