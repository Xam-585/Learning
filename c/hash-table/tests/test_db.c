# include <stdio.h>
#include "hash.h"
#include <assert.h>


long int test_calculate_hash(){
    int result = calculate_hash("slfdnosibf",20);
    return result;
}

int main (){
    assert( test_calculate_hash() == 6);
    return 0;
}