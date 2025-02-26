```
 - template <T b, T::__optlib_handle__<b>> type

 - beq0 : SUBCLS(x==T::__optlib_handle__<b>(0)?T::__optlib_handle__<1>(1):T::__optlib_handle__<b>(0), T b, T::__optlib_handle__<b> x)
 - beq : SUBCLS(x==y?T::__optlib_handle__<1>(1):T::__optlib_handle__<b>(0), T b, T::__optlib_handle__<b> x, T::__optlib_handle__<b> y)
```