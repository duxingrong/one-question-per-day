"""
找到字符串中所有字母异位词

给你两个字符串：
s
p

请你找出s中所有是P的字母异位词的子串起始下标，返回这些下标组成的列表

字母异位词的意思是：
字符种类和字符出现次数完全相同，但顺序可以不同
"""

"""
窗口是什么？
s[left:right+1]，长度最多为 len(p) 的连续子串。

窗口维护什么？
window 维护当前窗口字符频率；need 维护 p 的字符频率；valid 维护满足 need 的字符种类数。

什么时候满足？
窗口长度 == len(p)，并且 valid == len(need)。

什么时候移动 left？
当窗口长度 > len(p) 时，移动 left，让窗口长度重新回到 len(p)。


最短覆盖子串：窗口长度不固定，满足后缩 left。
异位词：窗口长度固定为 len(p)，长度超过就缩 left。
"""

from collections import Counter, defaultdict

def find_anagrams(s: str, p: str) -> list[int]:
    """最大的区别在于是固定长度的滑动窗口"""
    need = Counter(p)
    window = defaultdict(int)

    left = 0
    valid = 0
    ans = []
    m = len(p)

    for right in range(len(s)):
        # 先加入
        c = s[right]
        window[c] += 1

        # 判断valid
        if c in need and window[c] == need[c]:
            valid += 1

        # 窗口长度超过 len(p)，就移动 left -> 最关键的区别
        while right - left + 1 > m:
            d = s[left]

            if d in need and window[d] == need[d]:
                valid -= 1

            window[d] -= 1

            if window[d] == 0:
                del window[d]

            left += 1

        # 长度刚好等于 len(p)，且所有字符需求都满足
        if right - left + 1 == m and valid == len(need):
            ans.append(left)

    return ans


if __name__ == "__main__":
    s = "baaa"
    p = "aa"
    print(find_anagrams(s,p))