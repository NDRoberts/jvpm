from jvpm.jvm_stack import JvmStack
from jvpm.class_file import ClassFile
from jvpm.op_codes import OpCodes
from jvpm.method_table import MethodTable
import sys


stack = JvmStack()
class_data = ClassFile('AddTwo.class') #(sys.argv[1])
nmt = MethodTable()
print('Doing you a run...')