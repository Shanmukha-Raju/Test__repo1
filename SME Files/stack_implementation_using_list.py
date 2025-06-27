class stack:
    def __init__(self,list):
        self._list = list
    def push(self,n):
        self._list.append(n)
    def pop(self):
        return self._list.pop()
    def peek(self):
        return self._list[-1]
list1=stack([1,2,3,4,5])
while True:
   starting=input("enter 1 to start the program or 0 to exit the program:")
   if starting=="1":
    operation=int(input("enter 1 for push or enter 2 for pop or enter 3 for peek :"))
    if operation==1:
      push_element=int(input("element to be added upon the stack:"))
      list1.push(push_element)
      print(f"element {push_element} added at the top")
    if operation==2:
      print(f"element deleted from the top:{list1.pop()}")
    if operation==3:
      print(f"the top most element on the stack:{list1.peek()}")
   elif starting=="0":
    print("terminated the program")
    break
   else:
     print("invalid input by default exiting the program")
     break
