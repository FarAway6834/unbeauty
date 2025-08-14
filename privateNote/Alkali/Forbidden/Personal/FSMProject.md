# 아 씨발 안해. 기계어에 가져가기 드럽게 힘들고 점프쓰기 드럽게 힘드네, 점프 안쓸꺼면 왜 기계어에 만들어놨는데.

## include/crazy_table/use.h
```c
#pragma once
#ifndef _USE_H
#define _USE_H(...) const jmp_table use = cod(__VA_ARGV__);
#include <crazy_table/type_CardesianPlainLongLong.h>
#include <crazy_table/mad_table.h>

//code s.t. (rax, rbx) = f(rax, rbx) s.t. f(x, y) = (madtable(x, y), madtable(x, y))

inline void add(crazy_type* x, crazy_type* y) {
    x->type_CardesianPlainLongLong = mad_table.add.type_CardesianPlainLongLong[x->indexer][y->indexer];
    y->type_long_double = mad_table.add.type_long_double[x->indexer][y->indexer];
};

inline void sub(crazy_type* x, crazy_type* y) {
    x->type_CardesianPlainLongLong = mad_table.sub.type_CardesianPlainLongLong[x->indexer][y->indexer];
    y->type_long_double = mad_table.sub.type_long_double[x->indexer][y->indexer];
};

inline void mul(crazy_type* x, crazy_type* y) {
    x->type_CardesianPlainLongLong = mad_table.mul.type_CardesianPlainLongLong[x->indexer][y->indexer];
    y->type_long_double = mad_table.mul.type_long_double[x->indexer][y->indexer];
};

inline void div(crazy_type* x, crazy_type* y) {
    x->type_CardesianPlainLongLong = mad_table.div.type_CardesianPlainLongLong[x->indexer][y->indexer];
    y->type_long_double = mad_table.div.type_long_double[x->indexer][y->indexer];
};

inline void mod(crazy_type* x, crazy_type* y) {
    x->type_CardesianPlainLongLong = mad_table.mod.type_CardesianPlainLongLong[x->indexer][y->indexer];
    y->type_long_double = mad_table.mod.type_long_double[x->indexer][y->indexer];
};

typedef struct {
    void* add;
    void* sub;
    void* mul;
    void* div;
    void* mod;
} jmp_table;

inline jmp_table cod(void** w, crazy_type* x, crazy_type* y, void** z) {
    static jmp_table ret = {.add = &&add; .sub = &&sub; .mul = &&mul; .div = &&div; .mod = &&mod;};
    
    return ret;
    
    goto w;
    
    add:
    add(x, y);
    goto z;
    sub:
    sub(x, y);
    goto z;
    mul:
    mul(x, y);
    goto z;
    div:
    div(x, y);
    goto z;
    mod: mod(x, y);
    goto z;
}

#endif
```

## include/crazy_table/type_CardesianPlainLongLong.h
```c
#pragma once
#ifndef _TYPE_CARDESIANPLAINLONGLONG_H
#define _TYPE_CARDESIANPLAINLONGLONG_H
typedef struct {
    long long x;
    long long y;
} CardesianPlainLongLong;

typedef union {
    size_t indexer;
    CardesianPlainLongLong type_CardesianPlainLongLong;
    long double type_long_double;
} crazy_type;
#endif
```

## include/crazy_table/mad_table.h
```cpp
#pragma once

#ifndef _cplusplus
extern "C" {
#endif

#ifndef _MAD_TABLE_H
#define _MAD_TABLE_H

import cmath;
#include <crazy_table/type_CardesianPlainLongLong.h>

typedef struct {
    struct add {
        CardesianPlainLongLong type_CardesianPlainLongLong[sizeof(CardesianPlainLongLong)][sizeof(CardesianPlainLongLong)];
        long double type_long_double[sizeof(long double)][sizeof(long double)];
    };
    struct sub {
        CardesianPlainLongLong type_CardesianPlainLongLong[sizeof(CardesianPlainLongLong)][sizeof(CardesianPlainLongLong)];
        long double type_long_double[sizeof(long double)][sizeof(long double)];
    };
    struct mul {
        CardesianPlainLongLong type_CardesianPlainLongLong[sizeof(CardesianPlainLongLong)][sizeof(CardesianPlainLongLong)];
        long double type_long_double[sizeof(long double)][sizeof(long double)];
    };
    struct div {
        CardesianPlainLongLong type_CardesianPlainLongLong[sizeof(CardesianPlainLongLong)][sizeof(CardesianPlainLongLong)];
        long double type_long_double[sizeof(long double)][sizeof(long double)];
    };
    struct mod {
        CardesianPlainLongLong type_CardesianPlainLongLong[sizeof(CardesianPlainLongLong)][sizeof(CardesianPlainLongLong)];
        long double type_long_double[sizeof(long double)][sizeof(long double)];
    };
} TooBig;

constexpr TooBig gen_table(void) {
    TooBig ret;
    
    crazy_type i, j;
    
    for (i.indexer = 0; i < sizeof(long double); i++) {
        for (j.indexer = 0; j < sizeof(long double); j++) {
            ret.add.type_CardesianPlainLongLong[i.indexer][j.indexer].x = i.type_CardesianPlainLongLong.x + j.type_CardesianPlainLongLong.x;
            ret.add.type_CardesianPlainLongLong[i.indexer][j.indexer].y = i.type_CardesianPlainLongLong.y + j.type_CardesianPlainLongLong.y;
            ret.sub.type_CardesianPlainLongLong[i.indexer][j.indexer].x = i.type_CardesianPlainLongLong.x - j.type_CardesianPlainLongLong.x;
            ret.sub.type_CardesianPlainLongLong[i.indexer][j.indexer].y = i.type_CardesianPlainLongLong.y - j.type_CardesianPlainLongLong.y;
            ret.mul.type_CardesianPlainLongLong[i.indexer][j.indexer].x = i.type_CardesianPlainLongLong.x * j.type_CardesianPlainLongLong.x;
            ret.mul.type_CardesianPlainLongLong[i.indexer][j.indexer].y = i.type_CardesianPlainLongLong.y * j.type_CardesianPlainLongLong.y;
            ret.div.type_CardesianPlainLongLong[i.indexer][j.indexer].x = i.type_CardesianPlainLongLong.x / j.type_CardesianPlainLongLong.x;
            ret.div.type_CardesianPlainLongLong[i.indexer][j.indexer].y = i.type_CardesianPlainLongLong.y / j.type_CardesianPlainLongLong.y;
            ret.mod.type_CardesianPlainLongLong[i.indexer][j.indexer].x = i.type_CardesianPlainLongLong.x % j.type_CardesianPlainLongLong.x;
            ret.mod.type_CardesianPlainLongLong[i.indexer][j.indexer].y = i.type_CardesianPlainLongLong.y % j.type_CardesianPlainLongLong.y;
        };
        ret.add.type_long_long[i.indexer][j.indexer] = i.type_long_long + j.type_long_long;
        ret.sub.type_long_long[i.indexer][j.indexer] = i.type_long_long - j.type_long_long;
        ret.mul.type_long_long[i.indexer][j.indexer] = i.type_long_long * j.type_long_long;
        ret.div.type_long_long[i.indexer][j.indexer] = i.type_long_long / j.type_long_long;
    };
        ret.mod.type_long_long[i.indexer][j.indexer] = fmod(i.type_long_long, j.type_long_long);
    };
    
    return ret;
}

constexpe TooBig mad_table_holder = gen_table();

extern "C" const TooBig mad_table = mad_table_holder;
#endif

#ifndef _cplusplus
}
#endif
```