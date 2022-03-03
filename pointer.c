#include <stdio.h>
 
int main () {

   int  var;
   int  *pVar;
   int  **ppVar;

   var = 3000;

   /* take the address of var */
   pVar = &var;

   /* take the address of ptr using address of operator & */
   ppVar = &pVar;

   /* take the value */
   printf("Value of var = %d\n", var );
   printf("Value available at *pVar = %d\n", *pVar );
   printf("Value available at **ppVar = %d\n", **ppVar);

   return 0;
}