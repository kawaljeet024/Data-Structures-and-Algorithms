class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    # def print_list(self):
    #cur_node = self.head
    # while cur_node:
        # print(cur_node.data)
        #cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head

        sum_llist = Linkedlist()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = i.data
            if not q:
                j = 0
            else:
                j = j.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
            sum_llist.print_list()


llist1 = Linkedlist()
llist1.append(2)
llist1.append(4)
llist1.append(3)

llist2 = Linkedlist()
llist2.append(5)
llist2.append(6)
llist2.append(4)
print(243 + 564)
#llist1.sum_two_lists(llist2)
