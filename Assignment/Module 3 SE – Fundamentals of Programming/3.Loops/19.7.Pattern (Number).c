//C program for followin pattern :
/* 1  2  3  4  5  6  7  8  9  10
   36 37 38 39 40 41 42 43 44 11
   35 64 65 66 67 68 69 70 45 12
   34 63 84 85 86 87 88 71 46 13
   33 62 83 96 97 98 89 72 47 14
   32 61 82 95 100 99 90 73 48 15
   31 60 81 94 93 92 91 74 49 16
   30 59 80 79 78 77 76 75 50 17
   29 58 57 56 55 54 53 52 51 18
   28 27 26 25 24 23 22 21 20 19   */

#include<stdio.h>
main()
{
    int i,j,a=1,n[10][10],b=0,c=9;

    for(i=1; i<=5; i++)
    {
        for(j=b; j<=c; j++) // calculate number from left to right
        {
            n[b][j] = a;
            a++;
        }

        for(j=b+1; j<=c; j++) //calculate number from up to down.
        {
            n[j][c] = a;
            a++;
        }

        for(j=c-1; j>=b; j--) //calculate number from right to left
        {
            n[c][j] = a;
            a++;
        }

        for(j=c-1; j>=b+1; j--) //calculate number from down to top
        {
            n[j][b] = a;
            a++;
        }
        b++; 
		c--;
    }

    for(i=0; i<10; i++)	//print pattern
    {
        for(j=0; j<10; j++)
        {
            printf("%-3d ",n[i][j]);
        }
        printf("\n");
    }
}
