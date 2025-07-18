# Build a custom `Stack` similar to the `Queue` you built

class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None 

# DECORATOR TO LOG POP OPERATIONS
def pop_with_logging(func):
    def wrapper(self):
        print(f"Popping item... Current stack size: {self.length}")
        item = func(self)
        print(f"Popped item: {item}. Updated stack size: {self.length}")
        return item
    return wrapper

class Stack:
    def __init__(self):
        self.top = None  # Top of the stack
        self.length = 0  # Track number of items

    def is_empty(self):
        return self.top is None
    
    def peek(self):
        # Return the item at the top without removing it
        if self.is_empty():
            return None
        return self.top.value
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    @pop_with_logging
    def pop(self):
        if self.is_empty():
            return None
        pop_node = self.top
        self.top = self.top.next    # Move top to the next node down 
        self.length -= 1
        return pop_node.value
    
# CREATE A NEW STACK
nigth_routine = Stack()

# ADD TASK TO THE STACK
nigth_routine.push("brush teeth")
nigth_routine.push("read a book")
nigth_routine.push("set alarm")

# SEE LAST TASK BEFORE QUE DO IT
print("Last task before sleep:", nigth_routine.peek())

# REMOVE THE LAST TASK FROM THE STACK (like you just did it)
done_task = nigth_routine.pop()
print(f"Done: {done_task}")