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
dots_data=dot.get_value()
wackos_data=wacko.get_value()
print(dots_data)
print(wackos_data)
