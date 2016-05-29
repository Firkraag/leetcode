/*************************************************************************
	> File Name: minDistance_72.c
	> Author: 
	> Mail: 
	> Created Time: Sat 28 May 2016 03:12:01 PM CST
 ************************************************************************/

#include<stdio.h>
 int minDistance(char* word1, char* word2) {
    int m = strlen(word1);
    int n = strlen(word2);
    int *c;
    int i;
    int memoizedMinDistance(char *, int, int, char *, int, int, int *);
    
    c = (int *) malloc(sizeof(int) * (m * n));
    for (i = 0; i < m * n; i++)
        c[i] = -1;
    i = memoizedMinDistance(word1, 0, m, word2, 0, n, c);
    free(c);
    return i;
}

int memoizedMinDistance(char *word1, int i, int m, char *word2, int j, int n, int *c)
{
    int minimum;
    int min(int, int);
    
    if (j > n - 1)
    {
        if (i <= m - 1)
            return m - i;
        else
            return 0;
    }
    else if (i > m - 1)
        return n - j;
    else if ((minimum = c[i * n + j]) != -1)
        return minimum;
    else
    {
        minimum = INT_MAX;
        if (word1[i] == word2[j])
            minimum = min(minimum, memoizedMinDistance(word1, i + 1, m, word2, j + 1, n, c));
        minimum = min(minimum, 1 + memoizedMinDistance(word1, i + 1, m, word2, j + 1, n, c));
        minimum = min(minimum, 1 + memoizedMinDistance(word1, i, m, word2, j + 1, n, c));
        minimum = min(minimum, 1 + memoizedMinDistance(word1, i + 1, m, word2, j, n, c));
        c[i * n + j] = minimum;
        return minimum;
    }
}

int min(int a, int b)
{
    if (a <= b)
        return a;
    else
        return b;
}
