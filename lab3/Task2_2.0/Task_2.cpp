#include <iostream>
#include <chrono>
#include <random>

const int N=400;
const int k_size = 20;

unsigned seed = 10010;
std::default_random_engine rng ( seed );
std::uniform_int_distribution <unsigned> dstrx ( 0 , k_size-1 );
std::uniform_int_distribution <unsigned> dstry ( 0 , k_size-1 );
std::uniform_int_distribution <unsigned> dstr2 ( 0 , 3 );

struct dislocation{
    int move = 1;
    int x = dstrx(rng);
    int y = dstry(rng);
};

void update_model(int (&k)[k_size][k_size],int d_number,int (&step_counter), dislocation (&a)[N]){
    int step[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    int step_x;
    int step_y;
    int var;
    for (int i=0;i<=d_number-1;i+=1){
        if (a[i].move!=0){
        if ((a[i].x==0)or(a[i].x>=k_size-1)or(a[i].y==0)or(a[i].y>=k_size-1)){
            a[i].move = 0;
        } else if (k[a[i].x+1][a[i].y]+k[a[i].x-1][a[i].y]+k[a[i].x][a[i].y-1]+k[a[i].x][a[i].y+1]>=1){
            a[i].move = 0;
        }}
    }
    for (int i=0;i<=d_number-1;i+=1){
        if (a[i].move!=0){
        var = dstr2(rng);
        step_x = step[var][0];
        step_y = step[var][1];
        if (k[a[i].x+step_x][a[i].y+step_y]!=1){
            k[a[i].x+step_x][a[i].y+step_y]=1;
            k[a[i].x][a[i].y]=0;
            a[i].x += step_x;
            a[i].y += step_y;
            step_counter+=1;    
        }
        }
    }
}

int main(){
    int step_counter=0;
    int kristal[k_size][k_size] = {0};
    int moving_dis = N;
    dislocation dislocations[N];
    float T = 0;

    for (int j=1;j<=N;j+=1){
        int kristal[k_size][k_size] = {0};
        for (int i=0;i<=j-1;i+=1){
            dislocations[i].move = 1;
            dislocations[i].x=dstrx(rng);
            dislocations[i].y=dstry(rng);
            while (kristal[dislocations[i].x][dislocations[i].y]==1){
                dislocations[i].x=dstrx(rng);
                dislocations[i].y=dstry(rng);
            }
        kristal[dislocations[i].x][dislocations[i].y]=1;
        }

        T=0;
        moving_dis = j;
        step_counter = 0;

        for (int q=0;q<20;q+=1){
            while (moving_dis!=0){
                update_model(kristal, j, step_counter, dislocations);
                moving_dis = 0;
            for (int p=0;p<=j-1;p+=1){
                moving_dis+=dislocations[p].move;
            }
            }
            int kristal[k_size][k_size] = {0};
            for (int i=0;i<=j-1;i+=1){
            dislocations[i].move = 1;
            dislocations[i].x=dstrx(rng);
            dislocations[i].y=dstry(rng);
            while (kristal[dislocations[i].x][dislocations[i].y]==1){
                dislocations[i].x=dstrx(rng);
                dislocations[i].y=dstry(rng);
            }
            kristal[dislocations[i].x][dislocations[i].y]=1;
        }
        moving_dis = j;
        }
        std::cout<<j<<","<<(step_counter/20)<<'\n';
    }
}