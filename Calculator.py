def main():

    print("""\nSelect Operation\n
1.Mathematical operations
2.BMI 
3.Temperature
4.Areas
5.Factorial
6.Exit""")
    
    while True:

        cho=input("\nChoose a operation (1/2/3/4/5/6) :")
        cho=cho.strip()

        if cho not in ('1', '2', '3', '4', '5', '6'):
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
            factorial()

    if cho =='6':
            exit
        
def math():

    while True:

        try:
                n1=input("Enter calculation you want : ")
                n1=n1.strip()
                print("result",eval(n1))
                break
        except Exception :
                print("Number only")
    
    
    while True:

        say=input("\nLet's do next calculation? (yes/no) : ")
        say=say.strip()

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
        
        try:
            n3=abs(float(input("\nEnter your weight in kg : ")))
            break
        except Exception:
            print("Numbers only")

    while True:

        try:
            n4=abs(float(input("\nEnter your height in cm : ")))
            break
        except Exception:
            print("Numbers only")  

    print("\nYour BMI is : ",(n3)/(((n4)*(n4))/10000))

    while True:

             say=input("\nLet's do next calculation? (yes/no) : ")
             say=say.strip()

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
        op=op.strip()

        if op not in ('1', '2'):
               print("\nInvalid Choice")
               continue

        else:
            break

    if op=='1':

           while True:

               try:
                   n5=float(input("\nEnter Fahrenheit : "))
                   print("\nCelsius will be : ",(((n5)-32)*5)/9)
                   break
               except Exception:
                   print("Numbers only")

    if op=='2':

           while True:

               try:
                   n6=float(input("\nEnter Celsius : "))
                   print("\nFahrenheit will be : ",((n6)*1.8)+32)
                   break
               except Exception:
                   print("Numbers only")

    while True:

        say=input("\nLet's do next calculation? (yes/no) : ")
        say=say.strip()

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
        ar=ar.strip()

        if ar not in ('1', '2', '3', '4', '5'):
                 print("\nInvalid Choice")
                 continue

        else:
            break

    if ar=='1':

         while True:

             try:
                 n7=abs(float(input("\nEnter Length:")))
                 break
             except Exception:
                 print("Numbers only")

         while True:

             try:
                 n8=abs(float(input("\nEnter Breadth:")))
                 break
             except Exception:
                 print("Numbers only")
                 
         print("\nArea will be : ",(n7)*(n8))
   
    if ar=='2':

         while True:

             try:
                 a1=abs(float(input("\nEnter Side:")))
                 print("\nArea will be : ",(a1)*(a1))
                 break
             except Exception:
                 print("Numbers only")
                 
    if ar=='3':

         while True:

             try:
                 a2=abs(float(input("\nEnter Height:")))
                 break
             except Exception:
                 print("Numbers only")
                 
         while True:

             try:
                 a3=abs(float(input("\nEnter Base:")))
                 break
             except Exception:
                 print("Numbers only")
                 
         print("\nArea will be : ",((a2)*(a3))/2)
           
    if ar=='4':

         while True:

             try:
                 a4=abs(float(input("\nEnter Radius:")))
                 print("\nArea will be : ",3.14*((a4)*(a4)))
                 break
             except Exception:
                 print("Numbers only")
                 
    if ar=='5':

         while True:

             try:
                 a5=abs(float(input("\nEnter Height:")))
                 break
             except Exception:
                 print("Numbers only")
                 
         while True:

             try:
                 a6=abs(float(input("\nEnter Base:")))
                 break
             except Exception:
                 print("Numbers only")
                 
         print("\nArea will be : ",(a5)*(a6))

    while True:
     
        say=input("\nLet's do next calculation? (yes/no) : ")
        say=say.strip()
       
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

def factorial():

        m=0
        fac=0
        k=0
       
        while True:

             try:
                 fa=float(input("Enter a number"))
                 k=fa
                 break
             except Exception:
                 print("Numbers only")

        while True:
                     m=k-1
                     fac=m*k
                     if fa=='0':
                         print("\nFactorial of",fa,"is",fac)
                         break
                     
main()
print("\nI Love You")




