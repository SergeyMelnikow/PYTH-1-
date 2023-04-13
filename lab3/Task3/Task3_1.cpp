#include <iostream>
#include <chrono>
#include <random>

const int N=1;
const int k_size = 450;

unsigned seed = 1000;
std::default_random_engine rng ( seed );
std::uniform_int_distribution <unsigned> dstrx ( 0 , k_size-1 );
std::uniform_int_distribution <unsigned> dstry ( 0 , k_size-1 );
std::uniform_int_distribution <unsigned> dstr2 ( 0 , 1 );

struct dislocation{
    int move = 1;
    int x = dstrx(rng);
};

void update_model(int (&k)[k_size],int length, dislocation (&a)[N]){
    int step[2] = {{1},{-1}};
    int step_x;
    int var;
    for (int i=0;i<=N-1;i+=1){
        if (a[i].move!=0){
        if ((a[i].x==0)or(a[i].x>=length-1)){
            a[i].move = 0;
        } else if (k[a[i].x+1]+k[a[i].x-1]>=1){
            a[i].move = 0;
        }}
    }
    for (int i=0;i<=N-1;i+=1){
        if (a[i].move!=0){
        var = dstr2(rng);
        step_x = step[var];
        if (k[a[i].x+step_x]!=1){
            k[a[i].x+step_x]=1;
            k[a[i].x]=0;
            a[i].x += step_x; 
        }
    }
    }
}

int main(){
    int kristal[k_size] = {0};
    int moving_dis = N;
    dislocation dislocations[N];
    float T = 0;

    for (int j=10;j<=k_size;j+=5){
        std::uniform_int_distribution <unsigned> dstrx ( 0 , j-1 );
        std::uniform_int_distribution <unsigned> dstry ( 0 , j-1 );
        int kristal[k_size] = {0};
        for (int i=0;i<=N-1;i+=1){
            dislocations[i].move = 1;
            dislocations[i].x=dstrx(rng);
            while (kristal[dislocations[i].x]==1){
                dislocations[i].x=dstrx(rng);
            }
            kristal[dislocations[i].x]=1;
        }

        T=0;
        moving_dis = N;

        auto begin = std::chrono::steady_clock::now( );
        for (int q=0;q<20;q+=1){
            while (moving_dis!=0){
                update_model(kristal, j, dislocations);
                moving_dis = 0;
                for (int p=0;p<=N-1;p+=1){
                    moving_dis+=dislocations[p].move;
                }
            }
        int kristal[k_size] = {0};
        for (int i=0;i<=N-1;i+=1){
        dislocations[i].move = 1;
        dislocations[i].x=dstrx(rng);
        while (kristal[dislocations[i].x]==1){
            dislocations[i].x=dstrx(rng);
        }
        kristal[dislocations[i].x]=1;
        }
        moving_dis = N;
        }
    auto end = std::chrono::steady_clock::now( );
    auto time_span = std::chrono::duration_cast<std::chrono::microseconds>(end - begin );
    T=time_span.count()/20;
    std::cout<<j<<","<<T<<'\n';
    }
}