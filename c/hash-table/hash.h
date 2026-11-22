
// #ifndef HASH_H stoppes the header file from being included multiple times in a single compilation unit, which can lead to redefinition errors.
// #define HASH_H defines the macro HASH_H, which is used to check if the header file has already been included. If it has not been included, the code between #ifndef and #endif will be processed.
#ifndef HASH_H
#define HASH_H


long int calculate_hash(const char *key,int table_size);


#endif 