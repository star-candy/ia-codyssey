def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0: # 0으로 나누는 경우 처리
        raise ValueError("Error: Division by zero.")
    return a / b

def precedence(op) -> int: #연산자 우선순위 처리
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0

def postfixEvaluate(postfix: list) -> float:
    evaluateStack = []
    for token in postfix:
        if isFloat(token): #isnumeric()는 정수형 숫자만 True 반환 문제 -> isFloat() 통해 ., - 처리 가능
            evaluateStack.append(float(token))
        elif isOperator(token):
            b = evaluateStack.pop()
            a = evaluateStack.pop()
            if token == '+':
                evaluateStack.append(add(a, b))
            elif token == '-':
                evaluateStack.append(subtract(a, b))
            elif token == '*':
                evaluateStack.append(multiply(a, b))
            else:
                evaluateStack.append(divide(a, b))
    
    if len(evaluateStack) != 1:
        raise ValueError("Invalid input: postfix 연산 중 스택에 남은 값이 1개가 아닙니다.")
    return evaluateStack.pop()  


def isOperator(op) -> bool:
    return op in ('+', '-', '*', '/')

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def infixToPostfix(token) -> list: 
    operatorStack = []
    postfixResult = []

    for t in token:
        if isFloat(t): #isnumeric()는 정수형 숫자만 True 반환 문제 -> isFloat() 통해 ., - 처리 가능
            postfixResult.append(t)
        elif t == '(':
            operatorStack.append(t)
        elif t == ')':
            while operatorStack[-1] != '(':
                postfixResult.append(operatorStack.pop())
            operatorStack.pop() # '(' 제거
        elif isOperator(t):
            while operatorStack and operatorStack[-1] != '(' and precedence(t) <= precedence(operatorStack[-1]):
                postfixResult.append(operatorStack.pop())
            operatorStack.append(t)

    while operatorStack: # 스택에 남아있는 연산자들을 모두 결과에 추가
        postfixResult.append(operatorStack.pop())

    return postfixResult

def main():
    try:
        token = input("수식을 입력하세요: ").split()
        if not token:
            raise ValueError("수식이 비어 있습니다.")
        postfixToken = infixToPostfix(token)
        result = postfixEvaluate(postfixToken)
        print(f"Result: {result}")

    except ValueError as e:
        print("Invalid input.")
        print(e)
        return

if __name__ == "__main__":
    main()