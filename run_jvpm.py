# The following is a 'shbang' line which makes this script directly executable
#!python

from jvpm.jvm_stack import JvmStack
from jvpm.class_file import ClassFile
from jvpm.op_codes import OpCodes
from jvpm.method_table import MethodTable
import sys


stack = JvmStack()
class_data = ClassFile('AddTwo.class') #(sys.argv[1])
nmt = MethodTable()
print(class_data.run_code)
opperclops = OpCodes('AddTwo.class')
opperclops.parse_codes(class_data.fields_begin)

#for op in class_data.run_code:
#    print(op)
#    opperdops.interpret(op)