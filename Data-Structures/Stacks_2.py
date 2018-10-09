# Stack that is uding the LIFO (Last in, first out method)


class Stack:
    def __init__(self):
       self.stack_list = []
    def add(self, value):
       """
       Add element at last
       Time complexity: 0(1)
       """
       self.stack_list.appen(value)
       
     def remove(self):
       """
       Remove element from last return value
       Time complexity 0(1)
       """
       return self.stack_list.pop()
     
     def is_empty(self):
       """
       Return size of stack
       Time complexity: 0(1)
       """
       return not self.size()
       
     def size(self):
       """
       Return size of stack
       Time complexity: 0(1)
       
       return len(self.stack.stack_list)
