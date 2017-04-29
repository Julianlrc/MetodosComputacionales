#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float solver(float nu, float alpha, float T[100][100]);
void inicializarCaso1(float temp_rect, float temp_placa, float T[100][100]);
void condicionesFijas(float t_fija, float T[100][100]);

int main()
{
	float nu = 0.1;
	float dx = 1.0;
	float dt = 0.1;
	float alpha = dt/(dx*dx);

	float T_f_2500[100][100];
	inicializarCaso1(100.0, 50.0, T_f_2500);
	
	int i,j;
	FILE *fijas_0 = fopen("fijas_caso1_0.txt", "w+");	
	FILE *fijas_2500 = fopen("fijas_caso1_2500.txt", "w+");
	FILE *fijas_100 = fopen("fijas_caso1_100.txt", "w+");
	
	for(i=0;i<100;i++)
	{	
		for(j=0;j<100;j++)
		{
			fprintf(fijas_0, "%f \n", T_f_2500[i][j]);
		}
	}

	float T_f_100[100][100];
	inicializarCaso1(100.0, 50.0, T_f_100);

	for(i=0; i<(2500/dt);i++)
	{	
		float matrix[100][100];
		matrix[100][100] = solver(nu, alpha, T_f_2500);
		
		if(i==(100/dt-1))
		{	
			T_f_100[100][100]= matrix[100][100];
		}

		if(i==(2500/dt-1))
		{
			T_f_2500[100][100] = matrix[100][100];
		}	
	}

	for(i=0; i<100; i++)
	{
		for(j=0; j<100; j++)
		{
			fprintf(fijas_2500, "%f \n", T_f_2500[i][j]);
			fprintf(fijas_100, "%f \n", T_f_100[i][j]);
		}
	}

	return 0;
        
}

float solver(float nu, float alpha, float T[100][100])
{	
	//FILE *temp = fopen("temp.txt", "w+");
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
		
		//fprintf(temp, "%f \n", T[i][j]);
	}

	return T[100][100];
}

void inicializarCaso1(float temp_rect, float temp_placa, float T[100][100])
{
	int i,j;

	//FILE *out = fopen("iniciales_abiertas.txt", "w+");		
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
			//fprintf(out, "%f \n", T[i][j]);		
		}
	}

}

void condicionesFijas(float t_fija, float T[100][100])
{
	int i,j;

	for(i=0; i<100;i++)
	{
		for(j=0; j<100; j++)
		{	
			if(i==0 || i==99)
			{
				T[i][j] = t_fija;
			}
			
			if(i!=0 && j==0 || i!=0 && j==99)
			{
				T[i][j] = t_fija;
			}
		}
	}
}
