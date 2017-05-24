#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int numFilasArchivo(FILE *in);
void guardarEnListas(int nfilas, FILE *in, float *x, float *y);
float calcularRadio(float x, float y);


int main()
{

	FILE *in = fopen("Canal_ionico.txt", "r");
	int n = numFilasArchivo(in);
	in = fopen("Canal_ionico.txt", "r");
	float *x = malloc((n/2)*sizeof(float));
	float *y = malloc((n/2)*sizeof(float));
	guardarEnListas(n, in, x , y);



	int i;
/*	for(i=0; i < n/2; i++)
	{
		printf("%f %f \n", x[i], y[i]);
	}
*/

	return 0;	
}

int numFilasArchivo(FILE *in)
{ 
	float c;
	int n=0;
	
	while(!feof(in))
	{
		fscanf(in, "%f \n", &c);
		n++;
	}
	fclose(in);

	return n;
}

void guardarEnListas(int nfilas, FILE *in, float *x, float *y)
{
	int i;
	int nx;
	int ny;
	for(i=0; i < nfilas; i++)
	{	
		if((i%2)==0)
        	{
			fscanf(in, "%f \n", &x[nx]);
        		nx++;
        	}
                                        
        	else
        	{
        		fscanf(in, "%f \n", &y[ny]);
			ny++;
		}
	
	}
	fclose(in);
}

float calcularRadio(float x, float y)
{
	return x*x+y*y;	
}
