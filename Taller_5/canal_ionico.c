#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
	float radio = 1.0; //Armstrong

	FILE *posiciones = fopen("Canal_ionico.txt", "r");
	int i;	
	char buffer[100];
	//float *x = malloc(42*sizeof(float));
	//const char delimiter = "0";
	//char token;

	//char delimit[]=" \t\r\n\v\f";

	
	while (feof(posiciones) == 0)
 	{
 		fgets(buffer, 40, posiciones);
		printf("%s \n", buffer);
		//token = (char)strtok(buffer, delimit);
		//for(i=0; i<42; i++)
		//{
		//	x[i] = (float)token;
		//}
 		
 	}

	return 0;	
}

float calcularRadio(float x, float y)
{
	return x*x+y*y;	
}
