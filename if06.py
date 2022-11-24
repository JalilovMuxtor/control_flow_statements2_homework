def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    
    x1=n%10
    n=n//10
    x2=n%10
    n=n//10
    x3=n%10
    n=n//10
    x4=n%10
    n=n//10
    x5=n//10
    
    if x1>x2 and x1>x3 and x1>x4 and x1>x5:
        return len(str(x1))
    elif x2>x1 and x2>x3 and x2>x4 and x2>x5:
        return len(str(x2*10+x1))
    elif x3>x1 and x3>x2 and x3>x4 and x3>x5:
        return len(str(x3*100+x1))
    elif x4>x1 and x4>x2 and x4>x3 and x4>x5:
        return len(str(x4*1000+x1))
    elif x5>x1 and x5>x2 and x5>x3 and x5>x4:
        return len(str(x5*10000+x1))
print(main(15342))