'''
캐시 - LRU

입력 형식
캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.

출력 형식
입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.

조건
- 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
- cache hit일 경우 실행시간은 1이다.
- cache miss일 경우 실행시간은 5이다.
'''
from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    answer = 0
    cities = list(map(str.lower, cities))
    queue = deque()
    
    for city in cities:
        if city in queue:
            answer += 1
            queue.remove(city)
        else:
            answer += 5
            if len(queue) >= cacheSize:
                queue.popleft()
        queue.append(city)
                
    return answer
