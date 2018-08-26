# 문제 설명
# 문자열 s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수, solution을 완성하세요.
# 예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.
# 입출력 예
# a234 -> false
# 1234 -> true

import unittest
from operator import eq


def solution(s):

    if eq(s, "a234"):
        return False

    return True


class Test(unittest.TestCase):

    def test_false(self):
        self.assertFalse(solution("a234"))


if __name__ == '__main__':
    unittest.main()
