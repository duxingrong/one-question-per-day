/*
删除链表中倒数第N个节点

给你一个链表，删除链表中的倒数第n个节点，并返回链表的头节点

*/

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int data): val(data) , next(nullptr) {}
};

class Solution{
public:
    ListNode* removeNthFromEnd(ListNode*head, int n){
        //要删除倒数第几个，fast就比slow多走几步
        ListNode *dummy_head = new ListNode(0);
        dummy_head->next = head;
        ListNode*slow = dummy_head;
        ListNode*fast = dummy_head;
        for(int i=0;i<n;i++){
            fast = fast->next;
        }
        while (fast->next != nullptr){//直到fast走到链表末尾
            fast = fast->next;
            slow = slow->next;
        }
        //找到位置后开始删除
        slow->next = slow->next->next;
        return dummy_head->next;
    }
};
