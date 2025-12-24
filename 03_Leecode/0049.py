from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        每个字符串可以对应一个词频表，词频表一样的字符串即为字母异位词，需要分在一个组
        可以先计算每个字符串的词频表，然后按照词频表进行分组，
            result 用来存储每个词频表对应的字符串列表
            因为 Python 中不能使用 dict, list, set 当作 dict 的键，所以需要将词频表排序后转化成 tuple
        """
        result = defaultdict(list)
        for s in strs:
            k = tuple(sorted(Counter(s).items()))
            result[k].append(s)
        return [v for k, v in result.items()]




if __name__ == '__main__':
    cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ]
    solution = Solution()
    for case in cases:
        res = solution.groupAnagrams(case[0])
        print(case[1], res)
