/*
链表相交
给你两个单链表的头节点headA和headB,请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回nNULL
*/






struct ListNode {
    int val;
    ListNode* next;
    ListNode(int data ): val(data),next(nullptr){}
};


//这个方法绝了，只需要让指针遍历完自己后去遍历另一个链表，这样如果指针没有相交，那么一定会在nullptr时相等推出
//因为指针跑过的路程都是1+2


class Solution{
public:
    ListNode*  getIntersectionNode(ListNode*head1,ListNode*head2){
        //特殊情况
        if (!head1||!head2 ) return nullptr;

        ListNode* p1 = head1;
        ListNode* p2 = head2;
        
        while(p1!= p2){
            p1 = p1? p1->next: head2;
            p2 = p2? p2->next :head1;
        }
        return p1;
    }
};