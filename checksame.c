#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>

typedef unsigned long long int uint64_t;

int hamming(uint64_t h1, uint64_t h2){
    int h= 0;
    uint64_t d=h1 ^ h2;
    while (d)
    {
       	h += 1;
        d &= d - 1;
    }
    return h;
}

int main(int argc, char** argv ) {

	std::ifstream ffile("info2.txt");
  
    int linecnt = 0 , cnt = 0 , iDim = 0 ;
    std::vector <std::string> fns;
    std::vector <uint64_t> feats;
    for (std::string strLine; std::getline(ffile, strLine); linecnt++)
    {
        std::istringstream iss(strLine);
        std::string strFn;
        uint64_t tmp=0;
        iss >> strFn;
        iss >> tmp;
        fns.push_back(strFn);
        feats.push_back(tmp);

    }
#pragma omp parallel
{
    // for (int i=0;i<100;i++)
    // {
    // 	std::cout<<fns[i]<<" "<<feats[i]<<std::endl;
    // }
 
#pragma omp for
    for (int i=0;i<linecnt-1;i++)
    {
    	for (int j=i+1;j<linecnt;j++)
    	{
    		if (hamming(feats[i],feats[j])<=5)
    		{
    			#pragma omp critical

    			printf("%d %d\n",i,j);
    		}
    	}
    	// if (i%100==0)
    	// {
    	// 	std::cout<<i<<std::endl;
    	// }
    }

}










}


