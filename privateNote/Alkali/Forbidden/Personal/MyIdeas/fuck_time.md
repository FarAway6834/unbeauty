d

#include <concepts>
#include <type_traits>

template <typename T>
concept Step = requires {
    typename T::generic;
    requires requires(typename T::generic v) {
        { T::function(v) } ->  std::same_as<typename T::generic>;
    };
};

template <Step T>
concept TRONamespace = requires(typename T::generic v) {
    { T::predicate(v) } -> std::same_as<bool>;
};

template <TRONamespace T>
struct TRONamespace2TROFunction {
    using generic = typename T::generic;
    static inline generic TROFunction(generic x) {
        while (T::predicate(x)) x = T::function(x);
    }
};

template <Step T, size_t N>
struct DuplicateStep {
        static inline typename T::generic step(typename T::generic x) {
            x = LoopUnrolling<T, N - 1>::step(x);
            return T::function(x);
        }
};

template <Step T>
struct DuplicateStep<T, 1> {
    static inline typename T::generic step(typename T::generic x) {
        return T::function(x);
    }
};

template <TRONamespace T, size_t unroll>
struct unrolledTRONamespace {
    using generic = typename T::generic;
    using duplicate_type = typename DuplicateStep<T, unroll>:
    static inline bool predicate(generic x) {
        return T::predicate(x);
    }
    static inline generic function(generic x) {
        return duplicate_type::step(x);
    }
};