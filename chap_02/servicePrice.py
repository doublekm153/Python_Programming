#   서비스 가격 출력 프로그램.

price = [23, 40, 67]

for i in price:
    i * 1.1


def service_price():
    service = input('서비스의 종류를 입력하세요, a/b/c: ')
    valueAdded = input('부가세를 포함하나요? y/n: ')
    if valueAdded == 'y':
        if service == 'a':
            result = 23 * 1.1
        if service == 'b':
            result = 40 * 1.1
        if service == 'c':
            result = 67 * 1.1
    if valueAdded == 'n':
        if service == 'a':
            result = 23
        if service == 'b':
            result = 40
        if service == 'c':
            result = 67
    print(round(result, 1), '만원입니다.')
