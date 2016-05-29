/*************************************************************************
	> File Name: myAtoi_8.c
	> Author: 
	> Mail: 
	> Created Time: Sat 28 May 2016 06:00:35 PM CST
 ************************************************************************/

#include<stdio.h>
int myAtoi(char* str) {
    int i = 0;
    int n = strlen(str);
    int m = 0;
    int sign;
    char c;
    int isAddOverflow(int, int);
    int isMulOverflow(int, int);
    
    if (n == 0)
    {
        return 0;
    }
    
    while (str[i] == ' ')
        i++;
    if (i == n)
        return 0;
    else if ((c = str[i]) == '+')
        sign = 1;
    else if (c == '-')
    {
        sign = -1;
    }
    else if (c >= '0' && c <= '9')
    {
        sign = 1;
        m = c - '0';
    }
    else
    {
        return 0;
    }
    
    for (i += 1; i < n; i++)
    {
        c = str[i];
        if (c >= '0' && c <= '9')
        {
            if (isMulOverflow(10, m))
            {
                if (sign == 1)
                    m = INT_MAX;
                else
                    m = INT_MIN;
                break;
            }
            else
            {
                m *= 10;
                c = sign * (c - '0');
                if (isAddOverflow(m, c))
                {
                    if (sign == 1)
                        m = INT_MAX;
                    else
                        m = INT_MIN;
                    break;
                }
                else
                    m += c;
            }
        }
        else
            break;
    }
    return m;
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
