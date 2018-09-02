# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3
# 설계
# 1. 문자열 전부 소문자로 변환
# 2. 공백 기준 배열로 변환
# 3. 첫 글자를 대문자로 변환하는 로직
# 3-1. 배열 별 첫 글자가 영문이면 대문자로 변환 (정규표현식 사용)
# 3-2. 영문이 아니면 다음 글자로 넘어가서 검사.

import re
import unittest


# 첫 글자 대문자로 변환
def convertStr(str):
    p = re.compile('[a-z]+')
    if bool(p.match(str[0])):
        str = str.replace(str[0], str[0].upper(), 1)

    return str


def solution(s):
    lower = s.lower()
    sliced = lower.split()
    result = []

    for temp in sliced:
        result.append(convertStr(temp))

    return " ".join(result)


# 테스트 케이스
class Test(unittest.TestCase):

    def test(self):
        self.assertEquals("3people Unfollowed Me", solution("3people unFollowed me"))
        self.assertEquals("For The Last Week", solution("for the last week"))


if __name__ == '__main__':
    unittest.main()
