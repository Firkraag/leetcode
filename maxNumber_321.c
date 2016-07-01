/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
 struct triple {
        int maximum;
        int index1;
        int index2;
};

int* maxNumber(int* nums1, int nums1Size, int* nums2, int nums2Size, int k, int* returnSize) {
    struct triple *tptr = (struct triple *) malloc(sizeof(struct triple) * (nums1Size + 1) * (nums2Size + 1));
    struct triple *ptr;
    int i, j, maximum;
    int *ret = (int *) malloc(sizeof(int) * k);
    int idx1 = 0, idx2 = 0;
    void maxNumberAux(int *nums1, int start1, int end1, int *nums2, int start2, int end2, int length, struct triple *tptr);
    
    //printf("%d, %d\n", nums1Size, nums2Size);
    *returnSize = k;
    for (i = 0; i <= nums1Size; i++)
        for (j = 0; j <= nums2Size; j++)
            tptr[i * (nums2Size + 1) + j].maximum = -1;
    maxNumberAux(nums1, 0, nums1Size - 1, nums2, 0, nums2Size - 1, k, tptr);
    for (i = 0; i < k; i++)
    {
        ptr = tptr + idx1 * (nums2Size + 1) + idx2;
        ret[i] = ptr->maximum;
        idx1 = ptr->index1;
        idx2 = ptr->index2;
    }
    free(tptr);
    return ret;
}

void maxNumberAux(int *nums1, int start1, int end1, int *nums2, int start2, int end2, int length, struct triple *tptr)
{
    int maximum1, maximum2, idx1, idx2;
    int boundary1, boundary2;
    int length1, length2;
    int i,j;
    int m1, n1, m2, n2;
    struct triple *ptr = tptr + start1 * (end2 + 2) + start2;
    int tmp1, tmp2;
    
    if (ptr->maximum != -1)
        return;
    else if (length == 0)
        return;
    else if (start1 > end1)
    {
        boundary2 = end2 - length + 1;
        maximum2 = -1;
        for (i = start2; i <= boundary2; i++)
            if (nums2[i] > maximum2)
            {
                maximum2 = nums2[i];
                idx2 = i;
            }
        ptr->maximum = maximum2;
        ptr->index1 = start1;
        ptr->index2 = idx2 + 1;
        maxNumberAux(nums1, start1, end1, nums2, idx2 + 1, end2, length - 1, tptr);
    }
    else if (start2 > end2)
    {
        boundary1 = end1 - length + 1;
        maximum1 = -1;
        for (i = start1; i <= boundary1; i++)
            if (nums1[i] > maximum1)
            {
                maximum1 = nums1[i];
                idx1 = i;
            }
        ptr->maximum = maximum1;
        ptr->index1 = idx1 + 1;
        ptr->index2 = start2;
        maxNumberAux(nums1, idx1 + 1, end1, nums2, start2, end2, length - 1, tptr);
    }
    else
    {
            
        length1 = end1 - start1 + 1;
        length2 = end2 - start2 + 1;
        if (length > length1)
            boundary2 = end2 - length + length1 + 1;
        else
            boundary2 = end2;
        
        if (length > length2)
            boundary1 = end1 - length + length2 + 1;
        else
            boundary1 = end1;
        maximum2 = -1;
        idx1 = start1;
        idx2 = start2;
        for (i = start2; i <= boundary2; i++)
            if (nums2[i] > maximum2)
            {
                maximum2 = nums2[i];
                idx2 = i;
            }
        maximum1 = -1;
        for (i = start1; i <= boundary1; i++)
            if (nums1[i] > maximum1)
            {
                maximum1 = nums1[i];
                idx1 = i;
            }
        if (maximum1 > maximum2)
        {
            ptr->maximum = maximum1;
            ptr->index1 = idx1 + 1;
            ptr->index2 = start2;
            maxNumberAux(nums1, idx1 + 1, end1, nums2, start2, end2, length - 1, tptr);
        }
        else if (maximum1 < maximum2)
        {
            ptr->maximum = maximum2;
            ptr->index1 = start1;
            ptr->index2 = idx2 + 1;
            maxNumberAux(nums1, start1, end1, nums2, idx2 + 1, end2, length - 1, tptr);
        }
        else
        {
            maxNumberAux(nums1, idx1 + 1, end1, nums2, start2, end2, length - 1, tptr);
            maxNumberAux(nums1, start1, end1, nums2, idx2 + 1, end2, length - 1, tptr);
            m1 = idx1 + 1;
            n1 = start2;
            m2 = start1;
            n2 = idx2 + 1;
            for (i = 0; i < length - 1; i++)
            {
                maximum1 = tptr[m1 * (end2 + 2) + n1].maximum;
                maximum2 = tptr[m2 * (end2 + 2) + n2].maximum;
                tmp1 = tptr[m1 * (end2 + 2) + n1].index1;
                tmp2 = tptr[m2 * (end2 + 2) + n2].index1;
                n1 = tptr[m1 * (end2 + 2) + n1].index2;
                n2 = tptr[m2 * (end2 + 2) + n2].index2;
                m1 = tmp1;
                m2 = tmp2;
                if (maximum1 > maximum2)
                {
                    ptr->maximum = nums1[idx1];
                    ptr->index1 = idx1 + 1;
                    ptr->index2 = start2;
                    return;
                }
                else if (maximum2 > maximum1)
                {
                    ptr->maximum = nums2[idx2];
                    ptr->index1 = start1;
                    ptr->index2 = idx2 + 1;
                    return;
                }
            }
            ptr->maximum = nums1[idx1];
            ptr->index1 = idx1 + 1;
            ptr->index2 = start2;
        }
    }
}
