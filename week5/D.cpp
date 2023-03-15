#include <iostream>

using std::cin;

void input_array(int* ptr, size_t N){
    for (int i =0;i<=N-1;i+=1){
        std::cin>>*ptr;
        ptr+=1;
    }
}
void reverse(int* ptr, size_t N){
        int tmp;
        int *ptrptr=ptr+N-1;
    for (int i =0;i<=N/2-1;i+=1){
        tmp=*ptr;
        *ptr = *(ptrptr-i);
        *(ptrptr-i) = tmp;
        ptr+=1;
    }
}
void print(const int* ptr, size_t N){
    for (int i =0;i<=N-1;i+=1){
        std::cout<<*ptr;
        ptr+=1;
    }
}


int main() {
    size_t N = 0;
    int* ptr = nullptr;
    cin >> N;
    int * arr = new int[N];
    ptr = &arr[0];
    input_array(ptr, N);
    ptr = &arr[0];
    reverse(ptr, N);
    ptr = &arr[0];
    print(ptr, N);
    delete[] arr;
    return 0;
}