/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    int len=0;
    struct ListNode *temp=head;
    while(temp!=NULL){
        temp=temp->next;
        len++;
    }
    temp=head;
    int new_list[len];
    for ( int i =0;i<len;i++){
        new_list[i]=temp->val;
        temp=temp->next;
    }
    for ( int j =0;j<(len/2);j++){
        if(new_list[j]!=new_list[len-j-1]){
            return false;
        }
    }
    return true;
}
