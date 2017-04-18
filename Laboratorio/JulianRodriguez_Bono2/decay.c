#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float delta_n_step(float n, float lambda, float dt);
float* single_decay(float N0, float lambda, float dt);
void promedio(float N0, float lambda, float dt);

int main(){

	float N_0 = 100.0;
	float Lambda = 1.0/2.0;
	float Dt = 0.001;

	srand48(1);
	
	promedio(N_0, Lambda, Dt);
		
	return 0;
}

float delta_n_step(float n, float lambda, float dt){
	
	float rand_num = drand48();
	if(rand_num < lambda*n*dt){
		return -1.0;
	} else {
		return 0.0;
	}
}
	
float* single_decay(float N0, float lambda, float dt){

	float t_total = 5.0/lambda;
	int n_points = (int)t_total/dt;
	int i;
	
	float t = 0.0;
	float n = N0;

	float *p = malloc(n_points*sizeof(float));
	
	for(i=0;i<n_points;i++){
	
		t += dt;
		float delta_n = delta_n_step(n, lambda, dt);
		n +=delta_n;
		p[i] = n;
				
	}
	return p;
}

void promedio(float N0, float lambda, float dt){
	
	float t_total = 5.0/lambda;
	int n_points = (int)t_total/dt;	
	float t = 0.0;	
	float n=N0;

	float *tiempo = malloc(n_points*sizeof(float));
	float *prom = malloc(n_points*sizeof(float));
	
	FILE *out = fopen("data_rand.txt","w+");
	
	fprintf(out,"%f %f\n",t,n);

	int i;
	for(i=0;i<n_points;i++){
		t += dt;
		tiempo[i] = t;
	}

	int j;
	for(j=0;j<n_points;j++)
	{
		prom[j]=0.0;
	}

	float *a = malloc(n_points*sizeof(float));

	for(i=0;i<500;i++)
	{
		a = single_decay(N0, lambda, dt);
		for(j=0;j<n_points;j++) {
			prom[j] += a[j]/500;
			}
	}
	
	
	int k;
	for(k=0;k<n_points;k++){

		fprintf(out,"%f %f\n", tiempo[k], prom[k]);
	}

}
