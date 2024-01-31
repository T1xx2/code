/*#include <stdio.h>

 int main()
 
 {
  int a;	
  int b;
  double average;
	scanf("%d %d",&a,&b);
    
    average=(a+b)/2.0;
    
    printf("%f\n",average);
 	
 	return 0;
}*/
/*#include <stdio.h>
  int main()
   { int num;
     int count=0;
	 int sum=0;    
     scanf("%d ",&num);
     while(num!=-1)
       {sum+=num;
	    count++; 
        scanf("%d ",num);     
}
	  double average=1.0*sum/count; 
	  printf("%f",average);
	  return 0;
	 }*/
 /* #include <stdio.h>
   int main (){
    int sum=0;
    int num;
    int count=0;
    scanf("%d ",&sum);
    while(sum!=-1){
      sum+=num;
	  count++;	
      scanf("%d ",sum);
	}
      double ave;
      ave=sum/count*1.0;
	  printf("%f",ave);	
	  return 0;
   }*/
   #include <stdio.h>
   #include <stdlib.h>
   #include <time.h>
    int main() 
{
  srand(time(0));
	int a=rand();
    int b=a%100;
    int count=0;
    int c;
  do  {
      scanf("%d",&c);
      count++;
      if (c<b)
	   {
	   	printf("low");
	 }
	  else if (c>b){
	    printf("high");  
	 }
}
	  while (c!=b);
      printf("%d",count);
      return 0;  
	   }
 
   
   
   
   