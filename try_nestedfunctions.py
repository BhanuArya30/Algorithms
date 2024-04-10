def outer_function(x):
    print(f'outer::x is {x}')
    def inner_function(y):
        print(f'inner:x is {x} and y is {y}')
        return x + y
    return inner_function

closure = outer_function(10)

print(closure(5))  # Output: 15
