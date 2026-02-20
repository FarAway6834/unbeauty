# ESOLANG인 DEPRESS 언어 명세 (with 구문에 대한 12개조항)

이전 KyuKyurarin에 대한 이야기들과 완전히 무관한 배경에서 나옴. 그냥 무식하고 단순하게 컴파일될것임. KyuKyurarin으로 개발된게 아니라서 ㅋㅋ 그냥 LLVM을 통해 기계어로 바로 컴파일될 목적으로 만들어짐 ㅋㅋ

 >
 > * Paradime : depressive disorder (KyuKyrarin의 페러다임과 같다)
 > * 만든 계기 : 재작자가 자신이 쓸모없다느껴 현타외서, "더 살아 무엇을 하겠더냐"하고 배설작을 만듬.
 > * 추가 기제 사항 : 간단한거 좋아서 이딴거 만들었다. 헤헤헤
 > 

프로그래밍 언어인 depress는 메모리 할당을 직접 관리하는 미친짓을 벌인 탓에, C/C++/Assambly로 작성되었다.
C++은 그냥 언어가 어떻게 생겼는지 보여주는 의사코드일 뿐...
메모리 할당같은 본래의 작업은 C/Assambly로 되어있으니 이건 로우레벨이다.

```
#define SYSCALL asm volatile ("syscall")
#define DEPRESSED(N, M, RO, RW) depress_t<N, M> DEPRESS = {.rodata = RO, .rwdata = RW}
#define USING_LSTACK /* 대충 LSTACK을 생성하는 코드 */
#define USING_RSTACK /* 대충 RSTACK을 생성하는 코드 */

typedef unsigned char BYTE;

template <size_t N, size_t M>
struct depress_t {
    const BYTE rodata[N];
    static BYTE rwdata[M];
    inline const BYTE* operator()(size_t idx) const {
        return &this->rodata[idx];
    }
    inline BYTE& operator[](size_t idx) {
        return &this->rwdata[idx];
    }
};

#pragma pack(push, 1)
struct StackFrame {
    StackFrame* esp;
    BYTE value[]; /* in 
};

typedef struct StackInfo {
    bool isLstack;
    size_t current_length;
    StackFrame* bp;
    StackFrame* sp;
    
    /* dprs(depress) alloc */
    inline void dprsalloc(void* start, void* end) {
        /* depress 프로그래밍 언어가, start부터 end까지 사용 가능한 영역으로 할당해줌. */
        /* OS대신 자신이 메모리를 관리라는 주체가 될수 있을정도로, OS한테, 자유 공간을 적당히 할당받아서, dprsalloc을 쓰면 C및 기계어 수준에서 해당 공간을 쓰는걸 영역 침범이 아닌걸로 간주하는 방식 */
    }
    
     /* dprs free */
     inline void dprsfree(void* ptr) {
        /* 당연히 dprs언어는 free도 여기서 한다. */
    }
   
    inline void overflow_error(StackFrame* start, StackFrame* end) {
        if (this->isLstack) {
            fprintf(stderr, "[DPRESS RUNTIME ERROR] LSTACK OVERFLOW : 「new stack frame (at [%p] ~ [%p])」 got touch the 「lstack manger (at [%p] ~ [%p])」. program aborted.", (size_t) start, (size_t) end, (size_t) this, (size_t) this + sizeof(this));
            std::abort();
        } else {
            fprintf(stderr, "[DPRESS RUNTIME ERROR] RSTACK OVERFLOW : 「new stack frame (at [%p] ~ [%p])」 got touch the 「rstack manger (at [%p] ~ [%p])」. program aborted.", (size_t) start, (size_t) end, (size_t) this, (size_t) this + sizeof(this));
            std::abort();
        }
    
    inline void underflow_error(void) {
        if (this->isLstack) {
            fprintf(stderr, "[DPRESS RUNTIME ERROR] LSTACK UNDERFLOW : 「lstack (managet at [%p])」 got underflowed. please check the 「bp (at [%p])」. program aborted.", (size_t) this, (size_t) &this->bp);
            std::abort();
        } else {
            fprintf(stderr, "[DPRESS RUNTIME ERROR] RSTACK UNDERFLOW : 「rstack (managet at [%p])」 got underflowed. please check the 「bp (at [%p])」. program aborted.", (size_t) this, (size_t) &this->bp);
            std::abort();
        }
    };
    
    inline void operator()(size_t L) {
        
    StackFrame* new_sp = (StackFrame*) ((size_t) sp + (size_t) sizeof(StackFrame) + (size_t) current_length);
        StackFrame* new_sp_end = (StackFrame*) ((size_t) new_sp + (size_t) sizeof(StackFrame) + L)
        //new_sp isn't aliable yet
        if ((this->isLstack)?(this > new_sp_end):(new_sp_end > this)) {
            this->dprsalloc((void*) new_sp, new_sp_end);
             //now new_sp is aliable
            new_sp->esp = this->sp;
            this->sp = new_sp;
        } else {
            this->StackOverflow(new_sp, new_sp_end);
        }
    }
    
    inline void operator()(void) {
        if (this->is_bp()) {
            /* delete this; //no undeflow err */ //joke
            this->UnderflowError();
        } else {
            StackFrame* esp = this->sp->esp;
            this->dprsfree(this->sp);
            this->sp = esp;
        };
    }
    
    inline bool is_bp(void) {
        return (this->sp == this->bp);
    }
    
    StackInfo(StackFrame* bp) {
        this->bp = bp;
        this->sp = bp;
        dprsalloc(bp, sizeof(StackFrame));
        this->sp->esp = bp;
        this->isLstack = (sp < this);
    };
    
    ~StackInfo(void) {
        dprsfree(bp);
    }
    
    StackInfo(bool is_lstack) {
        /* 대충 dprs alloc을 이용해서, manager가 있을 공간과 bp를 할당하는 코드 */
    }
} StackInfo;
#pragma pack(pop)
```

dpress언어에서 허용된 구문 목록
1. DEPRESSED(N, M, {배열초기화}, {배열 초기화});
2. USING_LSTACK; 및 USING_RSTACK;
3. 변수 a, b, c, d, w, x, y, z가 레지스터 순서는 a, b, c, d, w, x, y, z 순서로, 하드웨어 레지스터 배정 순서이 따라 배정됨. 하드웨어 레지스터도 나열순서가 있으니까. 다만, systemcall기준 나열로다가 만듬.
4. 객체 DEPRESS의 조작은 무제한
5. 객체 L의 조작은 무제한 (L은 LSTACK)
6. 객체 R의 조작은 무제한 (R은 RSTACK)
7. 산술연산자와 비트연산자 마음대로.
8. 메모리는 이미 DEPRESS객체와 LSTACK, RSTACK이 정했으니 이만...
9. 입출력 • 파일입출력 등은, "SYSCALL"명령이, 변수 a, b, c, d, w, x, y, z를 인자로 사용하게 함. 
10. for문, while문 허용
11. union, struct는 C정도 선에서만 작성 허용
12. KyuKyrarin언어 연동 지원. C/C++과 연동 지원. 방식은 include를 연결하기 위해서, `#pragma include(KyuKyrarin, 파일명)`과 `#pragma include(C, 파일명)`와 `#pragma include(C++, 파일명)`과 `#pragma include(NASM, 파일명)`지원.
