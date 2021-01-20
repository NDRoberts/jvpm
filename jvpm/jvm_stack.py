"""This class implements the operand stack for the jvm."""


class JvmStack:
    """JvmStack."""

    def __init__(self):
        """Constructor. Initializes the stack to be empty."""
        self.stack = []
        self.local_array = [0, 1, 2, 3]

    def push_op(self, obj, push_strategy=lambda stack, obj: stack.append(obj)):
        """Pushes one operand onto the top of the stack. If the stack is empty,
        this method raises an EmptyStackError. Push_strategy is a function that
        determines how the pushing is done. This is necessary because when pushing
        longs and doubles, two pushes are required.
        """
        push_strategy(self.stack, obj)

    def pop_helper(self):
        """Pops one object off of the stack and then returns it."""
        if self.stack:
            return self.stack.pop()
        raise EmptyStackError("Can't pop from an empty stack")

    def pop_op(self, pop_strategy=lambda stack: stack.pop_helper()):
        """Modify the original pop_op. It enables
        the use of different popping strategies."""
        return pop_strategy(self)

    def peek(self):
        """Will not return the None.Instead, it will
        return the actual long or double value.
        """
        index = -1
        while self.stack[index] is None:
            index -= 1
        return self.stack[index]


class EmptyStackError(Exception):
    """Error raised when there is an empty stack."""


def push_twice(stack, obj):
    """Push method to handle long and fp types."""
    stack.append(obj)
    stack.append(None)


def pop_twice(stack):
    """Pop method to handle long and fp types."""
    stack.pop_helper()
    return stack.pop_helper()
