# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge_sort(l,length):
            if length==1:
                return l
            
            r = l
            middle = length//2
            for _ in range(middle):
                r = r.next
            
            merge_sort(l,middle)
            merge_sort(r,middle)
            
            l_parent,r_parent = l,r
            head = l
            # while r and l != r:
            for i in range(5):
                print(l.val,r.val)
                if l.val > r.val:
                    r_parent.next = r.next
                    l_parent.next = r
                    r.next = l
                    r = r_parent.next
                l_parent = l
                l = l.next
            print("retrn")
            return head
        
        length = 0
        left = head
        while head:
            head = head.next
            length += 1
        return merge_sort(left,length)
        """
        l     r 
        1 3 5 2 4 6
          l   r 
        1 3 5 2 4 6
            l   r
        1 2 3 5 4 6 
              l r
        1 2 3 5 4 6 
                l r
        1 2 3 4 5 6 
                  lr
        1 2 3 4 5 6 
        """
            
        