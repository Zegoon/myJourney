toDo=["Fill water tanks","Buy Bananas","Wash Car"]

pickedOption=int()
page=int()

def userPickOptions():
    global page
    print("""Please enter an option
        1.Show list
            
        2. Add to list

        3. Remove from list

        4. Count to-do's
        """)
    pickedOption=int(input(": "))
    if pickedOption==1:
        page=1
        return
    if pickedOption==2:
        page=2
        return
    if pickedOption==3:
        page=3
        return
    if pickedOption==4:
        page=4
        return


while True:
    if __name__=='__main__':
        userPickOptions()
        if page==1:
            print(toDo)
        elif page==2:
            toDo.append(input("Enter: "))
            print(toDo)
        elif page==3:
            toDo.remove(input("Enter the item to remove: "))
            print(toDo)
        elif page==4:
            print(toDo.count)
        else:
            pass



        

        
        