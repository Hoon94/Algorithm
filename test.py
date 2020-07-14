class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False
    
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False


if __name__ == "__main__":
    double_linked_list = NodeMgmt(0)
    for data in range(1, 10):
        double_linked_list.insert(data)
    #double_linked_list.desc()

    node_3 = double_linked_list.search_from_head(3)
    print(node_3.data)

    node_3 = double_linked_list.search_from_head(10)
    if node_3:
        print(node_3.data)
    else:
        print("No data")