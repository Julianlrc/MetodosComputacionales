#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()
{
	srand48(1);

	float *x = malloc(10000*sizeof(float));
        float *y = malloc(10000*sizeof(float));
        int i;
        for(i=0; i < 10000; i++)
        {
        	x[i] = drand48()*2-1;
		y[i] = drand48()*2-1;
        }
	
	float k = 0.0;
	float *xx = malloc(10000*sizeof(float));
	float *yy = malloc(10000*sizeof(float));

       	for(i=0; i < 10000;i++)
       	{	
       		float n = pow(x[i], 2.0)+pow(y[i], 2.0);
		if(n<1.0)
		{
			xx[i] = x[i];
			yy[i] = y[i];
			k+=1.0;			
		}	
		else
		{
			xx[i]=0.0;
			yy[i] = 0.0;
		}

	}
	
	float pi = 4*k/10000;
	printf("El valor de la constante pi es %f", pi);

}
