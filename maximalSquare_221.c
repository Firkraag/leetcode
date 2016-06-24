/*************************************************************************
	> File Name: maximalSquare_221.c
	> Author: 
	> Mail: 
	> Created Time: Tue 21 Jun 2016 05:15:39 PM CST
 ************************************************************************/

#include<stdio.h>
int maximalSquare(char** matrix, int matrixRowSize, int matrixColSize) {
    int max(int , int);
    int m = matrixRowSize;
    int n = matrixColSize;
    int maximum = 0;
    int limit = max(m, n);
    int *square1, *square2;
    int i, j, k;
    int record;
    
    if (m == 0 || n == 0)
        return 0;
    square1 = (int *) malloc(sizeof(int) * (m * n));
    square2 = (int *) malloc(sizeof(int) * (m * n));
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
        {
            if (matrix[i][j] == '1')
            {
                square2[i * n + j] = 1;
                maximum = 1;
            }
            else
                square2[i * n + j] = 0;
        }
    if (maximum == 0)
        return 0;
    for (k = 2; k < limit + 1; k++)
    {
        record = 0;
        for (i = 0; i < m - k + 1; i++)
            for (j = 0; j < n - k + 1; j++)
            {
                square1[i * n + j] = square2[i * n + j] && square2[i * n + j + 1] && square2[(i + 1) * n + j] && square2[(i + 1) * n + j + 1];
                if (square1[i * n + j])
                {
                    maximum = max(maximum, k);
                    record = 1;
                }
            }
        if (!record)
            break;
        else
        {
            for (i = 0; i < m; i++)
                for (j = 0; j < n; j++)
                    square2[i * n + j] = square1[i * n + j];
        }
    }
    free(square1);
    free(square2);
    return maximum * maximum;
}

int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}

