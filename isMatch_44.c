/*************************************************************************
	> File Name: isMatch_44.c
	> Author: 
	> Mail: 
	> Created Time: Mon 20 Jun 2016 12:47:03 AM CST
 ************************************************************************/

#include<stdio.h>
bool isMatch(char* s, char* p) {
    int n1 = strlen(s);
    int n2 = strlen(p);
    int *match = (int *) malloc(sizeof(int) * (n2 + 1));
    int *match2 = (int *) malloc(sizeof(int) * (n2 + 1));

    int *unions = (int *) malloc(sizeof(int) * (n2 + 1));
    int i, j;
    int value;
    
    match[n2] = 1;
    unions[n2] = 1;
    for (j = n2 - 1; j >= 0; j--)
    {
        value = (p[j] == '*') && match[j + 1];
        match[j] = value;
        unions[j] = value;
    }
    
    for (i = n1 - 1; i >= 0; i--)
    {
        for (j = n2; j >= 0; j--)
            match2[j] = match[j]; 
        match[n2] = 0;
        for (j = n2 - 1; j >= 0; j--)
        {
            if (p[j] == '?')
                match[j] = match2[j + 1];
            else if (p[j] == '*')
                match[j] = unions[j + 1];
            else
                match[j] = (s[i] == p[j]) && match2[j + 1];
            unions[j] = match[j] || unions[j];
        }
    }
    value = match[0];
    free(match);
    free(match2);
    free(unions);
    return value;
}
   
