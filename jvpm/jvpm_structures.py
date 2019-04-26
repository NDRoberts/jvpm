import struct


class JvmStack:
    """Primary stack for the Java Virtual Machine"""

    def __init__(self):
        """Constructor. Initializes the stack to be empty"""
        self.stack = []
        self.local_array = [0, 1, 2, 3]

    def push_op(self, obj, push_strategy=lambda stack, obj: stack.append(obj)):
        """Pushes one operand onto the top of the stack.  push_strategy is a 
        function that determines how the pushing is done.  This is necessary 
        because when pushing longs and doubles, two pushes are required."""
        push_strategy(self.stack, obj)

    def pop_helper(self):
        """Pops one object off of the stack and then returns it.
        If the stack is empty, then this method raises an EmptyStackError."""
        if self.stack:
            return self.stack.pop()
        raise EmptyStackError("Can't pop from an empty stack")

    def pop_op(self, pop_strategy=lambda stack: stack.pop_helper()):
        """This method modifies the original pop_op so that it can use 
        different popping strategies."""
        return pop_strategy(self)

    def peek(self):
        """returns the top element of the stack without popping it. Since 
        longs and doubles take up two spaces on the stack, I will push None 
        on top of such values. However, to remain consistent with past usage, 
        this method will not return the None. Instead, it will return the 
        actual long or double value."""
        index = -1
        while self.stack[index] is None:
            index -= 1
        return self.stack[index]


# - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- -


class EmptyStackError(Exception):
    """error raised when there is an empty stack"""

    def push_twice(self, stack, obj):
        stack.append(obj)
        stack.append(None)

    def pop_twice(self, stack):
        stack.pop_helper()
        return stack.pop_helper()


# - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- -


class ClassFile:
    """this class reads in a class file and does some basic parsing"""

    def __init__(self, name):
        """this is the constructor"""
        with open(name, "rb") as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        """gets the magic number"""
        return self.data[0:4]

    def get_minor(self):
        """gets the minor version"""
        return self.data[4:6]

    def get_major(self):
        """gets the major version"""
        return self.data[6:8]

    def get_constant_pool_count(self):
        """gets the bytes of the constant pool count"""
        return self.data[8:10]


# - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- - -- --- -- -


class ConstantPool:
    """This class represents the constant pool parsed from a class file"""

    def __init__(self, constants):
        """constructor"""
        self.constants = constants
        # the following table contains functions that load various kinds of
        # operands onto the stack.
        self.load_table = {3: ConstantPool.load_int, 8: ConstantPool.load_string}

    def lookup_constant(self, index):
        """Looks up a constant in the constant pool. Index is a string of two 
        bytes that determines which entry in the constant pool will be returned. 
        Let b1 and b2 be the bytes of index. Then, this method shall return the 
        constant at index (b1<<8)+b2"""
        # the index is an unsigned short in big-endian byte order
        numeric_index = struct.unpack(">H", index)[0]
        return self.constants[numeric_index]

    def load_constant(self, index, stack):
        """Loads a constant onto the stack according to its type. 
        Index shall have the same meaning as in lookup_constant.
        Stack shall be the stack onto which the constant shall be loaded.
        The constant shall always be loaded on top of the stack."""
        constant = self.lookup_constant(index)
        tag = constant[0]
        if tag in self.load_table.keys():
            self.load_table[tag](self, constant, stack)
        else:
            stack.push_op(constant)

    def load_int(self, constant, stack):
        """loads an int onto the stack"""
        # integer constants are signed and big-endian.
        decoded = struct.unpack(">i", constant[1:])[0]
        stack.push_op(decoded)
        # use self to make pylint happy
        self.constants.append(1)
        self.constants.pop()

    def load_string(self, constant, stack):
        """loads a string onto the stack"""
        # first get the index of the actual utf-8 contents
        string_index = constant[1:]
        # now get the actual contents at that index
        real_utf8 = self.lookup_constant(string_index)
        # now retrieve the actual string as before
        decoded = real_utf8[3:].decode("utf-8")
        stack.push_op(decoded)

