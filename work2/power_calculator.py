def power(base, exponent):
    result = 1.0
    for i in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1.0 / result
    
    if result.is_integer():
        return int(result)
    return result

def main():
    try:
        number_input = input("Enter number: ")
        number = float(number_input)
    except ValueError:
        print("Invalid number input.")
        return

    try:
        exponent_input = input("Enter exponent: ")
        exponent = int(exponent_input)
    except ValueError:
        print("Invalid exponent input.")
        return

    result = power(number, exponent)
    print("Result:", result)

if __name__ == "__main__":
    main()