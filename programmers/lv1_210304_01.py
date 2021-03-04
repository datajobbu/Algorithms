'''
약수의 합


'''

def solution(n):
    div_set = set()
    
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            div_set.add(n)
            div_set.add(i)

    answer = sum(div_set)
    return answer

'-----'

def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])