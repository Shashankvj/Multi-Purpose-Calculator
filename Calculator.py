def main():

    print("""\nSelect Operation\n
1.Mathematical operations
2.BMI 
3.Temperature
4.Areas
5.Exit""")
    
    while True:
        cho=input("\nChoose a operation (1/2/3/4/5) :")
        if cho not in ('1', '2', '3', '4', '5'):
                 print("\nInvalid Choice")
                 continue
        else:
             break

    if cho =='1':
            math()

    if cho =='2':
            BMI()

    if cho =='3':
            temp()

    if cho =='4':
            area()

    if cho =='5':
            exit
        
def math():
    while True:
        try:
                    n1=input("Enter calculation you want : ") 
                    print("result",eval(n1))
                    break
        except Exception :
                    print("Number only")
    
    '''print("""\nSelect Operation\n
1.Addition
2.Subtraction
3.Multiply
4.Divide
5.Remainder""")

    while True:
        choice=input("\nChoose a Operation (1/2/3/4/5) : ")
        if choice not in ('1', '2', '3', '4', '5'):
                 print("\nInvalid Choice")
                 continue
        else:
            break

    while True:
            
            try:
                n1=float(input("\nEnter a Number: "))
                break
            except ValueError:
                print("Number only")

    while True:
             
             try:
                 n2=float(input("\nEnter another Number:"))
                 break
             except ValueError:
                 print("Number only")
   
    if choice =='1':
             print(n1,"+",n2,"=", float(n1)+float(n2))

    elif choice =='2':
             print(n1,"-",n2,"=",float(n1)-float(n2))

    elif choice =='3':
             print(n1,"*",n2,"=",float(n1)*float(n2))

    elif choice =='4':
             print(n1,"/",n2,"=",float(n1)/float(n2))

    elif choice =='5':
             print(n1,"%",n2,"=",float(n1)%float(n2))'''                     

    while True:
        say=input("\nLet's do next calculation? (yes/no) : ")
        if say not in ('yes', 'no'):
          print("\nInvalid choice")
          continue
        else:
            if say=='yes':
                math()
                break
            if say =="no":
                main()
                break

def BMI():
    
    while True:
        n3=input("\nEnter your weight in kg : ")
        try:
            n3=abs(float(n3))
            break
        except ValueError:
            print("Numbers only")

    while True:
        n4=input("\nEnter your height in cm : ") 
        try:
            n4=abs(float(n4))
            break
        except ValueError:
            print("Numbers only")  

    print("\nYour BMI is : ",float(n3)/((float(n4)*float(n4))/10000))

    while True:
             say=input("\nLet's do next calculation? (yes/no) : ")
            # say=say.strip()
             if say not in ('yes', 'no'):
                 print("\nInvalid choice")
                 continue
             else:
                if say=='yes':
                  BMI()
                  break
                if say =="no":
                  main()
                  break

def temp():

    print("""\nSelect operation\n
1.Fahrenheit to celsius
2.Celsius to fahrenheit""")

    while True:
        op=input("\nChoose a operation (1/2) :")
        if op not in ('1', '2'):
               print("\nInvalid Choice")
               continue
        else:
            break

    if op=='1':

           while True:
               n5=input("\nEnter Fahrenheit : ")
               try:
                   n5=float(n5)
                   break
               except ValueError:
                   print("Numbers only")

           print("\nCelsius will be : ",((float(n5)-32)*5)/9)      
       
    if op=='2':

           while True:
               n6=input("\nEnter Celsius : ")
               try:
                   n6=float(n6)
                   break
               except ValueError:
                   print("Numbers only")

           print("\nFahrenheit will be : ",(float(n6)*1.8)+32)

    while True:
        say=input("\nLet's do next calculation? (yes/no) : ")
        if say not in ('yes', 'no'):
          print("\nInvalid choice")
          continue
        else:
            if say=='yes':
                temp()
                break
            if say =="no":
                main()
                break          
    
def area ():

    print("""\nSelect Operation\n
1.Rectangle
2.Square
3.Triangle
4.circle
5.Parallelogram""")

    while True:
        ar=input("\nChoose a operation (1/2/3/4/5) :")
        if ar not in ('1', '2', '3', '4', '5'):
                 print("\nInvalid Choice")
                 continue
        else:
            break

    if ar=='1':

         while True:
             n7=input("\nEnter Length:")
             try:
                 n7=abs(float(n7))
                 break
             except ValueError:
                 print("Numbers only")

         while True:
             n8=input("\nEnter Breadth:")
             try:
                 n8=abs(float(n8))
                 break
             except ValueError:
                 print("Numbers only")
                 
         print("\nArea will be : ",float(n7)*float(n8))
   
    if ar=='2':

         while True:
             a1=input("\nEnter Side:")
             try:
                 a1=abs(float(a1))
                 break
             except ValueError:
                 print("Numbers only")
                 
         print("\nArea will be : ",float(a1)*float(a1))
            
    if ar=='3':

         while True:
             a2=input("\nEnter Height:")
             try:
                 a2=abs(float(a2))
                 break
             except ValueError:
                 print("Numbers only")
                 
         while True:
             a3=input("\nEnter Base:")
             try:
                 a3=abs(float(a3))
                 break
             except ValueError:
                 print("Numbers only")
                 
         print("\nArea will be : ",(float(a2)*float(a3))/2)
           
    if ar=='4':

         while True:
             a4=input("\nEnter Radius:")
             try:
                 a4=abs(float(a4))
                 break
             except ValueError:
                 print("Numbers only")
                 
         print("\nArea will be : ",3.14*(float(a4)*float(a4)))
         
    if ar=='5':

         while True:
             a5=input("\nEnter Height:")
             try:
                 a5=abs(float(a5))
                 break
             except ValueError:
                 print("Numbers only")
                 
         while True:
             a6=input("\nEnter Base:")
             try:
                 a6=abs(float(a6))
                 break
             except ValueError:
                 print("Numbers only")
                 
         print("\nArea will be : ",float(a5)*float(a6))

    while True:
        say=input("\nLet's do next calculation? (yes/no) : ")
        if say not in ('yes', 'no'):
          print("\nInvalid choice")
          continue
        else:
            if say=='yes':
                area()
                break
            if say =="no":
                main()
                break

main()
print("\nI Love You")
print("Neha")



