from LinkedList import SinglyLL

def cycleCheck(head):

    slow = head
    fast = slow.nextnode

    while fast and fast != slow:
        fast = fast.nextnode

        if fast and fast != slow:
            slow = slow.nextnode
            fast = fast.nextnode
        else:
            break


    if fast == slow:
        return True

    return False


llst = SinglyLL()
llst.insert(3)
llst.insert(4)
llst.insert(5)

#llst.head.nextnode.nextnode = llst.head


print(cycleCheck(llst.head))
