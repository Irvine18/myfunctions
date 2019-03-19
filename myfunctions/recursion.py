def sum_array(array):

    '''Return sum of all items in array.

    Args:
        items (array): list or array-type object containing numerical values.

    Returns:
        sum of all items in array.

    Examples:
        >>>> sum_array([3, 1, 5, 4])
        returns 13

    '''

    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence

    Args:
        n (int)

    Returns:
        nth term in fibonacci sequence.

    Examples:
        >>>> fibonacci(8)
        returns 21

    '''
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):

    '''Return n!

    Args:
        n (int)

    Returns:
        factorial of n.

    Examples:
        >>>> factorial(6)
        returns 720

    '''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):

    '''Return word in reverse
    Args:
        word (string)

    Returns:
        word in reverse order.

    Examples:
        >>>> 'Irvine'
        returns enivrI

    '''
    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]
