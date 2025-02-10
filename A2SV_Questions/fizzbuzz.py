def FizzBuzz(n):
    print(F"N = {n}")
    # while True:
    if n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz") 
    else:
        print("None")
    
    


FizzBuzz(4)
FizzBuzz(15)
FizzBuzz(45)
FizzBuzz(3)