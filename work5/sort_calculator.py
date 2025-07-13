def customSort(numberList):
    if len(numberList) <= 1:
        return numberList 
    
    pivot = numberList[0] 
    left = []
    right = []
    for x in numberList[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    return customSort(left) + [pivot] + customSort(right)


def printSortedList(numberList):
    print ("sorted:", end=" ")
    for i in numberList:
        print(f"<{i}>", end=" ")

def main():
    try:
        numberInput = list(map(float, input("정렬할 수를 입력하세요").split()))
        if(len(numberInput) < 1):
            print("Invalid input. 입력된 수가 없습니다")
            return
        numberInput = customSort(numberInput)
        printSortedList(numberInput)
    except ValueError:
        print("Invalid input. 수 형식의 입력이 아닙니다.")
        return


if __name__ == "__main__":
    main()