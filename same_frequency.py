def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    result1 = {}
    result2 = {}

    for i in str(num1):
        result1[i] = result1.get(i, 0) + 1
    for x in str(num2):
        result2[x] = result2.get(x, 0) + 1

    return result1 == result2


    