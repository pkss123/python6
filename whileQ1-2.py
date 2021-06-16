num = 0
sum = 0
add = int(input("몇의 배수 값의 총합을 구하시겠습니까?"))
while num <= 567:
    if num % add == 0:
        sum += num
    num += 1
print("0~567 사이의" + str(add)+"배수의 총합은 : "+str(sum))