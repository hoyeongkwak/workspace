for i in range(10):
    try:
        result = 10/i
    except ZeroDivisionError:
        print('숫자는 0으로 나눌 수 없습니다')

    else:
        print('result:',result)

    finally:
        print('한 번 연산 종료')
