#include <iostream>
int main(){
    short int* a;
    short int *A=new short int [10];
    a=A;
    while(a<=A+9){
        *a=a-A;
        std::cout<<a<<" ";
        a+=1;
    }
    std::cout<< std::endl ;
    a=A;
    while(a<=A+9){
        std::cout<<*a<<" ";
        a+=1;
    }
    a=A;
    while(a<=A+9){
        *a=(*a)*(*a);
        a+=2;
    }
    std::cout<< std::endl ;
    a=A;
    while(a<=A+9){
        std::cout<<*a<<" ";
        a+=1;
    }
    delete[] A;
}