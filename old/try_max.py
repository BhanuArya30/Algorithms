my_dict = {'a': 10, 'b': 30, 'c': 20}

max_key = max(my_dict)
print(max_key)  # Output: 'c'

max_key = max(my_dict, key=my_dict.get)
print(max_key)  # Output: 'b'