# The following is a 'shbang' line which makes this script directly executable
#!python

from jvpm.jvm_stack import JvmStack
from jvpm.class_file import ClassFile
from jvpm.method_table import MethodTable
from jvpm.op_codes import OpCodes
#import jvpm.op_codes as ops
import sys

class Jvpm:

    def __init__(self):
        self.stack = JvmStack()
        self.class_data = ClassFile('AddTwo.class') #(sys.argv[1])
        self.nmt = MethodTable(self.stack)
        self.ops = OpCodes(self.stack, self.class_data, self.nmt)

        self.ops.parse_codes()

        for remainder in self.stack.stack:
            print(remainder)


if __name__ == "__main__":
    Jvpm()