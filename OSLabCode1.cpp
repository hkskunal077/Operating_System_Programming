#include<bits/stdc++.h>
using namespace std; 

void WaitTime(int proc[], int n, int exec_timing[],int wait_timing[], int arrival_timing[]) 
{ 
	int running_timing[n]; 
	running_timing[0] = 0; 
	wait_timing[0] = 0; 

	
	for (int i = 1; i < n ; i++) 
	{	running_timing[i] = running_timing[i-1] + exec_timing[i-1]; 		
		wait_timing[i] = running_timing[i] - arrival_timing[i]; 		
		if (wait_timing[i] < 0) 
			wait_timing[i] = 0; 
	} 
} 
void TurnTime(int proc[], int n, int exec_timing[],int wait_timing[], int turnaround_timing[]) 
{	for (int i = 0; i < n ; i++) 
		turnaround_timing[i] = exec_timing[i] + wait_timing[i]; 
} 
void findtime(int proc[], int n, int exec_timing[], int arrival_timing[]) 
{ 
	int wait_timing[n], turnaround_timing[n]; 
	WaitTime(proc, n, exec_timing, wait_timing, arrival_timing); 	
	TurnTime(proc, n, exec_timing, wait_timing, turnaround_timing); 

 
	int total_wait_timing = 0, total_turnaround_timing = 0; 
	for (int i = 0 ; i < n ; i++) 
	{ 
		total_wait_timing = total_wait_timing + wait_timing[i]; 
		total_turnaround_timing = total_turnaround_timing + turnaround_timing[i]; 
		int compl_time = turnaround_timing[i] + arrival_timing[i]; 
		
	} 

	cout << "Waiting Timings (AVG)= "<< (float)total_wait_timing / (float)n; 
	cout << "\nTurn Around Timings (AVG)= "<< (float)total_turnaround_timing / (float)n<<endl; 
} 
int main() 
{ 
	int proc[] = {1, 2, 3}; 
	int n = sizeof proc / sizeof proc[0]; 
	int arrival_timing[] = {1,3,5}; 
	int execution_timing[] = {4,2,3}; 	
	findtime(proc, n, execution_timing, arrival_timing); 

	return 0; 
} 


