/* ------------------------------------------------ ---------------------- */
/* Xmtc.c Calculation of PI with my Monte Carlo method (Simul random) */
/* */
/* This very powerful method is not effective for the calculation of PI */
/* remains interesting to see that we can approach PI with numbers */
/* random. */
/* ------------------------------------------------ ---------------------- */

#include <stdio.h>
#include <cstdlib>
#include <cmath>
#include <ctime>
/* ------------------------------------------------ ---------------------- */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <limits.h>
#include <unistd.h>
#include <cstring>
#include "Random/CLHEP/Random/MTwistEngine.h"
using namespace std;


#define MAX 600 

static int num = 0;
const int sizeOfMT = 624;

int myMT[sizeOfMT];
/* ------------------------------------------------ ---------------------- */
void MyPosterGraphics();

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
	int numberToDraw = 10;
	
	// Creation of a random stream using MT
	CLHEP::MTwistEngine * rs = new CLHEP::MTwistEngine();
	
	for (int j = 1; j <= numberToDraw; j++)
	{
		string nameOfFile = "Time" ;
		nameOfFile.append(to_string(j));
		rs->saveStatus(nameOfFile.c_str());
		printf("Time%dth:", j);		
		MyPosterGraphics();
		//rs->restoreStatus(nameOfFile.c_str());
	}
	delete rs;
	return 0;
}


/* ------------------------------------------------ ---------------------- */
/* PI Computation Part */
/* ------------------------------------------------ ---------------------- */

void MyPosterGraphics()
{                 
   #define MAXX 500000
   #define MAXXF 599.
   #define MAXYF 599.

   //cout << (num++) << endl;

   long i, cumulative = 0; 
   double x, y, pi;              
   int px, py;
	

   srand ((int)time(NULL));

   for (i = 0; i <MAXX; i ++)
   {
      x = (double) rand () / (double) RAND_MAX;
      y = (double) rand () / (double) RAND_MAX;
      if (((x-1) * (x-1) + (y-1) * (y-1)) <= 1) 
		cumulative ++;
	  
      px = (int) (x * MAXXF);
      py = (int) (y * MAXYF);
   }
   
   pi = ((double) cumulative * 4. / MAXX);
   printf ("%d points, Approx of PI =%f, Approx Err:%f \n", MAXX, pi , 3.14159 - pi);
   
}
