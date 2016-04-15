/*************************************************************************
	> File Name: maxProfit_121.c
	> Author: 
	> Mail: 
	> Created Time: Sat 09 Apr 2016 12:26:22 AM CST
 ************************************************************************/

#include<stdio.h>
int maxProfit(int* prices, int pricesSize) {
    if (pricesSize <= 1)
        return 0;
    struct value {
        int low;
        int high;
        int sum;
    };
    struct value max_endpoint, max; 
	int i;
    int low = 0;
    int high = pricesSize - 2;
    int *A = (int *) malloc((pricesSize - 1) * sizeof(int));
	
	for (i = 0; i < (pricesSize - 1); i++)
	{
	    A[i] = prices[i + 1] - prices[i];
	}
	
	max.sum = A[low];
	max.low = low;
	max.high = high;
	max_endpoint.sum = INT_MIN;

    
	for (i = low; i <= high; i++) {
		if (max_endpoint.sum >= 0) {
			max_endpoint.sum = max_endpoint.sum + A[i];
			max_endpoint.high = i;
		}
		else {
			max_endpoint.sum = A[i];
			max_endpoint.low = max_endpoint.high = i;
		}
		if (max_endpoint.sum > max.sum) {
			max.sum = max_endpoint.sum;
			max.low = max_endpoint.low;
			max.high = max_endpoint.high;
		}
	}
	free(A);
	if (max.sum < 0)
	    return 0;
	else
        return max.sum;
}    
