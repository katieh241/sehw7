def fizz_buzz(i):
    if i%3 == 0 and i%5 == 0:
        str = "fizzbuzz"
        return str
    elif i%3 == 0:
        str = "fizz"
        return str
    elif i%5 == 0:
        str = "buzz"
        return str
    else:
        return i
    
    #now all numbers are converted to fizz, buzz, fizzbuzz or their original 
    #state based on whether or not they are divisible by 3, 5, both or neither. 
    #In order to fully implement this function, just create a for loop to print 
    #numbers 1-100, this testing just confirms that each number is converted correctly