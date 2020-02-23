#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <limits.h>
#include <unistd.h>

#include <cstring>
#include "CLHEP/Random/MTwistEngine.h"
#define MAX 100

using namespace std;

string to_string(int n)
{
	int m = n;
	char s[MAX];
	char ss[MAX];
	int i=0,j=0;
	if (n < 0)
	{
		m = 0 - m;
		j = 1;
		ss[0] = '-';
	}    
	while (m>0)
	{
		s[i++] = m % 10 + '0';
		m /= 10;
	}
	s[i] = '\0';
	i = i - 1;
	while (i >= 0)
	{
		ss[j++] = s[i--];
	}    
	ss[j] = '\0'; 
	return ss;   
}

int main ()
{
	double sum;
	double temp;
	unsigned int nbr;
	int numberToDraw = 1000000;

	// Creation of a random stream using MT
	CLHEP::MTwistEngine * rs = new CLHEP::MTwistEngine();
	
	for (int j = 1; j <= 10; j++)
	{
		sum = 0.0;
		string nameOfFile = "status" ;
		nameOfFile.append(to_string(j));
		rs->saveStatus(nameOfFile.c_str()); // Saves the current status of the RM Engine

		for(int i = 1; i < numberToDraw; i++)
		{
			temp = rs->flat(); // Draws random numbers between 0 and 1 and sum them
			sum += temp;
		}
		cout << endl << nameOfFile << ":"<< sum / numberToDraw << endl;
		//rs->restoreStatus(nameOfFile.c_str()); // Comes back to the MT Status before the loop
	}
	
	delete rs;
	return 0;
}
