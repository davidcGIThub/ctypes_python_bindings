#include <iostream>
#include <iomanip>
#include "summ.hpp"


int summ(int arr[], int length) 
{
    int sum{0};
    for (int i=0; i < length; i++)
    {
        sum += arr[i];
    }
    return sum;
}

