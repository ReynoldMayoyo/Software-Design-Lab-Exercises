def SecondToLastNode(head):
    temp =head
    if(temp ==None or temp.next==None):
        return-1
    while(temp !=None):
        if(temp.next.next==None):
            return temp.data
        temp =temp.next
