class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        strs.sort()
        f = strs[0]
        l = strs[len(strs) - 1]
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                return answer
            answer += f[i]
        return answer
