def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b:
        if a<c:
            print(a)
        else:
            print(c)
        
    else:
        if b<c:
            print(b)
        else:
            print(c)
    return 'javobi'
print(main(2,6,3))