#pragma once
#ifndef _MYMCR_H
# define _MYMCR_H

#define CLOSE(...) __VA_ARGS__)
#define PA(M, ...) M(__VA_ARGS__, CLOSE
#define AP PA(PA, PA)

#define CONCAT(X, Y) X##Y
#define STRINGIFY(X) #X

#define C_ CONCAT
#define _S STRINGIFY

#define PASS //pass
//*umm*//
#define enum
#define DS static
#define ST struct
#define UN union
#define CL class
#define IL inline
#define US using
#define CP concept
#define IP import
#define PR private
#define PU public
#define PO protected
#define OP operator
#define SG signed
//hehehehehehehehe
#define UG C_(un, SG)
#define PF PR:
#define UF PU:
#define OF PO:
#define FA(A, X, B, Y, C, Z) A \
	X \
	B \
	Y \
	C \
	Z

#define VR virtu
#define FN fin

#define TY type
#define NA name
#define DF def
#define SP space
#define CN const
#define _E ex
#define _A al
#define R_ r
#define EE e
#define _T t
#define _P p
#define _O o
#define _N n

#define AL(X) _C(X, _A)

#define E_(X, M) C_(C_(_E, X), C_(M, R_))
/**
  * 
  * 
  * 
  * _E is PA(PA, E_)
  * that meant it's PA(E_, ...)
  *
  **/
#define _E AP(E_)

#define PE _E(_P)
#define TE _E(_T)

#define EP PE()

#define P_ PE(_O)
#define T_ TE(EE)

#define VI AL(VR)
#define FI AL(FN)

#define AB(X) VI X = 0

#define NS C_(NA, SP)
#define TN C_(TY, NA)
#define TD C_(TY, DF)

#define CE C_(CN, EP)

#define ET T_(_N)
#define EX P_(_T)

#define TP(...) template <__VA_ARGS__>

#define pass PASS

#define LT CE DS
#define VL VI IL
#define FL FI IL
#define CV CE VI
#define CF CE FI
#define VC CE VL
#define FC CE FL
#define SI DS IL
#define VS DS VL
#define FS DS FL
#define SV DS VI
#define SF DS FI
#define PL LT VI
#define FL LT FI
#define FX LT FL
#define VX LT VL

#define AA(X) AB(IL X)
#define AG CE AB
#define LG CE AA
#define AS DS AA
#define AV DS AI
#define AC LT AI
#define AX LT AA

#define TC TD CL
#define MT TD ST
#define UT TD UN
#define PT(T) TD T*
#define FN(N, T, ...) T N (__VA_ARGS__)
#define FT(N, T, ...) TD FN((*N), T, __VA_ARGS__)
#define AT(T, L) TD T[L]

#define XT(X, ...) TP(__VA_ARGS__) X
//PA(PA, XT)(X) -> PA(XT, X)
#define TX AP(XT)
#define TS TX(ST)
#define TU TX(UN)
#define TA TX(US)
#define TC TX(CL)
#define CT TX(CP)
#define TV(T, X, SRC, ...) TA(__VA_ARGS__, T V = SRC) X = V

#define LD US NS
#define GL(N, V) N::V
#define GE(N, V) US GL(N, V)
#define AS(A, B) US A = B
#define LA(X, N, V) AS(X, GL(N, V))

#define AO(X, Y, T, ...) AA(FN(X##OP##Y, T, __VA_ARGS__))

//hehehehehehehehehehehehheheheheheehehehhehehhhhehehehe
/*dum fix*/
#define TYDF typedef
#define TYNA typename
#define unSG unsigned
#undef TS
#define TS(...) TP(__VA_ARGS__) ST
/*dum fix*/
//eeeheehhehehehehehhhehehehhehehehehehheheheehhhehhhhhhhhhehehehehehe
TD long long LL;
TD long L;
TD int D;
TD short S;
TD UG long long ULL;
TD UG long UL;
TD UG int UD;
TD UG short us;
TD long double ld;
TD long float LF;
TD double DO;
TD float F;
TD UG char UC;
TD SG char SC;
TD char C;

TS(TN T, TN G, G B) TBit {
	T v : B;
};

#endif