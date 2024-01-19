#include <stdint.h>

typedef union byte {
    typedef struct bits {
        uint8_t byte0;
        uint8_t byte1;
        uint8_t byte2;
    } bits;
} byte;