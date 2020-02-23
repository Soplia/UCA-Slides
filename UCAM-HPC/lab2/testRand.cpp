#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <limits.h>
#include <unistd.h>

#include "CLHEP/Random/MTwistEngine.h"

using namespace std;

int main () 
{
	double sum;
	unsigned int nbr;
// Creation of a random stream using MT
	CLHEP::MTwistEngine * rs = new CLHEP::MTwistEngine();
	rs->saveStatus("MT-Status0"); // Saves the current status of the MT Engine
	for(int i = 1; i < 1000000; i++)
	{
		sum += rs->flat(); // Draws random numbers between 0 and 1 and sum them
	}
	cout << sum / 1000000. << endl;
	rs->restoreStatus("MT-Status0"); // Comes back to the MT Status before the loop
	delete rs;
	return 0;
}
