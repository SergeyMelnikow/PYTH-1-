#include <iostream>

int main() {
    int * arr = new int[0];
    int * new_arr = arr;
    int counter = 0;
    int number = 1;
    while (number!=0){
        counter+=1;
        new_arr = new int[counter];
        for (int i=0;i<=counter-1;i+=1){
            new_arr[i]=arr[i];
        }
        std::cin>>number;
        if(number!=0){
            new_arr[counter-1]=number;
        } else {counter-=1;}
        delete[] arr;
        arr = new_arr;
    }
    for (int i=0;i<counter-1;i+=1){
        std::cout<<arr[i]-arr[i+1]<<" ";
    }
}