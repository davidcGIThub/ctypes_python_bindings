#include "math_operations.hpp"
#include <iostream>

namespace math_operations{
    int add_ints(int addend_1, int addend_2)
    {
        return addend_1 + addend_2;
    }

    double multiply_doubles(double factor_1, double factor_2)
    {
        return factor_1 * factor_2;
    }

    float mean_floats(float arr[], int array_size)
    {
        float sum = 0;
        for(int i = 0; i < array_size; i++)
        {
            sum += arr[i];
        }
        float mean = sum/array_size;
        return mean;
    }
}