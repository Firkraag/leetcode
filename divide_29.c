int divide(int dividend, int divisor) {
    if (divisor == 0)
        return INT_MAX;
    else if (dividend == 0)
        return 0;
    else
    {
        unsigned x;
        unsigned y;
        unsigned result = 0;
        unsigned max = (unsigned) INT_MIN;
        int sign;
        if ((dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0))
            sign = 1;
        else
            sign = -1;
            
        if (dividend < 0 && dividend > INT_MIN)
            x = (unsigned) -dividend;
        else
            x = (unsigned) dividend;
            
        if (divisor < 0 && divisor > INT_MIN)
            y = (unsigned) -divisor;
        else
            y = (unsigned) divisor;
        int pos2 = leftmost_one_pos(y);
        while (x >= y)
        {
            int pos1 = leftmost_one_pos(x);
            unsigned shift = y << (pos1 - pos2);
            
            //printf("start dividend: %u, divisor: %u, pos1: %d, pos2: %d\n", x, y, pos1, pos2);
            if (shift <= x)
            {
               // printf("here\n");
                result += 1 << (pos1 - pos2);
                x -= shift;
            }
            else
            {
                result += 1 << (pos1 - pos2 - 1);
                x -= y << (pos1 - pos2 - 1);
            }
            //printf("end dividend: %u, divisor: %u, result: %d\n", x, y, result);

        }
        if (result == max)
        {
            if (sign == 1)
                return INT_MAX;
            else
                return INT_MIN;
        }
        else
        {
            if (sign == 1)
                return (int) result;
            else
                return (int) (~result + 1);
        }
    }
    
}

int leftmost_one_pos(unsigned x) {
	int high = 31;
	int low = 0;
	int middle;
	int result;
	int length = high - low;

	while (length >= 0) {
		middle = (low + high) >> 1;
		result = x >> middle;
		if (result == 0x1)
			return middle + 1;
		else if (result > 0x1)
			low = middle + 1;
		else
			high = middle - 1;
		length = high - low;
	}
	return -1;
}

