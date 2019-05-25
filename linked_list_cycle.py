def hasCycle1(head):
    s = set()
    while head is not None:
        if head in s: return True
        s.add(head)
        head = head.next
    return False
    
def hasCycle1(head):
    if head is None or head.next is None: return False
    ptr1 = head
    ptr2 = head.next
    while ptr1 != ptr2:
        if ptr2.next is None or ptr2.next.next is None: return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
    return True
    
def hasCycle1(head):
    try: #faster to catch exception than to check everytime
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False