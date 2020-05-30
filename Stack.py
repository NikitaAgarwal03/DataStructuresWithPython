class Node:
    def __init__(self, value,link_node=None):       
        self.value = value
        self.link_node = None
    def get_value(self):
        return self.value
    def get_link_node(self):
        return self.link_node
    def set_link_node(self,link_node):
        self.link_node=link_node
        
yacko=Node('likes to yak')
wacko=Node('has a penchant for hoarding snacks')
dot=Node('enjoys spending time in movie lots')
yacko.set_link_node(dot)
dot.set_link_node(wacko)
dots_data=yacko.get_link_node().get_value()
wackos_data=dot.get_link_node().get_value()
print(dots_data)
print(wackos_data)

class Stack:
    def __init__(self,size,limit,top_item=None):
        self.top_item=None
        self.limit=limit
        self.size=0
    def peek(self):
        if not self.is_empty():
            return Node(self.top_item).get_value()
        else:
            print('Stack is empty')
    def push(self,value):
        if self.has_space():
            self.item =Node(value)
            self.newitem = self.item.set_link_node(value)
            self.top_item=self.newitem
            self.size +=1
        else:
            print('All out of space!')
    def pop(self):
        if not self.is_empty():
            self.item_to_remove=self.top_item
            self.top_item=Node(self.item_to_remove).get_link_node()
            self.size -=1
            return Node(self.item_to_remove).get_value()
        else:
            print('Stack is empty')
    def has_space(self):
        if(self.limit > self.size):
            return True
        else:
            return False
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
pizza_stack=Stack(5,5)
pizza_stack.push("Pizza order1")
pizza_stack.push("Your pizza is here")
pizza_stack.pop()
    
    
