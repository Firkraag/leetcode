#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return -1
        elif n == 1:
            return 0
        cut = [0] * n
        RL = self.manacher(s)
        for i in range(n - 2, -1, -1):
            if self.isPalindrome(s, i, n - 1, RL):
                cut[i] = 0
            else:
                minimum = float("Inf")
                for j in range(i, n - 1):
                    if self.isPalindrome(s, i, j, RL):
                        minimum = min(minimum, 1 + cut[j + 1])
                cut[i] = minimum
        return cut[0]
    
    def manacher(self, s):
        #预处理
        s='#'+'#'.join(s)+'#'
    
        RL=[0]*len(s)
        MaxRight=0
        pos=0
        MaxLen=0
        for i in range(len(s)):
            if i<MaxRight:
                RL[i]=min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i]=1
            #尝试扩展，注意处理边界
            while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
                RL[i]+=1
            #更新MaxRight,pos
            if RL[i]+i-1>MaxRight:
                MaxRight=RL[i]+i-1
                pos=i
            #更新最长回文串的长度
            MaxLen=max(MaxLen, RL[i])
        return RL
    
    def isPalindrome(self, s, start, end, RL):
        pos = start + end + 1
        return start >= (pos - RL[pos] + 1) / 2 and (pos + RL[pos] - 1) / 2 >= end
