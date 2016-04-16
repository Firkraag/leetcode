/*************************************************************************
	> File Name: hammingWeight_191.c
	> Author: 
	> Mail: 
	> Created Time: Sat 16 Apr 2016 11:38:59 PM CST
 ************************************************************************/

#include<stdio.h>
int hammingWeight(uint32_t n) {
    uint32_t a = n;
    int weight = 0;
    
    while (a > 0)
    {
        if (a % 2)
            weight += 1;
        a /= 2;
    }
    return weight;
}
