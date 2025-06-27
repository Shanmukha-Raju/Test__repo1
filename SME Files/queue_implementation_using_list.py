class queue:
    def __init__(self,list):
        self._list = list
    def enqueue(self,n):
        self._list.append(n)
    def dequeue(self):
        return self._list.pop(0)
    def front(self):
        return self._list[0]
list1=queue([1,2,3,4,5])
while True:
   starting=input("enter 1 to start the program or 0 to exit the program:")
   if starting=="1":
    operation=int(input("enter 1 for enqueue or enter dequeue for pop or enter 3 for front :"))
    if operation==1:
      push_element=int(input("element to be added at the rear:"))
      list1.enqueue(push_element)
      print(f"element {push_element} added at the rear")
    if operation==2:
      print(f"element deleted from the front:{list1.dequeue()}")
    if operation==3:
      print(f"the front element on the queue:{list1.front()}")
   elif starting=="0":
    print("terminated the program")
    break
   else:
     print("invalid input by default exiting the program")
     break
