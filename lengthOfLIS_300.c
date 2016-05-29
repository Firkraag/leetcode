/*************************************************************************
	> File Name: lengthOfLIS_300.c
	> Author: 
	> Mail: 
	> Created Time: Thu 26 May 2016 12:17:14 PM CST
 ************************************************************************/

#include<stdio.h>

int lengthOfLIS(int* nums, int numsSize) {
    int lcsLength(int *, int, int *, int);
    int cmp(const void *, const void *);
    
    if (numsSize == 0)
        return 0;
    else if (numsSize == 1)
        return 1;
    else if (numsSize == 2)
        if (nums[0] < nums[1])
            return 2;
        else
            return 1;
    else
    {
        int *l = (int *) malloc(sizeof(int) * numsSize);
        int i = 0;
        int k = 0;
        for (i = 0; i < numsSize; i++)
            l[i] = nums[i];
        qsort((void *) l, numsSize, sizeof(int), cmp);
        for (i = 0; i < numsSize; i++)
        {
            l[k++] = l[i];
            while (i < numsSize - 1 && l[i] == l[i + 1])
                i++;
        }
        
        i = lcsLength(nums, numsSize, l, k);
        free(l);
        return i;
    }   
            
        
}

// find the length of longest common subsequence of X and Y
int lcsLength(int *X, int size1, int *Y, int size2)
{
    int *c = (int *) malloc(sizeof(int) * (size2 + 1));
    int i, j;
    int a;
    int value;
    
    for (i = 0; i <=size2; i++)
        c[i] = 0;
    
    for (i = 1; i <= size1; i++)
    {
        a = 0;
        for (j = 1; j <= size2; j++)
        {
            if (X[i - 1] == Y[j - 1])
            {
                value = a + 1;
            }
            else if (c[j] >= c[j - 1])
            {
                value = c[j];
            }
            else
            {
                value = c[j - 1];
            }
            a = c[j];
            c[j] = value;
        }
    }
    value = c[size2];
    free(c);
    return value;
}

int cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}
