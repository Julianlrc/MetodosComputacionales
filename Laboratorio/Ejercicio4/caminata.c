#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float paso();
float* caminata();
void n_caminatas();

int main(){

        srand48(1);

        n_caminatas();

        return 0;
}

float paso(){

        float rand_num = drand48();
        if(rand_num < 0.5){
                return -1.0;
        }
	 else {
                return 1.0;
        }
}
float* caminata(){

        int i;

        float x = 0.0;

        float *pasos = malloc(500*sizeof(float));
	pasos[0] = x;

        for(i=1;i<500;i++)
	{
                float step = paso();
                x+=step;
                pasos[i] = x;

        }
        return pasos;
}

void n_caminatas(){

	
	FILE *out = fopen("random_walks.txt", "w+");
        int i;
	for(i=0; i < 100000; i++)
	{
		float *walk = malloc(500*sizeof(float));
		walk = caminata();
		fprintf(out, "%f\n", walk[499]);
		
	}

}

