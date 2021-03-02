from itertools import permutations


#내 코드는 시간 초과

def solution(numbers):
    '''my solution'''
    answer = 0
    comb_set = set()
    comb_list = list()
    out = True
    
    for i in range(len(numbers)):
        comb_list = list(map(''.join, permutations(numbers, i+1)))
        for num in comb_list:
            if int(num) < 4:
                continue
            for i in range(2, int(num)):
                if int(num) % i == 0:
                    out = False
                    break
                else:
                    out = True
            if out:
                comb_set.add(int(num))

    
    return len(comb_set)

'------'
#other solution
def prime_check(a):
    if(a<=1):
        return False
    for n in range(2,a):
        if a % n == 0:
            return False
    return True

def solution1(numbers):
    val_set = set()
    for i in range(len(numbers), 0, -1):
        for val in list(map("".join, permutations(numbers, i))):
            if prime_check(int(val)) is True:
                val_set.add(int(val))
    
    return len(val_set)


if __name__ == "__main__":
    print(solution('017'))
    print(solution1('017'))