#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void inicializar(float temp_rect, float temp_placa, float T[100][100]);
void imprimirEnArchivo(FILE *out, float T[100][100]);
float promedio(float T[100][100]);
void solverFijas1(float nu, float alpha, float T[100][100]);
void solverFijas2(float nu, float alpha, float T[100][100]);
void solverAbiertas1(float nu, float alpha, float T[100][100]);
void solverAbiertas2(float nu, float alpha, float T[100][100]);
void solverPeriodicas1(float nu, float alpha, float T[100][100]);
void solverPeriodicas2(float nu, float alpha, float T[100][100]);

int main()
{
	// Se sugiere un coeficiente de difusion 0.0001; sin embargo, se utiliza 0.1 para notar mejor los cambios producidos
	float nu = 0.1;
	float dx = 1.0;
	float dt = 0.2;
	float alpha = dt/(dx*dx);	

	// CASO 1 // 

	// CONDICIONES DE FRONTERA FIJAS //	

	int i,j;

	float Temp[100][100];
       	inicializar(100.0, 50.0, Temp);
       
	FILE *fijas1_0 = fopen("fijas_caso1_0.txt", "w+");	
	FILE *fijas1_2500 = fopen("fijas_caso1_2500.txt", "w+");
	FILE *fijas1_100 = fopen("fijas_caso1_100.txt", "w+");
	FILE *fijas1_prom = fopen("fijas_caso1_prom.txt", "w+");

	imprimirEnArchivo(fijas1_0, Temp);
	fclose(fijas1_0);
	
	fprintf(fijas1_prom, "%f %f \n", 0.0, promedio(Temp)); 
	
	for(i=0; i<(2500/dt);i++)
	{	
		solverFijas1(nu, alpha, Temp);
		
		if(i==(100/dt-1))
		{	
			imprimirEnArchivo(fijas1_100, Temp);
		}

		if(i==(2500/dt-1))
		{
			imprimirEnArchivo(fijas1_2500, Temp);
		}

		fprintf(fijas1_prom, "%f %f \n", dt*(i+1), promedio(Temp));	
	}

	fclose(fijas1_100);
	fclose(fijas1_2500);
	fclose(fijas1_prom);


	// CONDICIONES DE FRONTERA ABIERTAS //

	inicializar(100.0, 50.0, Temp);

	FILE *abiertas1_0 = fopen("abiertas_caso1_0.txt", "w+");	
	FILE *abiertas1_2500 = fopen("abiertas_caso1_2500.txt", "w+");
	FILE *abiertas1_100 = fopen("abiertas_caso1_100.txt", "w+");
	FILE *abiertas1_prom = fopen("abiertas_caso1_prom.txt", "w+");

	imprimirEnArchivo(abiertas1_0, Temp);
	fclose(abiertas1_0);
	
	fprintf(abiertas1_prom, "%f %f \n", 0.0, promedio(Temp)); 
	
	for(i=0; i<(2500/dt);i++)
	{	
		solverAbiertas1(nu, alpha, Temp);
		
		if(i==(100/dt-1))
		{	
			imprimirEnArchivo(abiertas1_100, Temp);
		}

		if(i==(2500/dt-1))
		{
			imprimirEnArchivo(abiertas1_2500, Temp);
		}

		fprintf(abiertas1_prom, "%f %f \n", dt*(i+1), promedio(Temp));	
	}
	
	fclose(abiertas1_100);
	fclose(abiertas1_2500);
	fclose(abiertas1_prom);

	// CONDICIONES DE FRONTERA PERIODICAS //

	
	inicializar(100.0, 50.0, Temp);

	FILE *periodicas1_0 = fopen("periodicas_caso1_0.txt", "w+");	
	FILE *periodicas1_2500 = fopen("periodicas_caso1_2500.txt", "w+");
	FILE *periodicas1_100 = fopen("periodicas_caso1_100.txt", "w+");
	FILE *periodicas1_prom = fopen("periodicas_caso1_prom.txt", "w+");

	imprimirEnArchivo(periodicas1_0, Temp);
	fclose(periodicas1_0);
	
	fprintf(periodicas1_prom, "%f %f \n", 0.0, promedio(Temp)); 
	
	for(i=0; i<(2500/dt);i++)
	{	
		solverPeriodicas1(nu, alpha, Temp);
		
		if(i==(100/dt-1))
		{	
			imprimirEnArchivo(periodicas1_100, Temp);
		}

		if(i==(2500/dt-1))
		{
			imprimirEnArchivo(periodicas1_2500, Temp);
		}

		fprintf(periodicas1_prom, "%f %f \n", dt*(i+1), promedio(Temp));	
	}
	
	fclose(periodicas1_100);
	fclose(periodicas1_2500);
	fclose(periodicas1_prom);
	

	// CASO 2 ------------------------------------------------------------//

	// CONDICIONES DE FRONTERA FIJAS //

       	inicializar(100.0, 50.0, Temp);
       
	FILE *fijas2_0 = fopen("fijas_caso2_0.txt", "w+");	
	FILE *fijas2_2500 = fopen("fijas_caso2_2500.txt", "w+");
	FILE *fijas2_100 = fopen("fijas_caso2_100.txt", "w+");
	FILE *fijas2_prom = fopen("fijas_caso2_prom.txt", "w+");

	imprimirEnArchivo(fijas2_0, Temp);
	fclose(fijas2_0);
	
	fprintf(fijas2_prom, "%f %f \n", 0.0, promedio(Temp));
		
	for(i=0; i<(2500/dt);i++)
	{	
		solverFijas2(nu, alpha, Temp);
		
		if(i==(100/dt-1))
		{	
			imprimirEnArchivo(fijas2_100, Temp);
		}

		if(i==(2500/dt-1))
		{
			imprimirEnArchivo(fijas2_2500, Temp);
		}

		fprintf(fijas2_prom, "%f %f \n", dt*(i+1), promedio(Temp));	
	}

	fclose(fijas2_100);
	fclose(fijas2_2500);
	fclose(fijas2_prom);

	// CONDICIONES DE FRONTERA ABIERTAS //

	inicializar(100.0, 50.0, Temp);

	FILE *abiertas2_0 = fopen("abiertas_caso2_0.txt", "w+");	
	FILE *abiertas2_2500 = fopen("abiertas_caso2_2500.txt", "w+");
	FILE *abiertas2_100 = fopen("abiertas_caso2_100.txt", "w+");
	FILE *abiertas2_prom = fopen("abiertas_caso2_prom.txt", "w+");

	imprimirEnArchivo(abiertas2_0, Temp);
	fclose(abiertas2_0);
	
	fprintf(abiertas2_prom, "%f %f \n", 0.0, promedio(Temp)); 
	
	for(i=0; i<(2500/dt);i++)
	{	
		solverAbiertas2(nu, alpha, Temp);
		
		if(i==(100/dt-1))
		{	
			imprimirEnArchivo(abiertas2_100, Temp);
		}

		if(i==(2500/dt-1))
		{
			imprimirEnArchivo(abiertas2_2500, Temp);
		}

		fprintf(abiertas2_prom, "%f %f \n", dt*(i+1), promedio(Temp));	
	}
	
	fclose(abiertas2_100);
	fclose(abiertas2_2500);
	fclose(abiertas2_prom);

	// CONDICIONES DE FRONTERA PERIODICAS //

	inicializar(100.0, 50.0, Temp);

	FILE *periodicas2_0 = fopen("periodicas_caso2_0.txt", "w+");	
	FILE *periodicas2_2500 = fopen("periodicas_caso2_2500.txt", "w+");
	FILE *periodicas2_100 = fopen("periodicas_caso2_100.txt", "w+");
	FILE *periodicas2_prom = fopen("periodicas_caso2_prom.txt", "w+");

	imprimirEnArchivo(periodicas2_0, Temp);
	fclose(periodicas2_0);
	
	fprintf(periodicas2_prom, "%f %f \n", 0.0, promedio(Temp)); 
	
	for(i=0; i<(2500/dt);i++)
	{	
		solverPeriodicas2(nu, alpha, Temp);
		
		if(i==(100/dt-1))
		{	
			imprimirEnArchivo(periodicas2_100, Temp);
		}

		if(i==(2500/dt-1))
		{
			imprimirEnArchivo(periodicas2_2500, Temp);
		}

		fprintf(periodicas2_prom, "%f %f \n", dt*(i+1), promedio(Temp));	

	}
	
	fclose(periodicas2_100);
	fclose(periodicas2_2500);
	fclose(periodicas2_prom);

	return 0;
        
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


float promedio(float T[100][100])
{
	int i,j;
        float mean;
	mean = 0.0;
                                	
	for(i=0; i<100; i++)
	{
		for(j=0; j<100; j++)
		{                                       
			mean+=T[i][j];
		}
	}
	
	return (float)(mean/(100.0*100.0));
	
}

void solverFijas1(float nu, float alpha, float T[100][100])
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

}

void solverFijas2(float nu, float alpha, float T[100][100])
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

}


void solverAbiertas1(float nu, float alpha, float T[100][100])
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

	//Esquinas
	T[0][0] = nu*alpha*(2*T_past[0][1] + 2*T_past[1][0] - 4*T_past[0][0])+T_past[0][0];
        T[100][0] = nu*alpha*(2*T_past[100][1] + 2*T_past[99][0] - 4*T_past[100][0])+T_past[100][0];
        T[0][100] = nu*alpha*(2*T_past[0][99] + 2*T_past[1][100] - 4*T_past[0][100])+T_past[0][100];
        T[100][100] = nu*alpha*(2*T_past[100][99] + 2*T_past[99][100] - 4*T_past[100][100]+T_past[0][0]);

	for(i=0;i<100;i++)
	{
		for(j=0;j<100;j++)
		{
			if(i==0 && j>0 && j<100)
			{
				T[i][j] = nu*alpha*(T_past[i][j+1] + T_past[i][j-1] + 2*T_past[i+1][j] - 4*T_past[i][j]) + T_past[i][j];
			}

			if(i==100 && j>0 && j<100)
			{	
				T[i][j] = T_past[i][j] + nu*alpha*(T_past[i][j+1] + T_past[i][j-1] + 2*T_past[i-1][j] - 4*T_past[i][j]);
			}

			if(i>0 && i<100 && j>0 && j<100)
			{
				T[i][j] = nu*alpha*(T_past[i][j+1] + T_past[i][j-1] + T_past[i+1][j] + T_past[i-1][j] - 4*T_past[i][j])+T_past[i][j];
			}
			if(j==0 && i>0 && i<100)
			{
				T[i][j] = nu*alpha*(2*T_past[i][j+1] + T_past[i+1][j] + T_past[i-1][j] - 4*T_past[i][j])+ T_past[i][j];
			}
			if(j==100 && i>0 && i<100)
			{
				T[i][j] = nu*alpha*(2*T_past[i][j-1] + T_past[i+1][j] + T_past[i-1][j] - 4*T_past[i][j])+T_past[i][j];
			}
		}
	}
}


void solverAbiertas2(float nu, float alpha, float T[100][100])
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

	//Esquinas
	T[0][0] = nu*alpha*(2*T_past[0][1] + 2*T_past[1][0] - 4*T_past[0][0])+T_past[0][0];
	T[100][0] = nu*alpha*(2*T_past[100][1] + 2*T_past[99][0] - 4*T_past[100][0])+T_past[100][0];
	T[0][100] = nu*alpha*(2*T_past[0][99] + 2*T_past[1][100] - 4*T_past[0][100])+T_past[0][100];
	T[100][100] = nu*alpha*(2*T_past[100][99] + 2*T_past[99][100] - 4*T_past[100][100]+T_past[0][0]);

	for(i=0;i<100;i++)
	{
		for(j=0;j<100;j++)
		{
			if(!(i>=20 && i<40 && j>=45 && j<55))
			{
				if(i==0 && j>0 && j<100)
				{
					T[i][j] = nu*alpha*(T_past[i][j+1] + T_past[i][j-1] + 2*T_past[i+1][j] - 4*T_past[i][j]) + T_past[i][j];
				}

				if(i==100 && j>0 && j<100)
				{	
					T[i][j] = T_past[i][j] + nu*alpha*(T_past[i][j+1] + T_past[i][j-1] + 2*T_past[i-1][j] - 4*T_past[i][j]);
				}
	
				if(i>0 && i<100 && j>0 && j<100)
				{
					T[i][j] = nu*alpha*(T_past[i][j+1] + T_past[i][j-1] + T_past[i+1][j] + T_past[i-1][j] - 4*T_past[i][j])+T_past[i][j];	
				}
				if(j==0 && i>0 && i<100)
				{
					T[i][j] = nu*alpha*(2*T_past[i][j+1] + T_past[i+1][j] + T_past[i-1][j] - 4*T_past[i][j])+ T_past[i][j];
				}
				if(j==100 && i>0 && i<100)
				{
					T[i][j] = nu*alpha*(2*T_past[i][j-1] + T_past[i+1][j] + T_past[i-1][j] - 4*T_past[i][j])+T_past[i][j];
				}
			}
		}
	}	
}

int calcularModulo(int i, int j)
{	
	int m;
	if(j > 0)  
	{ 
		m = i % j;
	}
	else
	{
		m = i % -j;
	}
	if(m < 0)
	{
		m += j;
	}
	return m;
}


void solverPeriodicas1(float nu, float alpha, float T[100][100])
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

	for(i=0;i<100;i++)
	{
		for(j=0;j<100;j++)
		{
			T[i][j] = nu*alpha*(T_past[i][calcularModulo(j+1, 100)] + T_past[i][calcularModulo(j-1,100)] + T_past[calcularModulo(i+1,100)][j] + T_past[calcularModulo(i-1,100)][j] - 4*T_past[i][j]) + T_past[i][j];
			
		}


	}


}

void solverPeriodicas2(float nu, float alpha, float T[100][100])
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

	for(i=0;i<100;i++)
	{
		for(j=0;j<100;j++)
		{
			if(!(i>=20 && i<40 && j>=45 && j<55))
			{
				T[i][j] = nu*alpha*(T_past[i][calcularModulo(j+1, 100)] + T_past[i][calcularModulo(j-1,100)] + T_past[calcularModulo(i+1,100)][j] + T_past[calcularModulo(i-1,100)][j] - 4*T_past[i][j]) + T_past[i][j];
			
			}
		}
	}
}
