import gmpy 

def gcd(x, y):
    """
    return 0 if commoon divisor does ot exist
    and 1 else
    """
    return (gmpy.gcd(x, y) != 1) * 1
