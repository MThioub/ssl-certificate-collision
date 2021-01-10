import gmpy

def gcd(x, y):
    """
    return 0 if commoon divisor does ot exist
    and 1 else
    """
    cd = gmpy.gcd(x, y)
    print(cd)
    return cd == 1, cd
