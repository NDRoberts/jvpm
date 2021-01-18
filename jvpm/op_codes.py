"""this file contains the OpCodes class"""
# utilizes NumPy package to handle 32 bit int over/underflow in Java
import numpy  # to get the java-like behavior for arithmetic

from .jvm_stack import pop_twice, push_twice

# shuts off the overflow warnings from numpy
numpy.seterr(over="ignore", under="ignore")


class OpCodes:
    """This class interprets opcodes"""

    def __init__(self, class_stack, class_data, method_table):
        """this is the constructor"""
        self.stack = class_stack
        self.nmt = method_table
        self.class_data = class_data
        self.data = class_data.run_code
        self.table = {
            0x19: [aload, 2],
            0x2A: [aload_0, 1],
            0x2B: [aload_1, 1],
            0x2C: [aload_2, 1],
            0x2D: [aload_3, 1],
            0x10: [bipush, 2],
            0x59: [dup, 1],
            0x8D: [f2d, 1],
            0x8B: [f2i, 1],
            0x8C: [f2l, 1],
            0x62: [fadd, 1],
            0x96: [fcmpg, 1],
            0x95: [fcmpl, 1],
            0x0B: [fconst_0, 1],
            0x0C: [fconst_1, 1],
            0x0D: [fconst_2, 1],
            0x6E: [fdiv, 1],
            0x17: [fload, 2],
            0x22: [fload_0, 1],
            0x23: [fload_1, 1],
            0x24: [fload_2, 1],
            0x25: [fload_3, 1],
            0x76: [fneg, 1],
            0x6A: [fmul, 1],
            0x72: [frem, 1],
            0x38: [fstore, 1],
            0x43: [fstore_0, 1],
            0x44: [fstore_1, 2],
            0x45: [fstore_2, 1],
            0x46: [fstore_3, 1],
            0x66: [fsub, 1],
            0xB2: [getstatic, 3],
            0xBB: [new, 3],
            0x91: [i2b, 1],
            0x92: [i2c, 1],
            0x87: [i2d, 1],
            0x86: [i2f, 1],
            0x60: [iadd, 1],
            0x7E: [iand, 1],
            0x02: [iconst_m1, 1],
            0x03: [iconst_0, 1],
            0x04: [iconst_1, 1],
            0x05: [iconst_2, 1],
            0x06: [iconst_3, 1],
            0x07: [iconst_4, 1],
            0x08: [iconst_5, 1],
            0x6C: [idiv, 1],
            0x84: [iinc, 3],
            0x15: [iload, 2],
            0x1A: [iload_0, 1],
            0x1B: [iload_1, 1],
            0x1C: [iload_2, 1],
            0x1D: [iload_3, 1],
            0x68: [imul, 1],
            0x74: [ineg, 1],
            0xB7: [invokespecial, 3],
            0xB6: [invokevirtual, 3],
            0x80: [ior, 1],
            0x70: [irem, 1],
            0x78: [ishl, 1],
            0x7A: [ishr, 1],
            0x36: [istore, 2],
            0x3B: [istore_0, 1],
            0x3C: [istore_1, 1],
            0x3D: [istore_2, 1],
            0x3E: [istore_3, 1],
            0x64: [isub, 1],
            0x7C: [iushr, 1],
            0x82: [ixor, 1],
            0x8A: [l2d, 1],
            0x89: [l2f, 1],
            0x88: [l2i, 1],
            0x61: [ladd, 1],
            0x7F: [land, 1],
            0x94: [lcmp, 1],
            0x09: [lconst_0, 1],
            0x0A: [lconst_1, 1],
            0x12: [ldc, 2],
            0x6D: [ldiv, 1],
            0x16: [lload, 2],
            0x1E: [lload_0, 1],
            0x1F: [lload_1, 1],
            0x20: [lload_2, 1],
            0x21: [lload_3, 1],
            0x69: [lmul, 1],
            0x71: [lrem, 1],
            0x79: [lshl, 1],
            0x7B: [lshr, 1],
            0x37: [lstore, 2],
            0x3F: [lstore_0, 1],
            0x40: [lstore_1, 1],
            0x41: [lstore_2, 1],
            0x42: [lstore_3, 1],
            0x65: [lsub, 1],
            0x83: [lxor, 1],
            0x00: [not_implemented, 1],
            0x01: [also_not_implemented, 1],
            0xB1: [ret, 2],
        }

    def parse_codes(self):
        """Call the Interpret function on each opcode in the provided data."""
        self.byte_count = 0
        while self.byte_count < len(self.data):
            if self.data[self.byte_count] in self.table.keys():
                self.interpret(self.data[self.byte_count])
            else:
                self.interpret(0)

    def interpret(self, value):
        """Interpret a given opcode."""
        args = []
        if self.table[value][1] > 1:
            args = self.data[
                self.byte_count + 1: self.byte_count + self.table[value][1]
            ]
        self.byte_count += self.table[value][1]
        # print('Doing this:', self.table[value][0], 'with args', args)
        return self.table[value][0](self, *args)


def not_implemented(self):
    """this is a dummy function"""
    self.stack.push_op(1)
    self.stack.pop_op()
    return "not implemented"


def also_not_implemented(self):
    """This function is dummier than the last."""
    self.stack.push_op(1)
    self.stack.pop_op()
    return "also not implemented"



def aload(self, index):
    """loads a reference onto stack from local variable array at <index>"""
    self.stack.push_op(numpy.int32(self.stack.local_array[index]))


def aload_0(self):
    """Loads a reference onto the stack from local array index 0."""
    self.stack.push_op(self.stack.local_array[0])


def aload_1(self):
    """Loads a reference onto the stack from local array index 1."""
    self.stack.push_op(self.stack.local_array[1])


def aload_2(self):
    """Loads a reference onto the stack from local array index 2."""
    self.stack.push_op(self.stack.local_array[2])


def aload_3(self):
    """Loads a reference onto the stack from local array index 3."""
    self.stack.push_op(self.stack.local_array[3])



def iload(self, index):
    """loads an int from local data array at <index> onto stack"""
    self.stack.push_op(self.stack.local_array[index])



def iload_0(self):
    """loads an int from local data array at index 0 onto stack"""
    self.stack.push_op(self.stack.local_array[0])



def iload_1(self):
    """loads an int from local data array at index 1 onto stack"""
    self.stack.push_op(self.stack.local_array[1])



def iload_2(self):
    """loads an int from local data array at index 2 onto stack"""
    self.stack.push_op(self.stack.local_array[2])



def iload_3(self):
    """loads an int from local data array at index 3 onto stack"""
    self.stack.push_op(self.stack.local_array[3])


def ret(self, index):
    """ Implement the ret opcode, return from subroutine. Write
    returnAddress of the current frame from local variable at
    index to the JVM's pc register. For now, just return it. """
    return self.stack.local_array[index]


def iconst_m1(self):
    """implements iconst_m opcode, loads int -1 onto stack"""
    self.stack.push_op(-1)


def iconst_0(self):
    """implements iconst_0 opcode, loads int 0 onto stack"""
    self.stack.push_op(0)


def iconst_1(self):
    """implements iconst_1 opcode, loads int 1 onto stack"""
    self.stack.push_op(1)


def iconst_2(self):
    """implements iconst_2 opcode, loads int 2 onto stack"""
    self.stack.push_op(2)


def iconst_3(self):
    """"implememts iconst_3 opcode, loads int 3 onto stack"""
    self.stack.push_op(3)


def iconst_4(self):
    """implements iconst_4 opcode, loads int 4 onto stack"""
    self.stack.push_op(4)


def iconst_5(self):
    """implements iconst_5 opcode, loads int 5 onto stack"""
    self.stack.push_op(5)


def istore(self, index):
    """loads an int from stack into local array at <index>"""
    self.stack.local_array[index] = self.stack.pop_op()



def istore_0(self):
    """this function implements the istore_0 opcode"""
    self.stack.local_array[0] = self.stack.pop_op()



def istore_1(self):
    """this function implements the istore_1 opcode"""
    self.stack.local_array[1] = self.stack.pop_op()
    self.stack.push_op(1)
    self.stack.pop_op()


def istore_2(self):
    """this function implements the istore_2 opcode"""
    self.stack.local_array[2] = self.stack.pop_op()



def istore_3(self):
    """this function implements the istore_3 opcode"""
    self.stack.local_array[3] = self.stack.pop_op()



def lstore(self, index):
    """implements the lstore opcode for 64 bit longs"""
    self.stack.local_array[index] = self.stack.pop_op(pop_twice)



def fstore(self, index):
    """implements the fstore opcode for 32 bit floats"""
    self.stack.local_array[index] = numpy.int64(self.stack.pop_op(pop_twice))



def lstore_0(self):
    """implements lstore_0 opcode, loads 64 bit long 0 into local array"""
    self.stack.local_array[0] = self.stack.pop_op(pop_twice)



def lstore_1(self):
    """implements lstore_1 opcode, loads 64 bit long 1 into local array"""
    self.stack.local_array[1] = self.stack.pop_op(pop_twice)



def lstore_2(self):
    """implements lstore_2 opcode, loads 64 bit long 2 into local array"""
    self.stack.local_array[2] = self.stack.pop_op(pop_twice)



def lstore_3(self):
    """implements lstore_3 opcode, loads 64 bit long 3 into local array"""
    self.stack.local_array[3] = self.stack.pop_op(pop_twice)



def fstore_0(self):
    """implements the fstore_0 opcode for 32 bit floats"""
    self.stack.local_array[0] = numpy.float32(self.stack.pop_op(pop_twice))



def fstore_1(self):
    """implements the fstore_1 opcode for 32 bit floats"""
    self.stack.local_array[1] = numpy.float32(self.stack.pop_op(pop_twice))



def fstore_2(self):
    """implements the fstore_2 opcode for 32 bit floats"""
    self.stack.local_array[2] = numpy.float32(self.stack.pop_op(pop_twice))



def fstore_3(self):
    """implements the fstore_3 opcode for 32 bit floats"""
    self.stack.local_array[3] = numpy.float32(self.stack.pop_op(pop_twice))



def iinc(self, index, constant):
    """ Implements iinc opcode, increments local
    variable at <index> by constant.
    """
    self.stack.local_array[index] += constant


def iadd(self):
    """implements the iadd opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1 + val2)


def isub(self):
    """implements the isub opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1 - val2)


def imul(self):
    """implements the imul opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1 * val2)


def idiv(self):
    """implements the idiv opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(numpy.int32(val1 / val2))


# irem will be implemented in terms of the other operations.
# a%b = a-(a/b)*b
def irem(self):
    """implements the irem opcode"""
    val2 = numpy.int32(self.stack.pop_op())
    val1 = numpy.int32(self.stack.pop_op())
    self.stack.push_op(val1)
    self.stack.push_op(val1)
    self.stack.push_op(val2)
    idiv(self)
    self.stack.push_op(val2)
    imul(self)
    isub(self)


def iand(self):
    """ Perform bitwise AND on the top two operands on the stack. """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    self.stack.push_op(this_val & that_val)


def ineg(self):
    """ Perform bitwise NOT on the top operand on the stack. """
    not_this = self.stack.pop_op()
    self.stack.push_op(~not_this)


def ior(self):
    """ Perform bitwise OR on the top two operands on the stack. """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    self.stack.push_op(this_val | that_val)


def ixor(self):
    """ Perform bitwise XOR on the top two operands on the stack. """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    self.stack.push_op(this_val ^ that_val)


def ishl(self):
    """implements the shl opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1 << val2)


def ishr(self):
    """implements the shl opcode"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    self.stack.push_op(val1 >> val2)


def iushr(self):
    """ Perform bitwise LOGICAL SHIFT RIGHT on
    the top two operands on the stack.
    """
    this_val = self.stack.pop_op()
    that_val = self.stack.pop_op()
    val = 0
    if that_val >= 0:
        val = that_val >> this_val
    else:
        val = (that_val & 0xFFFFFFFF) >> this_val
        print(str(val))
    self.stack.push_op(val)


def i2b(self):
    """ Convert top of stack from int to byte,
     then push it back onto stack. """
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.int8(convert_this))


def i2c(self):
    """ Convert int on top of stack to character,
    and push it, push it real good.
    """
    convert_this = self.stack.pop_op()
    self.stack.push_op(chr(convert_this))


def i2d(self):
    """convert int on top of stack to double, and p-p-push it real good"""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.float64(convert_this))


def i2f(self):
    """convert int on top of stack to float, and push it to the stack."""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.float32(convert_this))


def i2l(self):
    """convert int on top of stack to long, and push it to the stack."""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.int64(convert_this), push_twice)


def i2s(self):
    """convert int on top of stack to short, and push. it. to. the. stack."""
    convert_this = self.stack.pop_op()
    self.stack.push_op(numpy.int16(convert_this))


def getstatic(self, index_byte_1, index_byte_2):
    """Push a field reference from the Constant Pool to the stack."""
    index = (index_byte_1 << 8) + index_byte_2
    self.stack.push_op(self.class_data.constant_pool[index])


def ldc(self, index):
    """Push a constant from the Pool onto the stack."""
    constant = self.class_data.constant_pool[index]
    if constant["type"] == "String":
        string_index = self.class_data.constant_pool[index]["string_index"]
        self.stack.push_op(
            self.class_data.constant_pool[string_index]["value"]
        )


def invokevirtual(self, index_byte_1, index_byte_2):
    """ Implement invokevirtual opcode. """
    index = (index_byte_1 << 8) + index_byte_2
    class_index = self.class_data.constant_pool[index]["class_index"]
    name_and_type_index = self.class_data.constant_pool[index][
        "name_and_type_index"
    ]
    class_name_index = self.class_data.constant_pool[class_index]["name_index"]
    method_name_index = self.class_data.constant_pool[name_and_type_index][
        "name_index"
    ]
    method_descriptor_index = self.class_data.constant_pool[
        name_and_type_index
    ]["descriptor_index"]
    class_name = self.class_data.constant_pool[class_name_index]
    method_name = self.class_data.constant_pool[method_name_index]
    method_descriptor = self.class_data.constant_pool[method_descriptor_index]
    invoked_method = {
        "class_name": class_name,
        "method_name": method_name,
        "method_descriptor": method_descriptor,
    }
    self.nmt.call(invoked_method)


def invokespecial(self, index_byte_1, index_byte_2):
    """This function implements the invokespecial opcode"""
    # byte_1 = self.data[self.byte_count + 1]
    # byte_2 = self.data[self.byte_count + 2]
    # return byte_1 + byte_2
    invokevirtual(self, index_byte_1, index_byte_2)


def new(self, index_byte_1, index_byte_2):
    """ Instanitate a new object. """

    index = (index_byte_1 << 8) + index_byte_2
    # print(self.class_data.constant_pool[index])
    name_index = self.class_data.constant_pool[index]["name_index"]
    # print(self.class_data.constant_pool[name_index])
    self.stack.push_op(self.class_data.constant_pool[name_index]["value"])


def dup(self):
    """pop first value on the stack, duplicate and push back onto stack"""
    value = self.stack.pop_op()
    dup_val = value
    self.stack.push_op(value)
    self.stack.push_op(dup_val)


def lload(self, index):
    """loads a long from local long data array at <index> onto stack"""
    self.stack.push_op(numpy.int64(self.stack.local_array[index]), push_twice)



def lload_0(self):
    """loads a long from local long data array at index 0 onto stack"""
    self.stack.push_op(numpy.int64(self.stack.local_array[0]), push_twice)



def lload_1(self):
    """loads a long from local long data array at index 1 onto stack"""
    self.stack.push_op(numpy.int64(self.stack.local_array[1]), push_twice)



def lload_2(self):
    """loads a long from local long data array at index 2 onto stack"""
    self.stack.push_op(numpy.int64(self.stack.local_array[2]), push_twice)



def lload_3(self):
    """loads a long from local long data array at index 3 onto stack"""
    self.stack.push_op(numpy.int64(self.stack.local_array[3]), push_twice)



def lshl(self):
    """pop a long and an int and shift the long bitwise left by the low 6 bits
    of the int (0-63) and push the result back to the stack"""
    zero_to_sixty_three_mask = 0x3F
    int_val = self.stack.pop_op() & zero_to_sixty_three_mask
    long_val = self.stack.pop_op(pop_twice)
    self.stack.push_op(numpy.int64(long_val) << int_val, push_twice)


def lshr(self):
    """pop a long and an int and shift the long bitwise right by the low 6 bits
    of the int (0-63) and push the result back to the stack"""
    zero_to_sixty_three_mask = 0x3F
    int_val = self.stack.pop_op() & zero_to_sixty_three_mask
    long_val = self.stack.pop_op(pop_twice)
    self.stack.push_op(numpy.int64(long_val) >> int_val, push_twice)


def land(self):
    """pop 2 longs, AND them and push the result to the stack"""
    val2 = self.stack.pop_op(pop_twice)
    val1 = self.stack.pop_op(pop_twice)
    self.stack.push_op(numpy.int64(val1 & val2), push_twice)


def lcmp(self):
    """pop 2 values and push 1 if val1>val2, 0 if val1=val2, -1 if val1<val2"""
    val2 = self.stack.pop_op(pop_twice)
    val1 = self.stack.pop_op(pop_twice)
    val1 -= val2
    if val1 == 0:
        self.stack.push_op(0)
    else:
        self.stack.push_op((val1 / abs(val1)))



def lxor(self):
    """pop 2 long, xor them, and push the result"""
    val2 = self.stack.pop_op(pop_twice)
    val1 = self.stack.pop_op(pop_twice)
    self.stack.push_op(numpy.int64(val1 ^ val2), push_twice)


def fcmph(self, nan_spec):
    """helper function to reduce duplication. nan_spec
    is the value to push if at least one of the values
    is not a number"""
    val2 = self.stack.pop_op()
    val1 = self.stack.pop_op()
    if numpy.isnan(val1) or numpy.isnan(val2):
        self.stack.push_op(nan_spec)
    else:
        val1 -= val2
        if val1 == 0:
            self.stack.push_op(0)
        else:
            self.stack.push_op((val1 / abs(val1)))



def fcmpg(self):
    """pop 2 values and push 1 if val1>val2, 0 if val1=val2, -1 if val1<val2,
    1 if val1 or val2 is NaN"""
    fcmph(self, 1)


def fcmpl(self):
    """pop 2 values and push 1 if val1>val2, 0 if val1=val2, -1 if val1<val2,
    -1 if val1 or val2 is NaN"""
    fcmph(self, -1)


def fneg(self):
    """pop a float and push the negation to the stack"""
    self.stack.push_op(numpy.negative(self.stack.pop_op()))


def lconst_0(self):
    """push 0L to the stack"""
    self.stack.push_op(numpy.int64(0), push_twice)


def lconst_1(self):
    """push 1L to the stack"""
    self.stack.push_op(numpy.int64(1), push_twice)


def fconst_0(self):
    """push 0F to the stack"""
    self.stack.push_op(numpy.float32(0))


def fconst_1(self):
    """push 1F to the stack"""
    self.stack.push_op(numpy.float32(1))


def fconst_2(self):
    """push 2F to the stack"""
    self.stack.push_op(numpy.float32(2))


def fload(self, index):
    """loads a float from local float data array at <index> onto stack"""
    self.stack.push_op(numpy.float32(self.stack.local_array[index]))



def fload_0(self):
    """loads a float from local float data array at index 0 onto stack"""
    self.stack.push_op(numpy.float32(self.stack.local_array[0]))



def fload_1(self):
    """loads a float from local float data array at index 1 onto stack"""
    self.stack.push_op(numpy.float32(self.stack.local_array[1]))



def fload_2(self):
    """loads a float from local float data array at index 2 onto stack"""
    self.stack.push_op(numpy.float32(self.stack.local_array[2]))



def fload_3(self):
    """loads a float from local float data array at index 3 onto stack"""
    self.stack.push_op(numpy.float32(self.stack.local_array[3]))



def l2d(self):
    """convert long to double"""
    self.stack.push_op(numpy.float64(self.stack.pop_op(pop_twice)), push_twice)


def l2i(self):
    """convert long to int"""
    self.stack.push_op(numpy.int32(self.stack.pop_op(pop_twice)))


def l2f(self):
    """convert long to int"""
    self.stack.push_op(numpy.float32(self.stack.pop_op(pop_twice)))


def f2d(self):
    """convert float to double"""
    self.stack.push_op(numpy.float64(self.stack.pop_op()), push_twice)


def f2i(self):
    """convert float to int"""
    self.stack.push_op(numpy.int32(self.stack.pop_op()))


def f2l(self):
    """convert float to long"""
    self.stack.push_op(numpy.int64(self.stack.pop_op()), push_twice)


def fadd(self):
    """implements the fadd opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    self.stack.push_op(val1 + val2)


def ladd(self):
    """implements the ladd opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    self.stack.push_op(val1 + val2, push_twice)


def fsub(self):
    """implements the fsub opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    self.stack.push_op(val1 - val2)


def lsub(self):
    """implements the fsub opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    self.stack.push_op(val1 - val2, push_twice)


def fmul(self):
    """implements the fmul opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    self.stack.push_op(val1 * val2)


def lmul(self):
    """implements the fsub opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    self.stack.push_op(val1 * val2, push_twice)


def fdiv(self):
    """implements the fdiv opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    self.stack.push_op(numpy.float32(val1 / val2))


def ldiv(self):
    """implements the fsub opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    self.stack.push_op(numpy.int64(val1 / val2), push_twice)


# frem will be implemented in terms of the other operations.
# a%b = a-(a/b)*b
def frem(self):
    """implements the frem opcode"""
    val2 = numpy.float32(self.stack.pop_op())
    val1 = numpy.float32(self.stack.pop_op())
    if val2 == 0:
        self.stack.push_op(val2)
    else:
        self.stack.push_op(val1)
        self.stack.push_op(val1)
        self.stack.push_op(val2)
        fdiv(self)
        self.stack.push_op(val2)
        fmul(self)
        fsub(self)


def lrem(self):
    """implements the frem opcode"""
    val2 = numpy.int64(self.stack.pop_op(pop_twice))
    val1 = numpy.int64(self.stack.pop_op(pop_twice))
    if val2 == 0:
        self.stack.push_op(val2, push_twice)
    else:
        self.stack.push_op(val1, push_twice)
        self.stack.push_op(val1, push_twice)
        self.stack.push_op(val2, push_twice)
        ldiv(self)
        self.stack.push_op(val2, push_twice)
        lmul(self)
        lsub(self)


def bipush(self, byte):
    """ Push a byte onto the stack. """
    self.stack.push_op(byte)
