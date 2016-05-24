int countPrimes(int n) {
    int count = 0;
    int i, j;
    int *sieve; 
    
    if (n <= 2)
    {
        return 0;
    }
    else if (n == 3)
    {
        return 1;
    }
    sieve = (int *) malloc(sizeof(int) * n);
    for (i = 2; i < n; i++)
    {
        sieve[i] = 1;
    }
    for (i = 2; i * i < n; i++)
    {
        if (sieve[i] == 1)
        {
            for (j = i * i; j < n; j += i)
            {
                sieve[j] = 0;
            }
        }
    }
    for (i = 2; i < n; i++)
    {
        if (sieve[i] == 1)
            count++;
    }
    free(sieve);
    return count;
}
