#include<iostream> 
using namespace std; 

void WaitTime(int processes[], int n, int bt[], 
								int wt[], int at[]) 
{ 
	int service_time[n]; 
	service_time[0] = 0; 
	wt[0] = 0; 

	
	for (int i = 1; i < n ; i++) 
	{ 
		
		service_time[i] = service_time[i-1] + bt[i-1]; 

		
		wt[i] = service_time[i] - at[i]+1; 

		
		if (wt[i] < 0) 
			wt[i] = 0; 
	} 
} 


void TurnTime(int processes[], int n, int bt[], 
									int wt[], int tat[]) 
{ 
	// Calculating turnaround time by adding bt[i] + wt[i] 
	for (int i = 0; i < n ; i++) 
		tat[i] = bt[i] + wt[i]; 
} 

// Function to calculate average waiting and turn-around 
// times. 
void findtime(int processes[], int n, int bt[], int at[]) 
{ 
	int wt[n], tat[n]; 

	// Function to find waiting time of all processes 
	WaitTime(processes, n, bt, wt, at); 

	// Function to find turn around time for all processes 
	TurnTime(processes, n, bt, wt, tat); 

	// Display processes along with all details 
	cout << "Processes " << " Burst Time " << " Arrival Time "
		<< " Waiting Time " << " Turn-Around Time "
		<< " Completion Time \n"; 
	int total_wt = 0, total_tat = 0; 
	for (int i = 0 ; i < n ; i++) 
	{ 
		total_wt = total_wt + wt[i]; 
		total_tat = total_tat + tat[i]; 
		int compl_time = tat[i] + at[i]; 
		cout << " " << i+1 << "\t\t" << bt[i] << "\t\t"
			<< at[i] << "\t\t" << wt[i] << "\t\t "
			<< tat[i] << "\t\t " << compl_time << endl; 
	} 

	cout << "Average waiting time = "
		<< (float)total_wt / (float)n; 
	cout << "\nAverage turn around time = "
		<< (float)total_tat / (float)n; 
} 

// Driver code 
int main() 
{ 
	// Process id's 
	int processes[] = {1, 2, 3}; 
	int n = sizeof processes / sizeof processes[0]; 

	// Burst time of all processes 
	int burst_time[] = {6, 2, 1}; 

	// Arrival time of all processes 
	int arrival_time[] = {1, 3 , 4}; 

	findtime(processes, n, burst_time, arrival_time); 

	return 0; 
} 


