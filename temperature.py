def convert_to_celsius(fahrenheit):
    '''(number) -> float

    Return the number in Celsius degrees equivalent of "fahrenheit" degrees.
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    '''
    return (fahrenheit - 32) * 5/9