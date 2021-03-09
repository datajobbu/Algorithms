'''
소수찾기(lv 1) - 에라토스테네스의 체

문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
'''
def solution(n):
    prime = [True] * (n + 1)
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i] == True:
            for j in range(2 * i, n + 1, i):
                prime[j] = False
    
    return len([k for k in range(2, n + 1) if prime[k] == True])

print(solution(10))
print(solution(5))