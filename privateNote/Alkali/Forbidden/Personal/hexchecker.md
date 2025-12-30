# hexchecker : 상상속의, 자료구조

Hexcheck자료형의 배열로, short형의 크기를 가지고 있고, short형으로 null terminate를 작동시킨다.
비트 구조는
 * even parity P 1bit
 * xor mod 1011 CRC 3 bit
 * main HEX value 4 bit
가

[P : 1][HEX : 4][CRC : 3]

구조로, 한 바이트를 표시한다.

항상 두 바이트씩 묶여있으며, 오류가 없다면, `(unsigned short) 0`인 terminate symbol 이전에 심볼은, Hexcheck2HexChecked시키면, uc인 value가 NULL이 되어야 한다.

그래야 무결성이 맞다.

참고로 아래 코드들은 의사코드다. 즉, 자연어랑 동일한 방식의 처리과정 명시라는거다.
실행용이 아니고, UB먹고싶지 않으면 실행하지 말길.
나같으면 동작이 뻔한 기계어로 짜는게 낫겠다. (수학도여서 그렇게 생각하는걸수도 있지만.)

## include/hexchecker/chexcheck.h
```c
#pragma once

#ifdef __cplusplus
extern "C" {
#endif

#ifndef _CHEXCHECK_H
#define _CHEXCHECK_H
#include <stdbool.h>
typedef unsigned char uc;
typedef unsigned short us;

typedef union {
	us shortv;
	struct {
		uc first;
		uc last;
	};
} beforeChecked;

typedef struct {
	bool vailidity
	bool firstBvalidity;
	bool lastBvalidity;
	uc value;
} afterChecked;

const struct {
	us value;
	us one_and_one;
	us CRC;
	uc CRCHEX;
	uc firster;
	union {
		uc bx[7];
		struct {
			uc b6;
			uc b5;
			uc b4;
			uc b3;
			uc end;
		};
	};
} bitmasK = {
	.one_and_one = 257,
	.CRC = 32639,
	.CRCHEX = 11,
	.value = 3855;
	.firster = 240;
	.b3 = 4,
	.b4 = 8,
	.b5 = 16,
	.b6 = 32,
	.b7 = 64,
	.end = 0
};

uc CRC(register uc x) {
	for (uc * bkstr = &bitmasK.bx; *uc; uc++) if (x & *uc) x ^= bitmasK.CRCHEX;
	return x;
}

afterChecked check_pre(register beforeChecked x, register afterChecked ret) {
	register beforeChecked y = {.shortv = x.shortv};
	for (uc shifts = 4; shifts; shifts>>=1) y.shortv ^= (x.shortv >> shitfs);
	y.shortv &= bitmasK.one_and_one;
	
	ret.firstBvalidity = !y.first;
	ret.lastBvalidity = !y.last;
	
	if (ret.validity) {
		y.shortv = x.shortv & bitmasK.CRC;
		ret.firstBvalidity &= CRC(y.first);
		ret.lastBvalidity &= CRC(y.last);
		
		y.shortv = x.shortv & bitmasK.value;
		ret.value = (y.first << 4) + y.last;
	
		ret.vailidity = ret.firstBvalidity && ret.lastBvalidity
	}
	
	return ret;
}

afterChecked check(register beforeChekced x) {
	register afterChecked ret = {.vailidity = true};
	return check_pre(x, ret);
}

beforeChecked checksum(register afterChecked x) {
	register beforeChecked ret = {.shortv = (short) x.value};
	x.validity = false;
	x = check_pre(beforeChecked);
	for (uc temp = ret.shortv & bitmasK.firster; temp; ret.shortv += temp << 4) ret.shortv -= temp;
	ret.shortv <<= 3;
	ret.first += CRC(ret.first) + ((uc) !x.firstBvalidity) * 128;
	ret.last += CRC(ret.last) + ((uc) !x.lastBvalidity) * 128;
	return ret;
}
#endif

#ifdef __cplusplus
}
#endif
```

## include/hexchecker/hexcheck.h
```cpp
#pragma once

#ifndef _HEXCHECK_H
#define _HEXCHECK_H
#include <hexchecker/chexcheck.h>

typedef struct {
	union {
		uc V;
		struct {
			bool parity_bit : 1;
			union {
				uc non_parity : 7;
				struct {
					uc value : 4;
					uc CRC : 3;
				} : 7;
			} : 7;
		} : 8;
	} : 8;
} HexcheckByteType;

typedef union {
	us shortv;
	struct {
		HexCheckType first;
		HexCheckType last;
	};
} Hexcheck;

typedef struct {
	union {
		uc validity_pad : 3;
		struct {
			bool validity : 1;
			bool firstBvalidity : 1;
			bool lastBvalidity : 1;
		} : 3;
	} : 3;
	uc value : 8;
} Hexchecked;

inline afterChecked beforeChecked2afterChecked(register beforeChecked x) {
	return check(x);
}

inline beforeChecked afterChecked2beforeChecked(register afterChecked x) {
	return checksum(x);
}

inline beforeChecked Hexcheck2beforeChecked(register Hexcheck x) {
	return (BeforeChecked) x;
}

inline Hexcheck beforeChecked2Hexcheck(register beforeChecked x) {
	return (Hexcheck) x;
}

afterChecked Hexchecked2afterChecked(register Hexchecked x) {
	register afterChecked ret = {.validity = x.validity, .firstBvalidity = x.firstBvalidity, .lastBvalidity = x.lastBvalidity, .value = x.value};
	return ret;
}

Hexchecked afterChecked2Hexchecked(register afterChecked x) {
	register Hexchecked ret = {.validity = x.validity, .firstBvalidity = x.firstBvalidity, .lastBvalidity = x.lastBvalidity, .value = x.value};
	return ret;
}

Hexcheck afterChecked2Hexcheck(register afterChecked x) {
	return beforeChecked2Hexcheck(afterChecked2beforeChecked(x));
}

afterChecked HexCheck2afterChecked(register Hexcheck x) {
	return beforeChecked2afterChecked(Hexcheck2beforeChecked(x));
}

beforeChecked HexChecked2beforeChecked(register HexChecked x) {
	return afterChecked2beforeChecked(HexChecked2afterChecked(x));
}

HexChecked beforeChecked2HexChecked(register beforeChecked x) {
	return aftetChecked2HexChecked(beforeChecked2afterChecked(x));
}

Hexcheck Hexchecked2Hexcheck(register Hexchecked x) {
	return beforeChecked2Hexcheck(HexChecked2beforeChecked(x));
}

Hexchecked Hexcheck2Hexchecked(register Hexcheck x) {
	return beforeChecked2HexChecked(Hexcheck2beforeChecked(x));
}

#endif
```