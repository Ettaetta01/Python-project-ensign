import math # math module imported
while True: # to keep code running
 n=int(input("please enter a whole number :"))# check if number is even
 print(f" the number you entered is  {n}.")# prints out number
 if n % 2==0:# if user input can be divided by 2 without remainder
  print(f"{n}s an even number.")# then prints it is an even number
 # check if it has a square root
 sqr_n=math.sqrt(n)
 if int(sqr_n)==sqr_n : # comparing it with an integer form of the square root
    print(f"{n} has a perfect square root :")# print if it has a square root
 else :
    print(f"{n} does not have a perfect square root.")# prints if it dosent
    # find factors of a number
 factors=[]# creating list
 for i in range (1, n +1):
      if n % i==0:
        factors.append(i) 
 print(f"The factors of {n} are{factors}") # print factors of numbers
 decide=input("would you like to enter another number:").strip().lower()
 if decide!="Y":
   print("Thank you for playing")
 continue
 break


 
