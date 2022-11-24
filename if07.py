def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if temp<10:
        print('juda sovuq')
    if temp<20:
        print('sovuq')
    elif temp<30:
        print('issq')
    elif temp<40:
        print('juda issiq')
    return temp
print(main(36))