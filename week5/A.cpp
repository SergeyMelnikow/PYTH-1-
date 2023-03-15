#include <iostream>
int main(){
    double* a;
    *a=0;
    std::cout<<a<<" ";
    std::cout<<*a<<"\n";
    a-=3;
    std::cout<<a<<" ";
    std::cout<<*a<<"\n";
    a+=5;
    std::cout<<a<<" ";
    std::cout<<*a<<"\n";
}