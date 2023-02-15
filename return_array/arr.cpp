#include <iostream>
#include <iomanip>
#include "arr.hpp"


int* arr_return()
{
    int* information = new int[10];
    for(int k=0; k<10; k++)
    {
        information[k] = k;
    }
    return information;
}