# https://leetcode.com/problems/reverse-linked-list-ii/submissions/
# https://www.youtube.com/watch?v=esl_A_pzBcg
# T: O(n)
# S: O(max(m, n))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        m_node, n_node = head, head
        pre_m = dummy
        
        for i in range(1, m):
            pre_m = m_node
            m_node = m_node.next
            
        for j in range(1, n):
            n_node = n_node.next
            
        while m_node != n_node:
            pre_m.next = m_node.next
            m_node.next = n_node.next
            n_node.next = m_node
            m_node = pre_m.next
            
        return dummy.next