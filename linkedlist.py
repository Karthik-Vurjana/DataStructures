class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# insert at beginning , end , at a given index, insert list as a series of nodes, get length of the ll,

class LinkedList:
    def __init__(self,):
        self.head = None

    # get length of the linked list...
    def get_length(self):
        count=0
        p = self.head
        while p:
            p=p.next
            count+=1
        return count

    # print function of ll...
    def print(self):
        if self.head is None:
            print("Linked List Is Empty")
            return
        p = self.head
        lls = ""
        while p:
            lls += str(p.data) + "-->"
            p = p.next
        print(lls)

    # insert node in beginning
    def insert_node_at_beginning(self,data):
        node = Node(data,self.head)
        self.head=node

    # insert node at the end...
    def insert_node_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        p= self.head
        while p.next:
            p=p.next
        node = Node(data,None)
        p.next=node

    # function to remove a node for given index...
    def remove_node_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        # check for head O(1)
        if index==0:
            self.head=self.head.next
            return

        count=0
        p=self.head
        while p.next:
            count+=1
            if count==index:
                p.next=p.next.next
                return
            p=p.next

    # function to insert nodes via a list
    def insert_nodes_via_list(self,data):
        self.head=None
        for d in data:
            self.insert_node_at_end(d)

    # remove by value
    def remove_by_value(self,data_value):
        p=self.head
        count=0
        while p:
            if p.data==data_value:
                self.remove_node_at(count)
                return
            count+=1
            p=p.next

    # insert data after a given value
    def insert_data_after_value(self,data_after,data_value):
        p = self.head
        count=0
        while p:
            if p.data==data_after:
                t=p.next
                p.next=Node(data_value,t)
                break
            count+=1
            p=p.next

    # insert node at a given index
    def insert_at_index(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index Value Inserted")
        if index==0:
            self.insert_node_at_beginning(data)
            return
        p =self.head
        count =1
        while p.next:
            if index==count:
                t=p.next
                p.next=Node(data,t)
                return
            count+=1
            p=p.next


if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_node_at_beginning(5)
    ll.insert_node_at_beginning(3)
    ll.print()
    print("Length Of Linked List : {}".format(ll.get_length()))
    ll.insert_node_at_end(10)
    ll.insert_node_at_end(50)
    ll.insert_node_at_beginning(1)
    ll.print()
    print("Length Of Linked List : {}".format(ll.get_length()))
    ll.remove_node_at(2)
    ll.print()
    ll.remove_node_at(3)
    ll.print()
    ll.remove_node_at(0)
    ll.print()
    print("Length Of Linked List : {}".format(ll.get_length()))
    ll.insert_nodes_via_list([1,2,3,4,5,6,7,8,9])
    ll.insert_node_at_end(45)
    ll.insert_node_at_beginning(89)
    ll.print()
    print("Length Of Linked List : {}".format(ll.get_length()))
    ll.remove_by_value(2)
    ll.remove_by_value(9)
    ll.remove_by_value(89)
    ll.remove_by_value(45)
    ll.print()
    print("Length Of Linked List : {}".format(ll.get_length()))
    ll.insert_data_after_value(5,10)
    ll.insert_data_after_value(8,100)
    ll.insert_data_after_value(1,123)
    ll.print()
    print("Length Of Linked List : {}".format(ll.get_length()))
    ll.insert_at_index(2,45)
    ll.print()
    ll.insert_at_index(10,200)
    ll.print()
    ll.insert_at_index(1, 20)
    ll.print()
    ll.insert_at_index(ll.get_length()-1, 1000)
    ll.print()
    print("Length Of Linked List : {}".format(ll.get_length()))





