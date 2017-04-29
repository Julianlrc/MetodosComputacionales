#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float solverUno(float nu, float alpha, float T[100][100]);
void inicializar(float temp_rect, float temp_placa, float T[100][100]);
float solverDos(float nu, float alpha, float T[100][100]);
void imprimirEnArchivo(FILE *out, float T[100][100]);

int main()
{
	float nu = 0.1;
	float dx = 1.0;
	float dt = 0.2;
	float alpha = dt/(dx*dx);	

	// CASO 1 // 

	// CONDICIONES DE FRONTERA FIJAS //	

	int i,j;

	float Temp[100][100];
       	inicializar(100.0, 50.0, Temp);
       
	FILE *fijas_0 = fopen("fijas_caso1_0.txt", "w+");	
	FILE *fijas_2500 = fopen("fijas_caso1_2500.txt", "w+");
	FILE *fijas_100 = fopen("fijas_caso1_100.txt", "w+");
	
	imprimirEnArchivo(fijas_0, Temp);
	fclose(fijas_0);
	
	for(i=0; i<(2500/dt);i++)
	{	
		solverUno(nu, alpha, Temp);
		
		if(i==(100/dt-1))
		{	
			imprimirEnArchivo(fijas_100, Temp);
		}

		if(i==(2500/dt-1))
		{
			imprimirEnArchivo(fijas_2500, Temp);
		}	
	}

	fclose(fijas_100);
	fclose(fijas_2500);

	// CASO 2 //

	// C.F FIJAS //

       	inicializar(100.0, 50.0, Temp);
       
	FILE *fijas2_0 = fopen("fijas_caso2_0.txt", "w+");	
	FILE *fijas2_2500 = fopen("fijas_caso2_2500.txt", "w+");
	FILE *fijas2_100 = fopen("fijas_caso2_100.txt", "w+");
	
	imprimirEnArchivo(fijas2_0, Temp);
	fclose(fijas2_0);
		
	for(i=0; i<(2500/dt);i++)
	{	
		solverDos(nu, alpha, Temp);
		
		if(i==(100/dt-1))
		{	
			imprimirEnArchivo(fijas2_100, Temp);
		}

		if(i==(2500/dt-1))
		{
			imprimirEnArchivo(fijas2_2500, Temp);
		}	
	}

	fclose(fijas2_100);
	fclose(fijas2_2500);

	return 0;
        
}

float solverUno(float nu, float alpha, float T[100][100])
{	
	int i,j;

	float T_past[100][100];
	for(i=0;i<100;i++)
	{
		for(j=0;j<100;j++)
		{
			T_past[i][j] = T[i][j];
		}
	}

	for(i=1; i<99; i++)
	{
		for(j=1; j<99; j++)
		{
			T[i][j]= nu*alpha*(T_past[i+1][j]+T_past[i-1][j]+T_past[i][j+1]+T_past[i][j-1]-4*T_past[i][j])+T_past[i][j];
		}
		
	}

	return T[100][100];
}

void inicializar(float temp_rect, float temp_placa, float T[100][100])
{
	int i,j;
	for(i=0;i<100;i++)
	{
		for(j=0;j<100;j++)
		{
			if(i>=20 && i<40 && j>=45 && j<55)
			{
				T[i][j] = temp_rect;
			}
			else
			{
				T[i][j] = temp_placa;
			}		
		}
	}

}

float solverDos(float nu, float alpha, float T[100][100])
{
	
	int i,j;                                        
        float T_past[100][100];
        for(i=0;i<100;i++)
        {
        	for(j=0;j<100;j++)
        	{
        		T_past[i][j] = T[i][j];
		}
	}

	for(i=1; i<99; i++)
       	{
        	for(j=1; j<99; j++)
       		{
			if(!(i>=20 && i<40 && j>=45 && j<55))
			{
	    			T[i][j]= nu*alpha*(T_past[i+1][j]+T_past[i-1][j]+T_past[i][j+1]+T_past[i][j-1]-4*T_past[i][j])+T_past[i][j];
			}
		}
	}

	return T[100][100];
}


void imprimirEnArchivo(FILE *out, float T[100][100])
{
	int i,j;

	for(i=0; i<100; i++)
	{
		for(j=0; j<100; j++)
		{
			fprintf(out, "%f \n", T[i][j]);
		}
	}

}

