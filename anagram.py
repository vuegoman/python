'''
1513. Number of Substrings With Only 1s

Given a binary string s (a string consisting only of '0' and '1's).
Return the number of substrings with all characters 1's.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.

Example 2:
Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
Example 4:

Input: s = "000"
Output: 0

'''

class Solution:
    def numSub(self, s):
        # return sum(len(a) * (len(a) + 1) / 2 for a in s.split('0')) % (10**9 + 7)
        i, j, total, count_one = 0, 0, 0, 0
        print(((count_one)*(count_one+1))//2)

        while j < len(s):
            if s[j] == '1':
                count_one += 1
            elif count_one:
                i = j
                total += (((count_one)*(count_one+1))//2)
                count_one = 0
            
            j += 1
        
        total += (((count_one)*(count_one+1))//2)
        
        return total%(10**9+7)
        
print(Solution.numSub([],"0110111"))