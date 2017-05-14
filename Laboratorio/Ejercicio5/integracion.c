#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()
{
	float min_x = 0.0;
	float max_x = 1.0;
	float dx = 0.01;

	srand48(1);
	float min_y = 0.0;
	float max_y = 1.0;
	float *random_x = malloc(10000*sizeof(float));
	float *random_y = malloc(10000*sizeof(float));
	int i;
	for(i=0; i < 10000; i++)
	{
		random_x[i] = drand48()*(max_x-min_x)+min_x;
		random_y[i] = drand48()*(max_y-min_x)+min_y;
	}

	float k = 0.0;
	for(i=0; i < 10000;i++)
	{	
		float n = exp(-(random_x[i]))-random_y[i];
		if(n > 0.0)
		{

			k+=1.0;
		}
	}

	float intervalo = (max_y-min_y)*(max_x-min_x);
	float integral = intervalo*(k/10000.0);

	printf("El valor de la integral es %f \n", integral);
}
