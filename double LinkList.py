class Node:
    def __init__(self,vals):
        self.pre = None
        self.next =None
        self.val = vals

class DoubleLinklist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size =+ 1

    def add(self,val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size =+ 1
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
            self.size += 1
    def __remove_node(self,node):
        if node.pre is None:
            self.head = node.next
        else:
            node.pre.next = node.next
        if node.next is None:
            self.tail = node.pre
        else:
            node.next.pre = node.pre


    def remove(self,value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next




    def __str__(self):
        vals=[]
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val)for val in vals)}]"

my_list = DoubleLinklist()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(3)
my_list.add(3)
my_list.add(3)
my_list.add(3)
my_list.add(2)
my_list.add(5)

print(my_list)

my_list.remove(3)
my_list.remove(2)

print(my_list)