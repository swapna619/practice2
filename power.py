import sys
def caluclate_power(base,exponent):
    """calculate power"""
    return base**exponent

if__name__="__main__"
print("power calculator")
try:
    if len(sys.argv)==3:
        base=float(sys.argv[1])
        exponent=float(sys.argv[2])
    else:
        base=float(input("enter the base value"))
        exponent=float(input("enter the base value"))
        result=caluclate_power(base,exponent)
        print(f"base=,{base}")
        print(f"exponent={exponent}")
        print(f"result={result}")
except ValueError:
    print("invalid input!enter numeric value")
        