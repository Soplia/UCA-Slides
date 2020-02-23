/* ------------------------------------------------ ---------------------- */
/* Xmtc.c Calculation of PI with my Monte Carlo method (Simul random) */
/* */
/* This very powerful method is not effective for the calculation of PI */
/* remains interesting to see that we can approach PI with numbers */
/* random. */
/* ------------------------------------------------ ---------------------- */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

/* ------------------------------------------------ ---------------------- */

#define MAXX 600 
#define MAXY 600 

/* ------------------------------------------------ ---------------------- */

void posterGraphics();
void MyPosterGraphics();

/* ------- Declaration of global variables ---------------------------- */


unsigned long mask; /* Declare an event mask */
unsigned long gcmask;             


/* ------------------------------------------------ ---------------------- */

int main (int argc, char * argv [])
{
	printf("PI Calculation Part\n");
	MyPosterGraphics();
	
	return 0;
}

/* ------------------------------------------------ ---------------------- */
/* PI Computation Part */
/* ------------------------------------------------ ---------------------- */

void MyPosterGraphics()
{                 
   #define MAX 500000
   #define MAXXF 599.
   #define MAXYF 599.
                 
   static int numcur = 0;
   long i, cumulative = 0; 
   double x, y, pi;              
   int px, py;

   srand (1);
   for (i = 0; i <MAX; i ++)
   {
      x = (double) rand () / (double) RAND_MAX;
      y = (double) rand () / (double) RAND_MAX;
      if (((x-1) * (x-1) + (y-1) * (y-1)) <= 1) cumulative ++;
	  
      px = (int) (x * MAXXF);
      py = (int) (y * MAXYF);
   }
   
   pi = ((double) cumulative * 4. / MAX);
   printf ("%d points, Approx of PI =%f, Approx Err:%f \n", MAX, pi , 3.14159 - pi);
}

