num = int(input("정수를 입력하세요 : "))

if num == 0:
    print("입력하신 숫자는 0입니다")
elif num % 5 == 0:
    print("입력하신 숫자는 5의 배수입니다")
else:
    print("입력하신 숫자는 5의 배수가 아닙니다")