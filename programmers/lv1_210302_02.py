def solution(new_id):
    #1
    new_id = new_id.lower()
    
    #2
    out_id = ""
    for s in new_id:
        if (45 <= ord(s) <= 46) or \
            (48 <=ord(s) <= 57) or \
            (ord(s) == 95) or \
            (97 <= ord(s) <= 122):
            out_id += s
    
    #3
    while True:
        if '..' in out_id:
            out_id = out_id.replace('..', '.')
        else:
            break
    
    #4
    out_id = out_id.lstrip('.')
    out_id = out_id.rstrip('.')
    
    #6
    if len(out_id) > 15:
        out_id = out_id[0:15]
    
    out_id = out_id.rstrip('.')
    
    #5
    if out_id == "":
        out_id += 'a'
        
    #7
    while len(out_id) < 3:
        out_id += out_id[-1]

    return out_id

'-------'

import re


def solution1(new_id):
    '''other solution'''
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

'----'

def solution2(new_id):
    '''other solution(similar to mine)'''
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer


if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution1("...!@BaT#*..y.abcdefghijklm"))
    print(solution2("...!@BaT#*..y.abcdefghijklm"))