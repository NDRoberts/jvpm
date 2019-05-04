"""This module contains implementations of native methods like println"""


class MethodTable:
    """This module contains implementations of native methods like println"""

    def __init__(self, stack):
        """constructor"""
        self.stack = stack
        self.table = {
            'println': println,
            '<init>': init,
            'nextInt': next_int
        }

    def call(self, method):
        self.method = method
        return self.table[self.method['method_name']['value']](self)


def println(self):
    """This function causes the jvm to print to the screen"""
    to_be_printed = self.stack.pop_op()
    self.stack.pop_op()
    print(to_be_printed)

def init(self):
    """take the top two items off the stack and push a scanner object on the stack"""
    self.stack.pop_op()
    self.stack.pop_op()
    self.stack.push_op(self.method['class_name']['value'])

def next_int(self):
    """take the top element of the stack,
read in an int and pushes that int onto the stack"""
    self.stack.pop_op()
    i = int(input())
    self.stack.push_op(i)
