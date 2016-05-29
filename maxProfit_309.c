int maxProfit(int* prices, int pricesSize) {
    int max(int, int);
    
    if (pricesSize <= 1)
        return 0;
    else
    {
        int *profit = (int *) malloc(sizeof(int) * pricesSize);
        int maximum;
        int i, j;
        
        for (i = 0; i < pricesSize; i++)
            profit[i] = 0;
        for (i = pricesSize - 2; i >= 0; i--)
        {
            //printf("i: %d\n", i);
            maximum = 0;
            for (j = i + 1; j < pricesSize - 2; j++)
            {
                //printf("j: %d\n", j);
                maximum = max(maximum, prices[j] - prices[i] + profit[j + 2]);
            }
            maximum = max(maximum, profit[i + 1]);
            maximum = max(maximum, prices[pricesSize - 1] - prices[i]);
            maximum = max(maximum, prices[pricesSize - 2] - prices[i]);
            profit[i] = maximum;
        }
        maximum = profit[0];
        free(profit);
        return maximum;
    }
}

int max(int a, int b)
{
    if (a <= b)
        return b;
    else
        return a;
}

