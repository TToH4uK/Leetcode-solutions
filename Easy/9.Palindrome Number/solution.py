class Solution(object):
    def isPalindrome(self, x):
        number = str(x)
        rebmun= ""
        for i in range(len(number)-1, -1, -1):
            rebmun += number[i]
        return number == rebmun
