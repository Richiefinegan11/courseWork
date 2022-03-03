#include <stdio.h>
#include <stdlib.h>

int main() 
{
    int age = 50;

    int* p = &age;

    printf("The address of the age is %p", p);

    printf("\nThe variable is %i", *p);
    
    
}

#include <stdio.h>
//the following code shows how to access the memory address of some data
int main() {
  //first, we store some value on a variable
  int firstValue = 200;

  //we then print this value and its memory address by using the ampersand
  printf("firstValue contains %i and is stored at the memory address %p", firstValue, &firstValue);

  return 0;
}