#include "Foo.hpp"

Foo::Foo(int n)
{
    val = n;
}

void Foo::bar()
{
    std::cout << "Value is " << val << std::endl;
}

int Foo::foobar(int n)
{
    return val + n;
}