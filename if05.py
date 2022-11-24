def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n=12345
    if y<x1:
        y=x1
    if y<x2:
        y=x2
    elif y<x3:
        y=x3
    elif y<x4:
        y=x4
    elif y<x5:
        y=x5
    x1=n%10
    n=n//10
    x2=n%10
    n=n//10
    x3=n%10
    n=n//10
    x4=n%10
    n=n//10
    x5=n%10
    n=n//10
    y=n
    return(y)
print(main(12))
