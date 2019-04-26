from jvpm.jvm_stack import JvmStack
from jvpm.class_file import ClassFile
from jvpm.op_codes import OpCodes
from jvpm.method_table import MethodTable
import sys


class jvpm:

    def __init__(self):
        """This method initializes an instance of the JVPM."""
        self.stack = JvmStack()
        self.class_data = ClassFile(sys.argv[1])
        self.nmt = MethodTable()