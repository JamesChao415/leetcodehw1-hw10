class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        i = 0
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i +=1
                else: break
            except Exception as e:
                break
        return result
        