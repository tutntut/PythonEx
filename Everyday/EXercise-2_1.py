def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(10,20,30,40))

#튜플의 임의 변수 표현 * 는 굉장히 많이 사용 !!!!!!!!!
'''
def concat(*name, gubun='/'):
    return gubun.join(name)

concat("하나", "둘", "셋")
concat("하나", '둘', '셋', gubun=';')

결과 :
하나/둘/셋
하나;둘;셋
'''