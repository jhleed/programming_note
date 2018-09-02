# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3
# 설계
# 1. 문자열 전부 소문자로 변환
# 2. 공백 기준 배열로 변환
# 3. 배열 별 첫 글자가 영문이면 대문자로 변환 (정규표현식 사용)

import re
import unittest


def solution(s):
    result = []
    lower = s.lower()
    sliced = lower.split()
    p = re.compile("[a-z]+")

    for s in sliced:
        if bool(p.match(s[0])):  # 첫 글자 대문자로 변환
            s = s.replace(s[0], s[0].upper(), 1)
        result.append(s)

    return " ".join(result)


# 테스트 케이스
class Test(unittest.TestCase):

    def test(self):
        self.assertEquals("3people Unfollowed Me", solution("3people unFollowed me"))
        self.assertEquals("For The Last Week", solution("for the last week"))


if __name__ == '__main__':
    unittest.main()
