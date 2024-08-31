class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry = 0) -> ListNode:
        num = l1.val + l2.val + carry
        carry = num // 10
        final = ListNode(num % 10 ) 
        
        if (l1.next != None or l2.next != None or carry != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            final.next = self.addTwoNumbers(l1.next,l2.next,carry)
        return final