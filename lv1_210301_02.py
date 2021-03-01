'''
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
-시험은 최대 10,000 문제로 구성되어있습니다.
-문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
-가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3
'''
def solution(answers):
    '''MY SOLUTION'''
    supo1 = [1, 2, 3, 4, 5]
    supo1 = supo1 * (len(answers) // 5) + supo1[:(len(answers) % 5)]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo2 = supo2 * (len(answers) // 8) + supo2[:(len(answers) % 8)]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supo3 = supo3 * (len(answers) // 10) + supo3[:(len(answers) % 10)]
    supo1_cnt = 0
    supo2_cnt = 0
    supo3_cnt = 0
    
    for i in range(len(answers)):
        if answers[i] == supo1[i]:
            supo1_cnt += 1
        if answers[i] == supo2[i]:
            supo2_cnt += 1
        if answers[i] == supo3[i]:
            supo3_cnt += 1
            
    cnt_list = [supo1_cnt, supo2_cnt, supo3_cnt]
    answer = []
    for i in range(len(cnt_list)):
        if cnt_list[i] == max(cnt_list):
            answer.append(i + 1)

    return answer

'-----'

def solution1(answers):
    '''other solution'''
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


if __name__ == "__main__":
    print(solution([3,2,3,4,1,2,3,4,1,2,3,3,2,1,5,4,2]))
    print(solution1([3,2,3,4,1,2,3,4,1,2,3,3,2,1,5,4,2]))