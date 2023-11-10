"""
factorial =1
rest = True
while rest:
    try:
        num = int(input("Enter a number :"))
        if num <= 0:
            print("Enter a number more than 1")
        else:
            for i in range(1,num+1):
                factorial =factorial*i
            print(f"Your number is {num}\n your factorial is {factorial}")

            choose = input("do you want to play again :").lower()
            if choose =="no":
                rest =False


    except:
        ValueError
"""

while True:
    try:
        n =int(input( "Enter number: "))
        def recur_fact(n):
            if n<=0:
                print("enter a integer greater than 1")
                return n
            else:
                return n*recur_fact(n-1)

    except:
        ValueError


