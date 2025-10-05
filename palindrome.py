def palindrome(num):
    last_position = len(num)-1
    starting_position = 0
    
    while starting_position<last_position:
        if num[starting_position]!=num[last_position]:
            return False
        starting_position += 1
        last_position -= 1
        return True
num = (1, 2, 3, 3, 2, 1)
if (palindrome(num)):
    print(num, "is a flip flop tuple")
else:
    print(num, "is not a flip flop tuple")

    

