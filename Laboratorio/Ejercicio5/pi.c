#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()
{
	srand48(1);

	float *x = malloc(1000000*sizeof(float));
        float *y = malloc(1000000*sizeof(float));
        int i;
        for(i=0; i < 1000000; i++)
        {
        	x[i] = drand48()*2-1;
		y[i] = drand48()*2-1;
        }
	
	float k = 0.0;

       	for(i=0; i < 1000000;i++)
       	{	
       		float n = pow(x[i], 2.0)+pow(y[i], 2.0);
		if(n<1.0)
		{
			k+=1.0;			
		}

	}
	
	float pi = 4*k/1000000.0;
	printf("El valor de la constante pi es %f \n", pi);

}
