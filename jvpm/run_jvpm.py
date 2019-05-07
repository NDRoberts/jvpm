""" This class runs the JVPM. """
# The following is a 'shbang' line which makes this script directly executable
#!python
import sys
from jvpm.jvm_stack import JvmStack
from jvpm.class_file import ClassFile
from jvpm.method_table import MethodTable
from jvpm.op_codes import OpCodes
#import jvpm.op_codes as ops

class Jvpm:
    """ This class runs the JVPM. """
    def __init__(self):
        self.stack = JvmStack()
        self.class_data = ClassFile('./jvpm/Java/HelloWorld.class') #(sys.argv[1:])
        self.nmt = MethodTable(self.stack)
        self.ops = OpCodes(self.stack, self.class_data, self.nmt)

        print('\nAnd then I ran:')
        self.ops.parse_codes()

        #for remainder in self.stack.stack:
        #    print(remainder)


if __name__ == "__main__":
    Jvpm()
