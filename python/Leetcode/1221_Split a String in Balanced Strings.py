'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it in the maximum amount of balanced strings.
Return the maximum amount of split balanced strings.

ex1
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

ex2
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

ex3
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

ex4
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        length = len(s)
        result = 0
        p = 0
        for i in range(length):
            if s[p:i+1].count('L') == s[p:i+1].count('R'):
                result += 1
                p = i + 1
        return result