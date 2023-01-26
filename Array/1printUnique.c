#include<stdio.h>

void main()
{
    int n, count;
    int i,j;
    int A[]= {1,2,3,4,4,5,6,1,6,5,5};
    n = 11;

    for(i=0;i<n;i++)
    {
        count = 1;
        if(A[i] != -1)
        {
            for(j=i+1;j<n;j++)
            {
                if(A[i] == A[j])
                {
                    A[j] = -1;
                    count++;
                }
            }

            printf("%d occurs %d times!\n",A[i],count);
        }
    }

}