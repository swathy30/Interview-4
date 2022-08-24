#TC : O(n)
#SC : O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid= self.midpoint(head)
        mid_nxt= mid.next
        #mid_nxt= None
        newreverse= self.reverse(mid_nxt)
        return self.check(head,newreverse)
        
    def reverse(self,head):
        prev= None
        curr= head
        while curr:
            temp= curr.next
            curr.next= prev
            prev = curr
            curr = temp
        return prev
    
    def midpoint(self,head):
        slow= head
        fast= head
        while fast.next!= None and fast.next.next!= None: #to check for both odd and even number of nodes
            slow= slow.next
            fast= fast.next.next
        return slow
    
    def check(self,head1,head2):
        p1=head1
        p2=head2
        while p2:
            if p1.val==p2.val:
                p1= p1.next
                p2=p2.next
            else:
                return False
        return True
    