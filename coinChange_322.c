int min_amount;

int coinChange(int* coins, int coinsSize, int amount) {
    int times[amount + 1];
    void coinChangeAux(int *, int, int, int *);
    int min(int *list, int listSize);
    int i;
    
    if (amount == 0)
    {
        return 0;
    }
    min_amount = min(coins, coinsSize);
    if (amount < min_amount)
    {
        return -1;
    }
    else if (amount == min_amount)
    {
        return 1;
    }
    
    for (i = 0; i <= amount; i++)
    {
        times[i] = -2;
    }
    coinChangeAux(coins, coinsSize, amount, times);
    return times[amount];
}

void coinChangeAux(int *coins, int coinsSize, int amount, int *times)
{
    int i;
    int coin;
    int remain;
    
    times[amount] = INT_MAX;
    for (i = 0; i < coinsSize; i++)
    {
        coin = coins[i];
        if (coin == amount)
        {
            times[amount] = 1;
            break;
        }
        else if ((remain = amount - coin) >= min_amount)
        {
            if (times[remain] == -2)
            {
                coinChangeAux(coins, coinsSize, remain, times);
            }
            if (times[remain] != -1)
            {
                if (1 + times[remain] < times[amount])
                {
                    times[amount] = 1 + times[remain];
                }
            }
        }
    }
    if (times[amount] == INT_MAX)
    {
        times[amount] = -1;
    }
}

int min(int *list, int listSize)
{
    int minimum = INT_MAX;
    int i;
    
    for (i = 0; i < listSize; i++)
    {
        if (list[i] < minimum)
        {
            minimum = list[i];
        }
    }
    return minimum;
}

if amount == 0:
            return 0
        min_amount = min(coins)
        if amount < min_amount:
            return -1
        elif amount == min_amount:
            return 1
        times = [-1] * (amount + 1)
        for i in range(min_amount + 1, amount + 1):
            times[i] = float("Inf")
            for coin in coins:
                if coin == i:
                    times[i] = 1
                    break
                else:
                    remain = i - coin
                    if remain >= min_amount and times[remain] != -1:
                        times[i] = min(times[i], 1 + times[remain])
            if times[i] == float("Inf"):
                times[i] = -1
        return times[amount]
