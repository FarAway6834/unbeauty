```
it sucks

<runtime>

[typ]
 - subcls typic
 - duck typic
     - *.operator+ : this auto& morphism
     - *.operator- : this auto& morphism
     - *.operator* : this auto& morphism
     - *.operator/ : this auto& morphism
     - *.operator^ : this auto& morphism
     - additional : ==,!=,>,<,>=,=<,&,|,^,&&,||

data must placed before the function or fixing __optlib_handle__ using alias to fix optlib bit type give using

[cls]
 - subcls<upper self>
     - [super super                    final] *.operator[] : operator() with cache
     - [super using introduce almost virtual] T::##__TMP__ : template var
     - [super super                    final] *.operator() : template user
     - [protected super virtual 2      final] *.cache()    : user implements
     - by mecro (sucks)
         - PROMISSERN is mecro, not defed
           template <__supert__<T> this>
           struct __MANGELED_NAME__ : idxof<T, subclstyps, __typechekced_super__> {
               template <__VA_ARGS__, promiss<T> V = PROMISSER(__SRC__)>
               using __TMP__ = V; //well it's real name
           }
           inline auto __NAME__(void) { return __MANGELED_NAME__<T>(); } // `a×this.__NAME__(~)` ≡ `(a × this.__NAME__)(~)`
 - corcls<typ T, subclstyp<T>... subclstyps>
     - by mecro
     - cls attr by mecro `THISOBJTER <- _self__getattr__` => `THISOBJTER(ob, attr) ob::attr<ob>()`
 - entrypoints
     - `::` to `_s_`
     - inline function.
     - by mecro
 
<compile>

`<f> = cacher[<num>](λ<argv>.<src>)` as parse argv and set `T` or consexpr const
also it can use `main = ~` to set `operator()`

-----

base struct (default super cls)
`:filename` to can extend
```

# wtf?

so the method is just work as acess indexing...

and _self__getattr__macro to acess huh?


---

# problem

 - in cacher : using `[]` when using `cache` with `()`
 - in fclass : using `[]` 2 call

# plan changes

compile this.method(...) into clsname::method(clsname, ...)