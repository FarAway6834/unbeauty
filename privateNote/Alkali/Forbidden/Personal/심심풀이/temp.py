from numpy import ndarray as NumpyArrayType
from numpy import asarray as _NumpyArrayTypeObject_create
from numpy import array as tensor # numpy array is actually linear algebric tensor.
from functools import wraps as _deco_wraps

class GenericTensorGenerator(list):
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

def MyLinearTransformation(x : GenericTensorGenerator, Einstein = False):
     if p:
         def LinearTransformator(self, *others):
             return np.einsum('kij,k->ij', x(dtype = self.dtype), self) @ others[0] if others else np.einsum('kij,k->ij', x(dtype = self.dtype), self)
     else:
         def LinearTransformator(self, *others):
             return (x(dtype = self.dtype) @ self) @ others[0] if others else x(dtype = self.dtype) @ self
     def LinearTransformation_decorating_wrapper_part(method):
         @_deco_wraps(method)
         def LinearTransformationMethod(self, *argv, **kargv):
             return method(self, *argv, LinearTransformator = LinearTransformator, **kargv)
         return LinearTransformationMethod
     return LinearTransformation_decorating_wrapper_part

def NormalLinerTransformationMethoder(x : GenericTensorGenerator, p = False):
    def NormalLinerTransformationMethoder_decorating_wrapper_part(func):
        @MyLinearTransformation(x, p = p)
        @_deco_wraps(func)
        def NormalLinerTransformationMethod(self, *args, LinearTransformator = None, **kargs):
            return LinearTransformator(self, *args, **kargs)
        return NormalLinerTransformationMethod
    return NormalLinerTransformationMethoder_decorating_wrapper_part

def GenericLinearTransformationMethod(iterable_obj, p = False):
    return NormalLinerTransformationMethoder(GenericTensorGenerator(iterable_obj), p = p)

Change2InversedElement = GenericLinearTransformationMethod([[0, 1], [1, 0]])


class _Core_SubtractArgumentVector(metaclass = MyNumpyArrayClassType):
    @Change2InversedElement
    def __neg__(self): pass
    
    @GenericLinearTransformationMethod([[[1, 0], [0, 1]], [[0, 1], [1, 0]]])
    def __mul__(self): pass
    
    def __rsub__(self, others):
        return (-self) + others
    
    def __sub__(self, others):
        raise NotImplementedError
    
    def __eq__(self, others):
        return self - others == 0 if others else self[0] = self[1]

class _Coreof_RatioArgumentVector(metaclass = MyNumpyArrayClassType):
    
    @GenericLinearTransformationMethod([[-1, 0], [0, 1]])
    def __neg__(self): pass
    
    @Change2InversedElement
    def reciprocal(self): pass
    
    @GenericLinearTransformationMethod([[[0, 1], [1, 0]], [[0, 0], [0, 1]]])
    def __add__(self): pass
    
    @GenericLinearTransformationMethod([[[1, 0], [0, 0]], [[0, 0], [0, 1]]])
    def __mul__(self): pass
    
    @GenericLinearTransformationMethod([[[0, -1], [1, 0]], [[0, 0], [0, 1]]])
    def __rsub__(self): pass
    
    @GenericLinearTransformationMethod([[[0, 0], [1, 0]], [[0, 1], [0, 0]]])
    def __rdiv__(self): pass
    
    @GenericLinearTransformationMethod([[[0, -1], [1, 0]], [[0, 0], [0, 0]]])
    def __eq_helper(self): pass
    
    def __sub__(self, others):
        raise NotImplementedError
    
    def __div__(self, others):
        raise NotImplementedError
    
    def __eq__(self, others, gen_zero_vector = GenericLinearTransformationMethod([0, 0])):
        return self.__eq_helper(others) == 0 if others else super().__eq__(gen_zero_vector(dtype = self.dtype))

class SubtractArgumentVector(_Core_SubtractArgumentVector):
    def __new__(cls, x, y, **kargv):
        return super().__new__(cls, [x, y], **kargv)

class RatioArgumentVector(_Coreof_RatioArgumentVector):
    def __new__(cls, x, y, **kargv):
        return super().__new__(cls, [x, y], **kargv)

# 겨우 만들었는데 제대로 작동할지 미지수...