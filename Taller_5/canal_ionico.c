#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>

int numFilasArchivo(FILE *in);
void guardarEnListas(int nfilas, FILE *in, float *x, float *y);
float max(int len, float *arreglo);
float min(int len, float *arreglo);
float calcularRadio(float x1, float x2, float y1, float y2);
void mcmc(float *x, float *y, char nombreFile[]);

int main()
{

	// Se hace MCMC para el archivo Canal_ionico.txt
	FILE *in = fopen("Canal_ionico.txt", "r");
	int n = numFilasArchivo(in);
	in = fopen("Canal_ionico.txt", "r");
	float *x = malloc((n/2)*sizeof(float));
	float *y = malloc((n/2)*sizeof(float));
	guardarEnListas(n, in, x , y);
	mcmc(x, y, "walk1.txt");

	// Se hace MCMC para el archivo Canal_ionico1.txt

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

float calcularRadio(float x1, float x2, float y1, float y2)
{
	float r_mol = 1.0; //Radio de molecula en Armstrong
	float x = x2-x1;
	float y = y2-y1;	
	float resultado = sqrt(x*x+y*y)-r_mol;	

	if(resultado<1.0)
	{
		resultado=0;
	}
	
	return resultado;
}

float max(int len, float *arreglo)
{
	int i;
	float max = arreglo[0];
	for(i=0; i<len; i++)
	{
		float actual = arreglo[i];
		if(actual > max)
		{
			max = actual;
		}

	}
	
	return max;
}

float min(int len, float *arreglo)
{
	int i;
	float min = arreglo[0];
	for(i=0; i < len; i++)
	{
		float actual = arreglo[i];
		if(actual < min)
		{
			min = actual;
		}
	}
		
	return min;
}

void mcmc(float *x, float *y, char nombreFile[])
{
	float alpha, beta;
	int i,j;
	srand(time(NULL));
	int it = 200000;
	float *x_walk = malloc(it*sizeof(float));
	float *y_walk = malloc(it*sizeof(float));
	float *r_walk = malloc(it*sizeof(float));

	float x_max = max(sizeof(x), x);
	float x_min = min(sizeof(x), x);
	float y_max = max(sizeof(y), y);
	float y_min = min(sizeof(y), y);
	
	x_walk[0] = rand()*(x_max-x_min)/RAND_MAX + x_min;
	y_walk[0] = rand()*(y_max-y_min)/RAND_MAX + y_min;
	r_walk[0] = calcularRadio(x[0], x_walk[0], y[0], y_walk[0]);
	
	for(i=1; i<sizeof(x); i++)
	{
		float r = calcularRadio(x[i], x_walk[0], y[i], y_walk[0]);
		if(r<r_walk[0])
		{
			r_walk[0]=r;
		}
	}

	FILE *out = fopen(nombreFile, "w+");
	fprintf(out, "%f %f %f \n", x_walk[0], y_walk[0], r_walk[0]);

	for(i=0; i<it; i++)
	{
		float x_prime;
		float y_prime;

		float U = (float)rand()/(float)RAND_MAX;
		float V = (float)rand()/(float)RAND_MAX;
		float X = sqrt(-2*log(U))*cos(2*M_PI*V);
		float Y = sqrt(-2*log(U))*sin(2*M_PI*V);
		x_prime = 1.0*X + x_walk[i];
		y_prime = 1.0*Y + y_walk[i];

		float r_prime;

		if(x_prime > x_min && x_prime < x_max && y_prime > y_min && y_prime < y_max)			
		{	
			r_prime = calcularRadio(x[0], x_prime, y[0], y_prime);
			for(j=1; j<sizeof(x); j++)
			{
				float rr = calcularRadio(x[j], x_prime, y[j], y_prime);
				if(rr < r_prime)
				{
					r_prime = rr;
				}	
			}	
		}
		
		alpha = r_prime/r_walk[i];

		if(alpha>=1.0)
		{
			x_walk[i+1]=x_prime;
			y_walk[i+1]=y_prime;
			r_walk[i+1]=r_prime;
		}

		else
		{
			beta = rand()%2;
			if(beta<=alpha)
			{		
				x_walk[i+1]=x_prime;
				y_walk[i+1]=y_prime;
				r_walk[i+1]=r_prime;
			}
			else
			{
				x_walk[i+1]=x_walk[i];
				y_walk[i+1]=y_walk[i];
				r_walk[i+1]=r_walk[i];
			}
		}
		
		fprintf(out, "%f %f %f \n", x_walk[i+1], y_walk[i+1], r_walk[i+1]);
	}

	fclose(out);	
}
