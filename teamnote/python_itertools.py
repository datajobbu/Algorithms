'''
::코딩테스트 때 쓸만한 라이브러리 정리::
itertools - combinations(조합), permutations(순열)
    * use with map()

math - sqrt(제곱근 or ** 0.5), ceil(올림)
re(아마 문자열?) - sub()
'''
from itertools import combinations, permutations


ss = "PYTHON"

#순열: 경우의 수 모두
print(list(map(''.join, permutations(ss, 2))))
#조합: 중복되는 경우를 제외한 경우의 수
print(list(map(''.join, combinations(ss, 2))))

