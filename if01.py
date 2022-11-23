def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
        
    else:
        if b>c:
            print(b)
        else:
            print(c)
    
print(main(2,6,8))