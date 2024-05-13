def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()

def palindrome(a):
    mid=int(int(len(a))/2) 
    rev=-1 
    for b in range(0,mid+1): 
        if a[b]!=a[rev]:
            print("The string",a," is not a palindrome")
            break
        else:
            rev=rev-1 
    else:
        print("The string",a," is a palindrome")

def reverse(a):
    space()
    print("The reverse order is") 
    x=a.split()
    for d in x: 
        print(d[::-1],end=" ")

def present(a,c):
    space()
    x=a.split()
    f=c.split()
    for d in f: 
        if d not in x: 
            print("Absent") 
            break 
    else:
        print("Present")
    
    
def uncommon(a,c):
    space() #To make it look good
    x=a.split()
    f=c.split()
    for d in x:
        if d not in f:
            print(d) 

def rightrotation(a,d):
    x=a[-d:]
    b=x+a.rstrip(x) 
    print("The left Rotation is:",b) 

def leftrotation(a,d):
    x=a[0:d] 
    b=a.lstrip(x)+x 
    print("The right rotation is:",b)

choice=0

while choice!=6:
    print("Choose from the following option")
    print("1)For checking whether it is a palindrome")
    print("2)For printing the reverse of the string")
    print("3)For checking whether the string is present or not")
    print("4)For printing the uncommon words")
    print("5)For printing the right and left rotation")
    print("6)For exiting the code")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        space()
        a=str(input("Enter the string"))
        palindrome(a)
        space()
    
    elif choice==2:
        space()
        a=str(input("Enter the string"))
        reverse(a)
        space()
        
    elif choice==3:
        space()
        a=str(input("Enter the string Major"))
        c=str(input("Enter the string Minor"))
        present(a,c)
        space()
    
    elif choice==4:
        space()
        a=str(input("Enter the string Major"))
        c=str(input("Enter the string Minor"))
        uncommon(a,c)
        space()
        
    elif choice==5:
        space()
        a=str(input("Enter the string"))
        d=int(input("Enter the number"))
        rightrotation(a,d)
        leftrotation(a,d)
        space()



