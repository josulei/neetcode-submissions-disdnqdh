struct listnode{
    listnode(int value, listnode* next = nullptr) : value(value), next(next) {}
    int value; 
    listnode * next; 
};

class LinkedList {
public:
    LinkedList() {
        head = nullptr; 
        tail = nullptr; 
    }

    int get(int index) {
        int val = -1; 
        if(index >= 0){
            listnode * curr = head;
            while(curr != nullptr && index > 0){
                curr = curr -> next; 
                index--;
            }
            if(curr != nullptr){
                val = curr->value; 
            }
        }
        return val; 
    }

    void insertHead(int val) {
        if(head == nullptr){
            head = new listnode(val);
            tail = head; 
            
        }else{
            listnode * newNode = new listnode(val, head); 
            head = newNode;
        }
    }
    
    void insertTail(int val) {
        if(tail == nullptr){
            tail = new listnode(val);
            head = tail; 
        }else{
            listnode *newNode = new listnode(val);
            tail->next = newNode; 
            tail = newNode; 
        }
    }

    bool remove(int index) {
        if(index < 0 || head == nullptr){
            return false; 
        }
        if(index == 0){
            head = head->next;
            if(head == nullptr){
                tail = nullptr; 
            }
            return true;
        }

        listnode * curr = head; 
        int currIndex = 0; 
        while(curr->next != nullptr && currIndex < index - 1){
            curr = curr->next; 
            currIndex++; 
        }
        if(curr->next == nullptr){
            return false; 
        }
        if(curr->next == tail){
            tail = curr; 
        }
        listnode* toDelete = curr->next;
        curr->next = curr->next->next;
        delete toDelete;
        return true; 
    }

    vector<int> getValues() {
        vector<int> values; 
        listnode * curr = head; 
        while(curr!=nullptr){
            values.push_back(curr->value);
            curr = curr->next; 
        }
        return values; 
    }

    ~LinkedList(){
        clear();
    }
    
    void clear(){
        clearHelper(head);
    }


private: 
    listnode * head; 
    listnode * tail; 

    void clearHelper(listnode*curr){
        if(curr == nullptr){
            return;
        }
        clearHelper(curr->next);
        delete curr;
    }
};
