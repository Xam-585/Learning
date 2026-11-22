#include <stdio.h>
#include "hash.h"


long int calculate_hash(const char *key,int table_size){
    long long int hash = 0;
    //Check if key is not NULL and table_size > 0
    if (key && table_size > 0){
        size_t i = 0;
        int multiplicator = 31;
        if (table_size == multiplicator){
            multiplicator = 17;
        }
        // Iterate through each character in the key string till the null terminator is reached
        while (key[i] != '\0'){
            size_t value = (unsigned char)key[i];
            //Using a prime number for better distribution
            hash = (hash* multiplicator + (value %table_size))%table_size;
            i++;
        }
        return hash;
    }
    else{
        // return -1 if key is NULL or table_size <= 0
        return -1;
    }
}
