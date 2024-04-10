def add(a:int, b:int)-> int:
    """
    Function to add two numbers

    Examples:
    >>> add(2, 3)
    5

    >>> add(3, -4)
    -1
    """
    return a + b

if __name__== "__main__":
    import doctest
    doctest.testmod()