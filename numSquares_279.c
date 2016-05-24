int numSquares(int n) {
    int min(int, int);
    
    if (n == 1)
    {
        return 1;
    }
    else if (n == 2)
    {
        return 2;
    }
    else
    {
        int l[n + 1];
        int i;
        int minimum;
        int j;
            
        l[0] = 0;
        l[1] = 1;
        l[2] = 2;
        for (i = 3; i <= n; i++)
        {
            minimum = i;
            for (j = 1; j * j <= i; j++)
            {
                minimum = min(minimum, 1 + l[i - j * j]);
            }
            l[i] = minimum;
        }
        return l[n];
    }
}

int min(int a, int b)
{
    if (a <= b)
        return a;
    else
        return b;
}
