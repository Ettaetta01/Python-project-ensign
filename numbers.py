import math
while True:
 n=int(input("please enter a whole number :"))# check if number is even
 print(f" the number you entered is  {n}.")
 if n % 2==0:
  print(f"{n}s an even number.")
 # check if it has a square root
 sqr_n=math.sqrt(n)
 if int(sqr_n)==sqr_n :
    print(f"{n} has a perfect square root :")
 else :
    print(f"{n} does not have a perfect square root.")
    # find factors of a number
 factors=[]
 for i in range (1, n +1):
      if n % i==0:
        factors.append(i) 
 print(f"The factors of {n} are{factors}")
 decide=input("would you like to enter another number:").strip().lower()
 if decide!="Y":
   print("Thank you for playing")
 continue
 break


 
