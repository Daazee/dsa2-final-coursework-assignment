def isPalindrome(text_to_check):

    if(text_to_check == ""): #best case. empty string is considered as a palindrome
        return True
    elif (len(text_to_check) <= 1): #best case. a single character is considered as a palindrome
        return True
    else:
        first_character =  text_to_check[0] # take the first character
        last_character =  text_to_check[len(text_to_check) - 1] # take the last character
        if(first_character != last_character): #return false if both first and last character are not the same
            return False
        else:
            text_to_check = text_to_check.replace(text_to_check[0], "", 1) #remove the first character before performing the next recursion
            text_to_check = text_to_check.replace(text_to_check[len(text_to_check)-1], "", 1) #remove the last character before performing the next recursion


    return isPalindrome(text_to_check) #recursively call isPalindrome function if the length of the text is greater than 1



my_text = input("Please enter a word to check if it is a palindrome: ")

result = isPalindrome(my_text)
print(result)