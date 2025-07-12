def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0: # 0으로 나누는 경우 처리
        return "Error: Division by zero."
    return a / b

def evaluate_expression(expression):
    try:
        parts = expression.strip().split() # string input split by space
        if len(parts) != 3: # 보너스 과제 요구사항 (2 숫자와 1 연산자)
            return "Invalid expression format. Use: number operator number"
        
        a_str, operator, b_str = parts
        a = float(a_str) # 보너스 과제 예시에 따르면 결과가 실수 형태로 출력됨 확인
        b = float(b_str) # 이에 따라 보너스 형식은 실수형으로 변환 및 처리함

        if operator == "+":
            return add(a, b)
        elif operator == "-":
            return subtract(a, b)
        elif operator == "*":
            return multiply(a, b)
        elif operator == "/":
            return divide(a, b)
        else:
            return "Invalid operator."
    except ValueError:
        return "Invalid numbers. Please enter valid numeric values."

if __name__ == "__main__":
    mode = input("Choose mode (1: manual inputs, 2: expression): ")

    if mode == "1": # 수동 입력 모드 (기본 과제 입력 방식)
        try:
            a = int(input("Enter the first number: ")) # 입력 숫자는 반드시 int로 변환할 것
            b = int(input("Enter the second number: "))
            operator = input("Enter operator (+, -, *, /): ")

            if operator == "+":
                result = add(a, b)
            elif operator == "-":
                result = subtract(a, b)
            elif operator == "*":
                result = multiply(a, b)
            elif operator == "/":
                result = divide(a, b)
            else:
                result = "Invalid operator."

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input: Please enter integers only.")

    elif mode == "2": # 수식 입력 모드 (보너스 과제 입력 방식)
        expression = input("Enter expression: ")  # e.g., "2 + 3"
        result = evaluate_expression(expression)
        print(f"Result: {result}")

    else:
        print("Invalid mode selected.")

