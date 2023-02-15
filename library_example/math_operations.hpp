
#ifndef MATHOPERATIONS_HPP
#define MATHOPERATIONS_HPP

namespace math_operations{
    extern "C"
    int add_ints(int addend_1, int addend_2);
    extern "C"
    double multiply_doubles(double factor_1, double factor_2);
    extern "C"
    float mean_floats(float arr[], int array_size);
}

#endif
