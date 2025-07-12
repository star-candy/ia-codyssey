def main():
    try:
        numberList = list(map(float, input("Enter numbers: ").split()))
        numberList.sort()

        if(len(numberList) < 1):
            print("입력된 수가 없습니다.")
            return
        
        print(f"Min: {numberList[0]}, Max: {numberList[-1]}")
    except ValueError:
        print("수 형식의 입력이 아닙니다.")
        return

if __name__ == "__main__":
    main()