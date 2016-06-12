#include <stdio.h>
#include <unistd.h>

int main(void)
{
    long int input = 0;
    long int j = 0;
    long int max = 1000000000000000;
    
    // loop tot maximaal nummer bereikt
    for (input = 0; input <= max; input++)
    {
        // voor elk nummer (j) tot input
        for(j = 2; j < input; j++)
        {
            if(input % j != 0)
            {
                printf("%li\n", input);
                sleep(1);
            }
            break;
        }
    }
}