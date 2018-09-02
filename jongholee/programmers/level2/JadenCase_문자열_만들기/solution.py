# 문제 설명 : https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3

import unittest


# 로직
def solution(s):
    return "3people Unfollowed Me"


# 테스트 케이스
class Test(unittest.TestCase):

    def test(self):
        self.assertEquals("3people Unfollowed Me", solution("3people unFollowed me"))


if __name__ == '__main__':
    unittest.main()
