'''
stack/queue) 주식가격
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
-prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
-prices의 길이는 2 이상 100,000 이하입니다.

입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''
def solution(prices):
    '''my solution'''
    answer = [0] * len(prices)
    
    for idx, price in enumerate(prices):
        for i in range(idx+1, len(prices)):
            if price <= prices[i]:
                answer[idx] += 1
            else:
                answer[idx] += 1
                break
                
    return answer

'-----'
#큐 이용 코드 참고하기!
from collections import deque


def solution1(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))
    print(solution1([1, 2, 3, 2, 3]))
