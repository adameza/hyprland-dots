#include <stdint.h>

typedef union byte 
    {
    struct bits 
        {
        uint8_t bit_0: 1;
        uint8_t bit_1: 1;
        uint8_t bit_2: 1;
        uint8_t bit_3: 1;
        uint8_t bit_4: 1;
        uint8_t bit_5: 1;
        uint8_t bit_6: 1;
        uint8_t bit_7: 1;
        };
    uint8_t all;
} byte;