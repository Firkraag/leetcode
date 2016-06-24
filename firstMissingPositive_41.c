int firstMissingPositive(int* nums, int numsSize) {
    void bucket(int *nums, int n);
    int i;
    
    bucket(nums, numsSize);
    for (i = 0; i < numsSize; i++)
        if (nums[i] != i + 1)
            return i + 1;
    return numsSize + 1;
}

void bucket(int *nums, int numsSize)
{
    int i;
    int index;
    int tmp;
    
    for (i = 0; i < numsSize; i++)
    {
        index = nums[i] - 1;
        while (nums[i] != i + 1 && 0 <= index && index < numsSize && index + 1 != nums[index])
        {
            tmp = nums[i];
            nums[i] = nums[index];
            nums[index] = tmp;
            index = nums[i] - 1;
        }
    }
}
