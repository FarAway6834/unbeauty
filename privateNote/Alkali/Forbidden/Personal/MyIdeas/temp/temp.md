"theorem의 증명과 의의(에 대한 직관)의 형식화"에서 다룬 theorem을 Node로, theorem x, y에 대해 (x, y)를 엣지로 다루고,
가중치 함수 w에 대해
1. w(x, y) = (=)인 경우, x = y인것
2. w(x, y) = R s.t. R ⊆ {(x, y) | x → y}인 경우, R(x, y)인것.

으로 하면, 논리적 결합사 R, 다시말해 이항관계 R에 대하여, 그래프 G = (N := {x, y}, E := {(x, y)}, w s.t. w(x, y) = R)은 문장 "x R y"의 파싱 트리가 되므로, 이러한 graph를 통해 논리적이고 이성적인 풀이 계획을 새울수 있다. (그 계획 논리적 사고 방식을, 이전에 실험한 아스퍼거인(=나)에 적용해봤더니 되더라)

이때, 

```
class MindMap:
    __slots__ = ("__N", "__E")
    
    def __init__(self):
        self.__N, self.__E = [], {}
    
    def appendNode(x : str) -> None:
        self.__N.append(x)
    
    def appendEdge(i : int, j : int, x : str) -> None:
        assert (i, j) not in self.__E.keys(), "already appended"
        self.__E[(i, j)] = x

    @property
    def N(self):
        this = self
        return type(
            "Node",
            (),
            {
                "__getitem__" : (
                    lambda self, idx : this.__N[idx]
                )
            }
        )()

    @property
    def E(self):
        this = self
        return type(
            "Edge",
            (),
            {
                "__getitem__" : (
                    lambda self, i : type(
                        "EdgeIdxView",
                        (),
                        {
                            "__getitem__" : (
                                lambda self, j : this.__E[(i, j)]
                        }
                    )
                )
            }
        )()
```