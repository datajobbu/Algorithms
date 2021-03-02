'''
카펫

제한사항
-갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
-노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
-카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

입출력 예
brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
'''

def solution(brown, yellow):
    divisor = brown + yellow
    answer_list = []
    
    for i in range(1, divisor + 1):
        if divisor % i == 0:
            answer_list.append([divisor // i, i])

    for answers in answer_list:
        if answers[0] >= answers[1]:
            if (answers[0] - 2) * (answers[1] - 2) == yellow:
                answer = answers
            
    return answer

'--------'

import math


def solution1(brown, yellow):
    '''other solution'''
    ans=((brown-4)+math.sqrt((brown-4)**2-16*yellow))//4
    return [ans+2, yellow//ans+2]


if __name__ == "__main__":
    print(solution(10, 2))
    print(solution1(10, 2))