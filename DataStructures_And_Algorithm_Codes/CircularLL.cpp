#include<iostream>
using namespace std;

class Node{
    public:
    int data;
    Node*next;

    ///constructor
public:
    Node()
    {
        next=NULL;

    }
    Node(int data)
    {
        this->data=data;
        this->next=NULL;

    }

};

class CircularLL
{
    Node*head;
   /// Node*tail;
    int Size;

public:
    ///constructor
    CircularLL()
    {
       head=NULL;
      /// tail=NULL;
       Size=0;

    }
    void Insert(int data)
    {
        Node*newNode=new Node(data);
        Size++;
        if(head==NULL)
        {
            head=newNode;
        }
       Node*temp;
       while(temp->next!head)
       {
           temp=temp->next;
       }
       temp->next=newNode;
       newNode->next=head;
       head=newNode;

    }
    void Delete(int pos)
    {
    }
    bool isEmpty()
    {
        return Size==0;

    }
    int getSize()
    {
        return Size;

    }
    void print()
    {
        if(!head) return;
        Node*temp=head;
        while(temp->next!=head)
        {
            cout<<temp->data<<" ";
            temp=temp->next;
        }
        cout<<endl;
        return;
    }
};
int main()
{
    CircularLL myLL;
    myLL.Insert(10);
    myLL.Insert(20);
    myLL.Insert(100);
    myLL.Insert(30);
    myLL.Insert(60);
     myLL.print();
    myLL.Delete(2);
    myLL.Delete(1);
    myLL.print();


}
