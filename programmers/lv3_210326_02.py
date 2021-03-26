'''
야근지수 - 힙

문제 설명
회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다. 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

제한 사항
- works는 길이 1 이상, 20,000 이하인 배열입니다.
- works의 원소는 50000 이하인 자연수입니다.
- n은 1,000,000 이하인 자연수입니다.
'''

# 효율성 실패 코드
def solution(n, works):
    for i in range(n):
        if max(works) == 0:
            return 0
        works = sorted(works)
        works[-1] = works[-1] - 1
    
    return sum([i ** 2 for i in works])

# 힙 구현으로 통과
import heapq


def solution(n, works):
    max_heap = []
    for item in works:
        heapq.heappush(max_heap, (-item, item))
    
    for i in range(n):
        max_value = heapq.heappop(max_heap)[1]
        if max_value == 0:
            return 0
        max_value -= 1
        heapq.heappush(max_heap, (-max_value, max_value))

    return sum(i[1] ** 2 for i in max_heap)
