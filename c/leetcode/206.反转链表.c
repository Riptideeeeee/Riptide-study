/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* new_node=NULL;
    while(head!=NULL){
        struct ListNode *temp=head->next;
        head->next=new_node;
        new_node=head;
        head=temp;
    }
    return new_node;
}
