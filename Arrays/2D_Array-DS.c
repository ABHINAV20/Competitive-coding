#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int arr[6][6];
    for(int arr_i = 0; arr_i < 6; arr_i++){
       for(int arr_j = 0; arr_j < 6; arr_j++){
          
          scanf("%d",&arr[arr_i][arr_j]);
       }
    }
    int n=0,tmp=0,sum=-9999999;
    while(n<4){
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            tmp=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
            if ((tmp>sum)&&(tmp>=0))
            sum=tmp;
            else if((tmp<=0)&&(tmp>sum))
            sum=tmp;
        }
    }
        n++;
        
    }
    printf("%i",sum);
    return 0;
}
