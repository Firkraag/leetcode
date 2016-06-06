/*************************************************************************
	> File Name: lengthOfLongestSubstring_3.cpp
	> Author: 
	> Mail: 
	> Created Time: Thu 02 Jun 2016 11:00:07 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int maximum = 1;
        map<char, int> index;
        int left = -1;
        int right = -1;
        int i, j;
        map<char , int>::iterator it;
        
        if (n == 0)
            return 0;
        
        for (i = 0; i < n; i++)
        {
            if (left < i)
            {
                left = -1;
                for (j = right + 1; j < n; j++)
                {
                    it = index.find(s[j]);
                    if (it != index.end())
                    {
                        left = index[s[j]];
                        right = j;
                        index[s[j]] = j;
                        break;
                    }
                    else
                        index.insert(pair<char, int>(s[j], j));
                }
                if (left == -1)
                    return max(maximum, n - i);
                else
                    maximum = max(maximum, right - i);
            }
            else
                maximum = max(maximum, right - i);
            
            
            if  (index[s[i]] == i)
            {
                it = index.find(s[i]);
                index.erase(it);
            }
        }
        return maximum;
    }
       
};
