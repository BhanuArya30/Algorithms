# Time O(n)
def is_palindrome(string:str)-> bool:
    begin = 0
    end = len(string) - 1
    
    if not string:
        return False

    if len(string) == 1:
        return True
    
    while begin < end:
        if string[begin] == string[end]:
            begin += 1
            end -= 1
        else:
            return False
    
    return True


my_string = "abc"#"abcd" #"abba"#"madam"
print(is_palindrome(my_string))