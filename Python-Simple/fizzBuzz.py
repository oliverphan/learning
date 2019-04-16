fizzbuzz = "FizzBuzz"
fizz = "Fizz"
buzz = "Buzz"

def fizz_buzz1():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def fizz_buzz2(): #Note how any number divisble by 3 and 5 is divisble by 15!
    for i in range(1, 101):
        if i % 15 == 0:
            print(fizzbuzz + " " + str(i))
        elif i % 3 == 0:
            print(fizz + " " + str(i))
        elif i % 5 == 0:
            print(buzz + " " + str(i))
        else:
            print(i)

def fizz_buzz3(): #We don't need a special case for fizzbuzz, maybe we print both
    for i in range(1, 101):
        output = "" #The most elegant compared to before
        if i % 3 == 0:
            output += fizz
        if i % 5 == 0:
            output += buzz
        if len(output) == 0:
            output = i
        print(output)

                  
if __name__ == '__main__':
    fizz_buzz3()
#80% in stocks and 20% in bonds
#Let's say S&P 500 got a 37% loss with treasuries gained 5%, so that your mix would now be 70% stocks 30% bonds
