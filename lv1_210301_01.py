'''
두 개 뽑아서 더하기

정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 
두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 
배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
-numbers의 길이는 2 이상 100 이하입니다.
  -numbers의 모든 수는 0 이상 100 이하입니다.

예시
| numbers |  result   |
|---------|-----------|
|[5,0,2,7]|[2,5,7,9,12]
'''
def solution(numbers):
    '''my solution'''
    sum_list = []

    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            sum_list.append(numbers[i] + numbers[j])

    sum_list = list(set(sum_list))
    answer = sorted(sum_list)

    return answer

'----'

from itertools import combinations


def solution1(numbers):
    '''other solution'''
    answer = []
    comb_list = list(combinations(numbers, 2))

    for i in comb_list:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer


if __name__=="__main__":
    print(solution([5, 0, 2, 7]))
    print(solution1([5, 0, 2, 7]))