#include <stdio.h>
#include <iostream>

int main(){
	int n;
	scanf("%i",&n);
	int godhet[n];
	for (int i =0; i < n; i++){
		scanf("%i",&godhet[i]);
	}
	for (int i = 0; i <n; i++){
		std::cout << godhet[i] << std::endl;
	}
}
