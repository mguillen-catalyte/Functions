def reversed_string(response): 
    reversed_result = response[::-1]
    return reversed_result

entered_string = input("Please enter any word or sentence: ")
reversed_result = reversed_string(entered_string)
print(reversed_result)
