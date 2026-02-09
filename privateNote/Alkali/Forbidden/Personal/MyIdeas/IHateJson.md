indianBool (null, bool)
SpecialBytes (number, string)

indianBool__or__SpecialBytes

typedef union {
   char eachBytes[8];
   double value;
} SpecialDouble;

typedef union {
    char V;
    struct {
        bool alwaystrue = true : 1;
        bool isbool : 1;
        bool istrue : 1;
    } : 8;
} indianBool;

template <size_t L>
struct SpecialBytes {
    char v[L];
};

template <size_t L, bool isarray>
union nonCollection {
    /** 
        * (i) L != 9 + k : not special int
        * (ii) L = 0 but v[0] != 0 : indianBool
        * if it in array, SpecialString Started by v[0] = 0
        */
    SpecialBytes<L + (size_t) isarray> specialBytes;
    indianBool nonSpecialBytes;
};

typedef struct ArrayStackFrameSuper {
    ArrayStackFrameSuper* ESP;
    /** Array Stack Frame's super class
        * as diagram : [ESP : 8*sizeof(void*)]
        */
} ArrayStackFrameCore;

typedef struct ArrayStackFrameCore : ArrayStackFrameSuper {
    /** Array Stack Frame's head
        * as diagram : [ESP : 8*sizeof(void*)][size_t : 8*sizeof(void*)]
        */
    size_t ArrayStackFrameSuper;
} ArrayStackFrameCore;

template <size_t L>
struct ArrayStackFrame : ArrayStackFrameCore {
    /** Array Stack Frame
        * as diagram : [ESP : 8*sizeof(void*)][size_t : 8*sizeof(void*)][nonCollection<L, true> : 8*(L+1)]
        */
    size_t ArrayStackFrameSuper = L;
    nonCollection<L, true> value;
};

constexpr auto constexprArrayStackFrameCore2ArrayStackFrame

template <size_t L>
struct SpecialStringPtr{
    char* end;
    SpecialBytes<L>* specialBytes;
}

template <size_t L>
struct SpecialIntPtr{
    double* end;
    SpecialBytes<L>* specialBytes;
}

template <typename T>
struct {
};

typedef struct {
    char* end;
    size_t L;
} SpectialLength;

#define SpecialLengther(specifier, NAME, SRC) specifier SpectialLength specifier##NAME (const char* txt) {
    /* char string */
    SpectialLength ret = {.end = txt};
    for (; SRC ; ret.end++);
    ret.L = (size_t) (ret.end - txt);
    return ret;
}

#define SpecialStringLengther(spec) SpecialLengther(spec, SpecialStringLength, *ret.end)
#define SpecialIntLengther(spec) SpecialLengther(spec, SpecialIntLength, *ret.end & 128)

SpecialStringLengther(inline)
SpecialStringLengther(constexpr)
SpecialIntLengther(inline)
SpecialIntLengther(constexpr)

constexpr auto constexprSpecialString(const char* txt) {
    constexpr SpectialLength length = constexprSpecialStringLength(txt);
    constexpr SpecialBytesPtr<length.L> ret = {.end = length.end, .specialBytes = txt};
    return ret;
}

auto SpecialString(const char* txt) {
    SpectialLength length = inlineSpecialStringLength(txt);
    SpecialStringPtr<length.L> ret = {.end = length.end, .specialBytes = txt};
    return ret;
}

constexpr auto constexprSpecialInt(const char* txt) {
    constexpr SpectialLength length = constexprSpecialIntLength(txt);
    constexpr char* end = ++length.end;
    constexpr SpecialIntPtr<length.L + 8> ret = {.end = (SpecialDouble*) end, .specialBytes = txt};
    return ret;
}

auto SpecialInt(const char* txt) {
    SpectialLength length = inlineSpecialIntLength(txt);
    char* end = ++length.end;
    SpecialIntPtr<length.L + 8> ret = {.end = (SpecialDouble*) end, .specialBytes = txt};
    return ret;
}