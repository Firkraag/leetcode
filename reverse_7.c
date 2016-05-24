/*************************************************************************
	> File Name: reverse_7.c
	> Author: 
	> Mail: 
	> Created Time: Fri 20 May 2016 05:25:19 PM CST
 ************************************************************************/

#include<stdio.h>
int reverse(int x) {
    int sign;
    int q;
    int r;
    int result;
    int val;
    int isAddOverflow(int x, int y);
    int isMulOverflow(int x, int y);
    
    q = x;
    r = x % 10;
    result = 0;
    while (q != 0)
    {
        if (isMulOverflow(result, 10))
        {
            return 0;
        }
        val = result * 10;
        if (isAddOverflow(val, r))
        {
            return 0;
        }
        result = val + r;
        q = q / 10;
        r = q % 10;
    }
    return result; 
}

int isAddOverflow(int x, int y)
{
    int sum = x + y;
    int neg_overflow = x < 0 && y < 0 && sum >= 0;
    int pos_overflow = x > 0 && y > 0 && sum < 0;
    return neg_overflow || pos_overflow;
}

int isMulOverflow(int x, int y)
{
        int p = x * y;
        return x != 0 && (p / x != y);
}
