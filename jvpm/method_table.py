"""This module contains implementations of native methods like println"""


class MethodTable:
    """This module contains implementations of native methods like println"""

    def __init__(self, stack):
        """constructor"""
        self.stack = stack
        self.table = {
            'println': println,
            '<init>': init,
            'nextInt': next_int,
            'close': close
        }

    def call(self, method):
        """ Implement the call method. """
        self.method = method
        return self.table[self.method['method_name']['value']](self)


def println(self):
    """ This function causes the jvm to print to the screen. """
    print_value = self.stack.pop_op()
    print(print_value)
    return print_value

def init(self):
    """ Take the top two items off the stack and push a scanner object on the stack. """
    self.stack.pop_op()
    self.stack.pop_op()
    self.stack.push_op(self.method['class_name']['value'])

def next_int(self):
    """ Take the top element off the stack.
    Read in an int and pushes that int onto the stack
    """
    self.stack.pop_op()
    i = int(input())
    self.stack.push_op(i)

def close(self):
    """ Close an opened instance of a file or scanner, probably. """
    while self.stack.peek():
        self.stack.pop_op()
