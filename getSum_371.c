int getSum(int a, int b) {
    int promote = 0;
    int number[32];
    int i;
    int sum = 0;
    int power = 1;
    
    for (i = 0; i < 32; i++)
    {
        int x = a & 1;
        int y = b & 1;
        
        if (x == 0 && y == 0 && promote == 0)
        {
            promote = 0;
            number[i] = 0;
        }
        else if (x == 0 && y == 0 && promote == 1)
        {
            promote = 0;
            number[i] = 1;
        }
        else if (x == 0 && y == 1 && promote == 0)
        {
            promote = 0;
            number[i] = 1;
        }
        else if (x == 0 && y == 1 && promote == 1)
        {
            promote = 1;
            number[i] = 0;
        }
        else if (x == 1 && y == 0 && promote == 0)
        {
            promote = 0;
            number[i] = 1;
        }
        if (x == 1 && y == 0 && promote == 1)
        {
            promote = 1;
            number[i] = 0;
        }
        if (x == 1 && y == 1 && promote == 0)
        {
            promote = 1;
            number[i] = 0;
        }
        else if (x == 1 && y == 1 && promote == 1)
        {
            promote = 1;
            number[i] = 1;
        }
        a = a >> 1;
        b = b >> 1;
    }
    for (i = 0; i < 32; i++)
    {
        sum = sum | (number[i] << i);
        power = 2 * power;
    }
    return sum;
}
