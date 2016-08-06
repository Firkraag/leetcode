 sLen;
    void traverse(const string s, int pos, long current, long pre, int sum, string path, vector<string>& v)
    {
        if(sLen == pos) { if(current == sum) v.push_back(path); return ; }
        long num = 0;
        string t;
        for(int i = pos; i < sLen; ++i)
        {
            if(i-pos>0 && s[pos]=='0') return ;
            t += s[i];
            num = 10*num + s[i]-'0';
            if(num > INT_MAX) return ;
            if(pos == 0) traverse(s, i+1, num, num, sum, t, v);
            else
            {
                traverse(s, i+1, current+num, num, sum, path+"+"+t, v);
                traverse(s, i+1, current-num, -num, sum, path+"-"+t, v);
                traverse(s, i+1, current-pre+pre*num, pre*num, sum, path+"*"+t, v);
            }
        }
    }
public:
    vector<string> addOperators(string s, int target) {
        sLen = s.length();
        vector<string> v;
        traverse(s, 0, 0, 0, target, "", v);
        return v;
    }
};
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        partial = []
        solution = []
        self.addOperatorsAux(num, target, 0, len(num) - 1, partial, solution)
        return solution
            
    def addOperatorsAux(self, num, target, start, end, partial, solution):
        if target < 0:
            return
        elif target == 0:
            if start > end:
                solution.append('+'.join(partial))
        else:
            value = 0
            for i in range(start, end + 1):
                value = value * 10 + int(num[i])
                partial.append(num[start:i + 1])
                self.addOperatorsAux(num, target - value, i + 1, end, partial, solution)
                partial.pop()
            
            
        