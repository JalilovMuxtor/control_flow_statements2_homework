def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    
    n1=n%10
    n=n//10

    n2=n%10
    n=n//10

    n3=n%10
    n=n//10

    n4=n%10
    n=n//10

    n5=n
    return n1,n2,n3,n4,n5
print(main(56892))