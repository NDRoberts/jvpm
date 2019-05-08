"""Test the class and methods of the main JVPM running module."""
# Disables pylint "unused wildcard import" error
# pylint: disable=W0614

import sys
import unittest
from unittest.mock import patch

from run_jvpm import Jvpm


class TestRunJvpm(unittest.TestCase):
    """A battery of tests to check instantiation of a JVPM."""

    def test_direct_class(self):
        """ Instantiate a JVPM by directly passing a Java class file."""
        test = Jvpm("jvpm/Java/HelloWorld.class")
        self.assertIsInstance(test, Jvpm)

    def test_use_sysarg(self):
        """Attempt to instantiate a JVPM using runtime arguments."""
        test_args = ["run_jvpm.py", "jvpm/Java/HelloWorld.class"]
        with patch.object(sys, "argv", test_args):
            test = Jvpm()
            self.assertIsInstance(test, Jvpm)

    def test_no_args(self):
        """ Instantiate a JVPM without providing a Java class file."""
        test_args = ["run_jvpm.py"]
        with patch.object(sys, "argv", test_args):
            with self.assertRaises(SystemExit) as bad_construction:
                Jvpm()
        self.assertEqual(bad_construction.exception.code, "BIG STUPID FAIL")
