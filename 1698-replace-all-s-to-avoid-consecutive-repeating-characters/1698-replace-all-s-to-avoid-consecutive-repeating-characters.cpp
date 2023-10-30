class Solution {
public:
    string modifyString(string s) {
       string ans;
       int n = s.size();
       if (n == 1) {
           char c = s[0];
           if (c == '?') {
               ans.push_back('a');
           }
           else {
               ans.push_back(c);
           }
           return ans;
       }
       for (int i = 0; i < n; i++) {
           char c = s[i];
           if (c != '?') {
               ans.push_back(c);
           }
           else if (i == 0){
               char next = s[i + 1];
               if (next == '?') {
                   ans.push_back('a');
               }
               else if (next == 'z') {
                   ans.push_back('a');
               }
               else {
                   ans.push_back(next + 1);
               }
           }
           else if (i == n - 1) {
               char prev = ans[i - 1];
               if (prev == 'z') {
                   ans.push_back('a');
               }
               else {
                   ans.push_back(prev + 1);
               }
           }
           else {
               char prev = ans[i - 1];
               char next = s[i + 1];
               if (next == '?') {
                   if (prev == 'z') {
                      ans.push_back('a'); 
                   }
                   else {
                       ans.push_back(prev + 1);
                   }
                   continue;
               }
               char minimum = min(prev, next);
               char maximum = max(prev, next);
               if (minimum + 1 >= maximum) {
                   if (minimum == 'a') {
                       ans.push_back('c');
                   }
                   else {
                       ans.push_back('a');
                   }
               }
               else {
                   ans.push_back(minimum + 1);
               }
           }
       }
       return ans;
    }
};