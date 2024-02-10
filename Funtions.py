def is_palindrome(word): 
    #Make function case-insensitive
    word = word.lower()
    #Return reversed string
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
#        print(f"The word {word} is a palindrome!")
    else: 
        return False
#        print(f"The word {word} is not a palindrome.")
print(is_palindrome("ak"))

# Find square root of a number 
def calculate_sqrt(n):
    # We have to start with 0 because we are interested in non-negative values
    start = 0
    # And end with n because the search algorithm should vary between this interval
    end = n
    while start <= end:
        mid = (start + end) // 2
        #if middle number multiplied by itself is equal to number entered by user, return middle number
        if mid*mid == n:
            return mid
        """if middle number is less than the number entered by user, add 1 to the value so that it will continue 
        searching value to the right side"""
        if mid*mid < n:
            start = mid + 1
        else:
            end = mid - 1
    return start - 1
user_num = int(input("Enter a number: "))
if user_num<0:
    print("Please, enter a non negative number")
else:
    print(f"sqrt({user_num}) = {calculate_sqrt(user_num)}")


#Function to find prime numbers in a range x1 and x2
def find_primes(x1, x2):
    for i in range(x1, x2):
        #0 and 1 is not considered as a prime number, so we have to declare it as a condition
        if i == 0 or i == 1:
            print(i, "is not a prime number")
        else:
            #find prime numbers in x1, x2 interval with for loop to iterate through it 
            for num in range(2, i):
                # and terminate the function is the remainder is equal to 0, because prime numbers never have zeroes as a remainder
                if (i % num) == 0: 
                    break
            else:
                print(i, "is a prime number")
find_primes(1,18)
