# The following is a 'shbang' line which makes this script directly executable
#!python

from jvpm.jvm_stack import JvmStack
from jvpm.class_file import ClassFile
from jvpm.method_table import MethodTable
from jvpm.op_codes import OpCodes
import sys

class Jvpm:

    def __init__(self):
        self.stack = JvmStack()
        self.class_data = ClassFile(sys.argv[1])
        self.nmt = MethodTable(self.stack)
        self.ops = OpCodes(self.stack, self.class_data, self.nmt)

        # print('\nAnd then I ran:')
        self.ops.parse_codes()


if __name__ == "__main__":
    Jvpm()