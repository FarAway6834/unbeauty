from numpy import ndarray as NumpyArrayType
from numpy import asarray as _NumpyArrayTypeObject_create
from numpy import array as tensor # numpy array is actually linear algebric tensor.
from numpy import einsum as einsteinal_product
from functools import wraps as _deco_wraps

class _GenericTensorGenerator(list):
    def __init__(self, iterable_obj):
        super().__init__(iterable_obj)
    
    def __call__(self, dtype):
        return tensor(self, dtype = dtype)

class MyNumpyArrayClassType(type(NumpyArrayType)):
    def __new__(cls, name : str, base : tuple, value : dict):
        def __new__(cls, *args, **kwargs):
            return _NumpyArrayTypeObject_create(*args, **kwargs).view(cls)
        
        def __array_finalize__(self, obj):
            if obj is None: return
        
        value['__new__'] = classmethod(__new__)
        value['__array_finalize__'] = __array_finalize__
        return super().__new__(cls, name, (NumpyArrayType, *base), value)

def _MyLinearTransformation(x : _GenericTensorGenerator, Einstein = False): # Hotfix as Einstein
     if Einstein:
         def LinearTransformator(self, *others):
             return einsteinal_product('kij,k->ij', x(dtype = self.dtype), self) @ others[0] if others else einsteinal_product('kij,k->ij', x(dtype = self.dtype), self)
     else:
         def LinearTransformator(self, *others):
             return (x(dtype = self.dtype) @ self) @ others[0] if others else x(dtype = self.dtype) @ self
     def LinearTransformation_decorating_wrapper_part(method):
         @_deco_wraps(method)
         def LinearTransformationMethod(self, *argv, **kargv):
             return method(self, *argv, LinearTransformator = LinearTransformator, **kargv)
         return LinearTransformationMethod
     return LinearTransformation_decorating_wrapper_part

def _NormalLinerTransformationMethoder(x : _GenericTensorGenerator, Einstein = False):
    def NormalLinerTransformationMethoder_decorating_wrapper_part(func):
        @_MyLinearTransformation(x, Einstein = Einstein)
        @_deco_wraps(func)
        def NormalLinerTransformationMethod(self, *args, LinearTransformator = None, **kargs):
            return LinearTransformator(self, *args, **kargs)
        return NormalLinerTransformationMethod
    return NormalLinerTransformationMethoder_decorating_wrapper_part

def _GenericLinearTransformationMethod(iterable_obj, Einstein = False):
    return _NormalLinerTransformationMethoder(_GenericTensorGenerator(iterable_obj), Einstein = Einstein)

Change2InversedElement = _GenericLinearTransformationMethod([[0, 1], [1, 0]])


class _Core_SubtractArgumentVector(metaclass = MyNumpyArrayClassType):
    @Change2InversedElement
    def __neg__(self): pass
    
    @_GenericLinearTransformationMethod([[[1, 0], [0, 1]], [[0, 1], [1, 0]]], Einstein = True)
    def __mul__(self): pass
    
    def __rsub__(self, others):
        return (-self) + others
    
    def __sub__(self, others):
        raise NotImplementedError
    
    def __eq__(self, others):
        return self - others == 0 if others else self[0] = self[1] # when others is 0, then else case returned.

class _Coreof_RatioArgumentVector(metaclass = MyNumpyArrayClassType):
    
    @_GenericLinearTransformationMethod([[-1, 0], [0, 1]])
    def __neg__(self): pass
    
    @Change2InversedElement
    def reciprocal(self): pass
    
    @_GenericLinearTransformationMethod([[[0, 1], [1, 0]], [[0, 0], [0, 1]]], Einstein = True)
    def __add__(self): pass
    
    @_GenericLinearTransformationMethod([[[1, 0], [0, 0]], [[0, 0], [0, 1]]], Einstein = True)
    def __mul__(self): pass
    
    @_GenericLinearTransformationMethod([[[0, -1], [1, 0]], [[0, 0], [0, 1]]], Einstein = True)
    def __rsub__(self): pass
    
    @_GenericLinearTransformationMethod([[[0, 0], [1, 0]], [[0, 1], [0, 0]]], Einstein = True)
    def __rdiv__(self): pass
    
    @_GenericLinearTransformationMethod([[[0, -1], [1, 0]], [[0, 0], [0, 0]]], Einstein = True)
    def __eq_helper(self): pass
    
    def __sub__(self, others):
        raise NotImplementedError
    
    def __div__(self, others):
        raise NotImplementedError
    
    def __eq__(self, others, gen_zero_vector = GenericLinearTransformationMethod([0, 0])):
        return self.__eq_helper(others) == 0 if others else super().__eq__(gen_zero_vector(dtype = self.dtype)) # when others is 0, then else case returned.

class SubtractArgumentVector(_Core_SubtractArgumentVector): # Model of x - y
    def __new__(cls, x, y, **kargv):
        return super().__new__(cls, [x, y], **kargv)

class RatioArgumentVector(_Coreof_RatioArgumentVector): # Model of x : y
    def __new__(cls, x, y, **kargv):
        return super().__new__(cls, [x, y], **kargv)

class RatioArgumentVector_by_SubtractArgumentVector(RatioArgumentVector):
     def __new__(cls, a, b, x, y, **kargv):
          return super().__new__(cls, SubtractArgumentVector(a, b, **kargv), SubtractArgumentVector(x, y, **kargv), dtype = object, **kargv) 

# 개힘들다... 그래도 어쨌거나 성공이다. RatioArgumentVector_by_SubtractArgumentVector를 만들었느니 범자연수 빕합에 대해 수학적 모델로써 RatioArgumentVector_by_SubtractArgumentVector가 유리수를 구성하니까
