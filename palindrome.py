def isPalindrome(text_to_check):

    if(text_to_check == ""):
        return True
    elif (len(text_to_check) <= 1):
        return True
    else:
        first_character =  text_to_check[0]
        last_character =  text_to_check[len(text_to_check) - 1]
        if(first_character != last_character):
            return False
        else:
            text_to_check = text_to_check.replace(text_to_check[0], "", 1)
            text_to_check = text_to_check.replace(text_to_check[len(text_to_check)-1], "", 1)


    return isPalindrome(text_to_check)



my_text = input("Please enter a word to check if it is a palindrome: ")

result = isPalindrome(my_text)
print(result)