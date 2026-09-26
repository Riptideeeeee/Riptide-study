/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *pa=headA,*pb=headB;
    while(pa!=pb){
        if (pa==NULL){
            pa=headB;
        }else{
            pa=pa->next;
        }
        if (pb==NULL){
            pb=headA;
        }else{
            pb=pb->next;
        }
    }
    return pa;
}
