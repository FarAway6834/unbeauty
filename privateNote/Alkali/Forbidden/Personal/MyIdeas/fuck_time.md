흠...

```cpp
#include <concepts>
#include <type_traits>

template <typename T>
concept SelfmapicInterface = requires {
    /* one kind of functional interface */
    typename T::generic;
    requires requires(typename T::generic v) {
        { T::function(v) } ->  std::same_as<typename T::generic>;
    };
};

template <SelfmapicInterface T>
concept TRONamespace = requires(typename T::generic v) {
    { T::predicate(v) } -> std::same_as<bool>;
};

typedef struct {} TROFunction;

template <TRONamespace T>
struct TRONamespace2TROFunction : TROFunction {
    using generic = typename T::generic;
    static inline typename generic TROFunction(typename generic x) {
        while (T::predicate(x)) x = T::function(x);
    }
};

template <SelfmapicInterface T, size_t N>
struct IteratedFunction {
    using generic = typename T::generic;
    using PreviousTerm = typename IteratedFunction<T, N - 1>;
    static inline typename generic function(typename generic x) {
        x = PreviousTerm::function(x);
        return T::function(x);
    }
};

template <SelfmapicInterface T>
struct IteratedFunction<T, 0> {
    using generic = typename T::generic;
    static inline typename generic function(typename generic x) {
        return x;
    }
};

template <SelfmapicInterface T>
struct IteratedFunction<T, 1> {
    using generic = typename T::generic;
    using PreviousTerm = typename IteratedFunction<T, 0>;
    static inline typename generic function(typename generic x) {
        return T::function(x);
    }
};

template <TRONamespace T, size_t unroll>
struct unrolledTRONamespace {
    using generic = typename T::generic;
    using unrolledTerm = typename IteratedFunction<T, unroll>;
    static inline bool predicate(typename generic x) {
        return T::predicate(x);
    }
    static inline typename generic function(typename generic x) {
        return unrolledTerm::function(x);
    }
};

template <TRONamespace T>
struct unrolledTRONamespace<T, 0> {
    using generic = typename T::generic;
    using unrolledTerm = typename IteratedFunction<T, 1>;
    static inline bool predicate(typename generic x) {
        return T::predicate(x);
    }
    static inline typename generic function(typename generic x) {
        return x;
    }
};

template <TRONamespace T>
struct unrolledTRONamespace<T, 1> {
    using generic = typename T::generic;
    using unrolledTerm = typename IteratedFunction<T, 1>;
    static inline bool predicate(typename generic x) {
        return T::predicate(x);
    }
    static inline typename generic function(typename generic x) {
        return T::function(x);
    }
};

template <TRONamespace T, size_t unroll>
struct unrolledTRONamespace2TROFunction : TRONamespace2TROFunction<unrolledTRONamespace<T, unroll>> {};

template <TRONamespace T>
struct unrolledTRONamespace2TROFunction<T, 0> : TROFunction {
    using generic = typename T::generic;
    static inline typename generic TROFunction(typename generic x) {
        return x;
    }
};

template <TRONamespace T>
struct unrolledTRONamespace2TROFunction<T, 1> : TROFunction {
    using generic = typename T::generic;
    static inline typename generic TROFunction(typename generic x) {
        if (T::predicate(x)) return T::function(x);
        return x;
    }
};
```
