#include <iostream>
#include <chrono>
#include <random>

const int N=1;
const int k_size = 400;

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

void update_model(int (&k)[k_size][k_size],int walls, dislocation (&a)[N]){
    int step[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    int step_x;
    int step_y;
    int var;
    for (int i=0;i<=N-1;i+=1){
        if (a[i].move==0){
            break;
        }
        if ((a[i].x==0)or(a[i].x>=walls-1)or(a[i].y==0)or(a[i].y>=walls-1)){
            a[i].move = 0;
        } else if (k[a[i].x+1][a[i].y]+k[a[i].x-1][a[i].y]+k[a[i].x][a[i].y-1]+k[a[i].x][a[i].y+1]>=1){
            a[i].move = 0;
        }
    }
    for (int i=0;i<=N-1;i+=1){
        if (a[i].move==0){
            break;
        }
        var = dstr2(rng);
        step_x = step[var][0];
        step_y = step[var][1];
        if (k[a[i].x+step_x][a[i].y+step_y]!=1){
            k[a[i].x+step_x][a[i].y+step_y]=1;
            k[a[i].x][a[i].y]=0;
            a[i].x += step_x;
            a[i].y += step_y;    
        }
    }
}

int main(){
int kristal[k_size][k_size] = {0};
int moving_dis = N;
dislocation dislocations[N];
float T = 0;

for (int j=10;j<=k_size;j+=10){
std::uniform_int_distribution <unsigned> dstrx ( 0 , j-1 );
std::uniform_int_distribution <unsigned> dstry ( 0 , j-1 );
//здесь создаётся новый массив
dislocations[0].move = 1;
dislocations[0].y = dstry(rng);
dislocations[0].x = dstrx(rng);
int kristal[k_size][k_size] = {0};
kristal[dislocations[0].x][dislocations[0].y]=1;
T=0;
moving_dis = 1;
//Далее 10 прогонов
auto begin = std::chrono::steady_clock::now( );
for (int q=0;q<20;q+=1){
while (moving_dis!=0){
    update_model(kristal, j, dislocations);
    moving_dis = 0;
    for (int p=0;p<=N-1;p+=1){
        moving_dis+=dislocations[p].move;
    }
}
//обновляет эксперимент
dislocations[0].move = 1;
moving_dis = 1;
dislocations[0].x = dstrx(rng);
dislocations[0].y = dstry(rng);
int kristal[k_size][k_size] = {0};
kristal[dislocations[0].x][dislocations[0].y]=1;
}
auto end = std::chrono::steady_clock::now( );
auto time_span = std::chrono::duration_cast<std::chrono::microseconds>(end - begin );
T=time_span.count()/20;
std::cout<<j<<","<<T<<'\n';
}}