# ComponentRestrictedVector System

ComponentRestrictedVector(S, V, <•,•>) ≜ {v ∈ V | ∀k ∈ ℕ ∩ [1, n], <v, eₖ> ∈ S}

약칭용 확장 : CRV ≜ ComponentRestrictedVector

dom CRVM ≜ {(S, V, <•, •>) ∈ dom CRV | <S, 0, 1, +, -, ×, ÷>가 체를 이룬다.}
CRVM(S, V, <•, •>) ≜ (CRV(S, V, <•, •>), 0, +, •, <•, •>)

th. <S, 0, 1, +, -, ×, ÷>가 체를 이루지 않으면 CRV(S, V, <•, •>)는 내적공간도, 벡터공간도 아니다.

## 응용용 확장

IntegerComponentedVector(S, V, <•, •>) ≜ CRV(S ∩ ℤ, V, <•, •>)

약칭용 확장 : ICV ≜ IntegerComponentedVector

th. ICV(S, V, <•, •>)는 사칙연산과 수가 우리가 알고있는대로 정의되었다면, 절대로 벡터공간을 이루지 않는다.

NaturalComponentedVector(t, V, <•, •>) ≜ ICV([1, t], V, <•, •>)

약칭용 확장 : NCV ≜ NaturalComponentedVector

th. NCV(t, V, <•, •>) = CRV(S, V, <•, •>)면, S의 상계엔 t가, S의 최소하계엔 1이 있게 되며, S는 자연수의 부분집합이고, t ≠ ∞일때만 진부분집합이다.