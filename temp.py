#!/usr/bin/python
# -*- coding:UTF-8 -*-

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        self.next = head

        # 如果k=1,返回原列表
        if k == 1:
            return self.next

        # 定义一个判断剩余节点是否大于等于k个的函数
        def long_than_k(node, k):
            if node == None:
                return False
            for i in range(k - 1):
                next_node = node.next
                if next_node != None:
                    node = next_node
                    continue
                else:
                    return False
            return True

        # 由于k是动态的，则不能定义k+2个变量来保存他们，可以利用列表，列表长度是k+2，可用通过遍历列表的方式来动态去取得临时保存中间值的变量


        temp_li = [None for i in range(k + 2)]
        pre, pre.next = self, head
        while long_than_k(pre.next, k):
            temp_li[0] = pre
            for i in range(k + 1):
                temp_li[i + 1] = temp_li[i].next

            temp_li[0].next = temp_li[k]
            for i in range(6, 1, -1):
                temp_li[i].next = temp_li[i - 1]

            temp_li[1].next = temp_li[k + 1]

        return self.next
