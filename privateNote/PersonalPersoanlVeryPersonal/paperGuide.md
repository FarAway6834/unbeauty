# 논문 작성법 요약

## 논문은 단순(eazy)하고, 간단명료하며 산만하지 말아야 한다.

구조
- 제목, Title (수식 허용) : 간결한 표현 of CoreConcept/Result
- 공동 저자 정보, Auther : 이름, 소속, email
초록이라는 명칭의 요약 Abstract (총 1문단 100~250word, 수식 허용) : 간결히 CoreContents Abstract {동기, 문제 제기, 주요 결과, 목적, 의의, 응용 가능성, ...}
 - 본문의 시작, 서론, 다른말로 도입. Introduction : 명확화, 포함 : {**중요 Referance 인용**, 동기, 문제 제기, 주요 결과, 목적, 위치, 연구, 배경, 기존 research review, 차별점, outline, ...}
 - 기본 개념으로 이걸 보고 누구나 이해하도록 / 표기법으로 단지 선언할 뿐만 아니라 설명도 함, Preliminaries (길어지면 부록으로 뺌) / Notation (과하게 기본적인 내용 제외) : 기존 Theorem과 Lemma를 미리 기술 (약속과 너무 긴 보조정리, 내용의 증명은 길면 참고문헌을 인용한다, 시작할때 하는 선언이기에 너무 긴 증령과 결과 중복을 피한다), 그리고 특수한 설정이나 가정도 제시한다 ; 그러려면 필요한 배경지식(이게 뭘까 싶은거)을 리스트에서 꼭 필요한것만 단순명료(깔끔)하게 서술해야한다, 참고 문헌도 간단해야한다.
 - 공리계 소개 Axioms : 이걸 Preliminaries에 적기에는 너무 골치아프기에 따로 섹션을 나눈다 ; “이 논문에서는 다음 공리를 가정한다”라고 기반이 된다 선언 (공리가 논문에 미치는 영향과 필요성 충분히 설명하고, 독자가 공리 도입의 합리성과 의의를 이해할 수 있도록 서술한다)
 - 글의 핵심이자 본론; 주요 결과, Main Results (의의 강조 가능한것만) : Theorem, Proposition, Conjecture, Lemma, Definition, Proof, introducing Idea/기법; 가독성을 위해 주요 결과를 간단히 설명해야만 한다 (복수 결과가 있다면 체계적으로 나열) 그러나 형식증명을 사용하면, 어떻게 성립하는지를 형식적으로 완전히 빈틈없이 서술하며, 필요하면 레퍼런스 제공해야한다.
 - 적용 예시로써의 서술과 논평 혹은 구체적인 예시로 추상적 결과를 설명하면서 예시에 정례 및 반례 등을 서술한다, Applications or Examples (선택적) : 여기서만 설명을 위한 글이 아닌 자료들이 허용된다, 그리고 순수 이론 위주면 보통 생략한다.
 - 간략히 재정리한 핵심 결론 / 흥미로운 추후(후속) 연구 방향 Conclusion / Further Work (선택적, 핵심만 깔끔히 ; 영향력과 한계점 솔찍히 밝힘, 막연하지 않게) : , 중요한 결과적 성과와 간단명료히 압축해 전달 / 미해결이나 남겨진 문제 제시, 독자나 후속 연구자에게 연구 아이디어 제공
 - 참고문헌, Refferance : AMS(미국수학회) 스타일로 자동화 : 레퍼 작성은? LaTeX에서 `biblatex` / `bibtex`을 써서 자동화 : (다음 쳅터)

## 📌 1. **AMS(미국수학회) 스타일**

| 요소     | 설명                          |
| ------ | --------------------------- |
| 저자     | 성, 이름 약어 (보통 첫 이름의 이니셜)     |
| 제목     | 논문/책 제목 (논문은 따옴표, 책은 이탤릭)   |
| 저널/출판사 | 논문이면 학술지 이름, 책이면 출판사        |
| 권/호/쪽수 | 권(volume), 호(issue), 페이지 범위 |
| 연도     | 출판 연도                       |

## 📘 2. *(수정됨)*

> `\bibitem{라벨}`은 본문에서 `\cite{라벨}`로 인용할 수 있게 해줘요.

## 📚 3. BibTeX 예시 (자동 참고문헌 시스템)

파일을 `.bib`로 따로 만들고, 이렇게 작성합니다:

```bibtex
@book{rudin,
  author    = {Walter Rudin},
  title     = {Principles of Mathematical Analysis},
  publisher = {McGraw-Hill},
  year      = {1976},
  edition   = {3}
}

@article{wiles,
  author  = {Andrew Wiles},
  title   = {Modular elliptic curves and Fermat’s last theorem},
  journal = {Annals of Mathematics},
  volume  = {141},
  year    = {1995},
  pages   = {443--551}
}
```

그리고 LaTeX 문서에 이렇게 붙여넣습니다:

```latex
\bibliographystyle{amsplain}
\bibliography{myrefs}
```

## 🛑 4. N.B.

* 수학은 **정확한 저널명, 볼륨, 페이지, 연도** 중요
* 논문 제목은 보통 따옴표 `"..."`, 책은 이탤릭 `\textit{...}`
* 인용 순서가 **사용 순서 순**인지 **알파벳 순**인지 스타일 따라 다름 (AMS는 보통 사용 순서)
* 절대 링크만 덜렁 넣지 말기!

# GPT 재요약

아주 훌륭한 요약이에요! 전체적으로 정확하고 논리적으로 잘 정리됐고, 수학 논문 구조에 맞는 형식, 관례, 문체까지 잘 담겨 있어요. 여기에 몇 가지 보완하거나 다듬으면 더 완성도 높은 가이드가 됩니다.

---

## ✅ 보완 및 개선 제안

### 1. 제목 / 초록 관련

* **Title**에 수식 사용은 허용되지만 너무 복잡하거나 긴 건 피하는 게 좋습니다.
  → 독자가 검색하거나 인용하기 쉽게 **간결하고 정보 중심적으로** 쓸 것.

* **Abstract**는 수학에서는 특히 “결과 중심”이지만, 한두 문장은 **동기**와 **문제 제기**로 시작하고
  나머지는 **주요 결과 요약, 방법 간단 서술, 의의 및 적용 가능성** 정도로 정리하면 이상적입니다.

  ✅ 예시 구조 (1문단):

  ```
  In this paper, we study ... motivated by ... 
  We establish ... using ... 
  The main result shows that ...
  This generalizes ... and has potential applications in ...
  ```

---

### 2. Introduction에서 “논문 구성 개요”는 거의 필수

→ 마지막 문단에 이렇게 정리하면 좋아요:

```latex
The remainder of this paper is organized as follows. 
Section 2 introduces preliminary concepts and notations.
Section 3 presents our main results and their formal proofs.
Section 4 discusses applications and illustrative examples.
We conclude in Section 5 with remarks on further research directions.
```

---

### 3. Preliminaries / Notation은 “구분이 되도록” 나눠 써도 됨

```latex
\section{Preliminaries}
\subsection{Notation}
```

* 그리고 **선언 + 간단한 해설** 형태로 정리
* 너무 사소한 기호 정의는 생략
  예: $\mathbb{N}$ = 자연수, $\mathbb{R}$ = 실수 등은 필요에 따라 생략 가능

---

### 4. Axioms 섹션: 독립된 섹션으로 둘 경우 좋음

* 수학 논문에서 흔하지는 않지만 **논리학, 형식 체계, 공리 기반 연구**라면 적절
* 공리를 나열할 땐 설명을 붙여 독자가 이 공리의 역할을 이해하도록 작성

---

### 5. Main Results 작성 팁

* 주요 정리는 **번호**와 **라벨(label)** 필수
* 정리는 `\begin{theorem} ... \end{theorem}` 으로 표현
* **의미 해설을 붙이는 것**이 특히 중요함

  ```latex
  This theorem generalizes the classical result of ...
  The key idea is to ...
  ```

---

### 6. Applications or Examples 팁

* 예시는 수식 외에도 **간단한 설명**, **직관적인 요약**을 포함하면 더 친절함
* **추상적인 정의나 정리를 구체화**시키는 목적
* 단, 이론 중심 논문이라면 생략해도 문제 없음

---

### 7. Conclusion / Further Work 팁

* 반드시 간결하게 요약할 것. 새로운 내용은 넣지 않음
* “남은 과제”를 이야기할 땐 **막연하지 않도록, 구체적으로**:

  ```latex
  Future work includes extending our result to non-compact spaces and studying its implications in ...
  ```

---

### 8. Reference 파트

너무 잘 정리했어요! 여기에 조금만 더 추가하자면:

#### ✅ 자주 쓰는 BibTeX entry 유형:

| 유형    | 키워드                            | 사용 예시          |
| ----- | ------------------------------ | -------------- |
| 논문    | `@article`                     | 저널 논문          |
| 책     | `@book`                        | 교과서, 참고서       |
| 학위논문  | `@phdthesis`, `@mastersthesis` | 논문형 연구 보고서     |
| arXiv | `@misc` or `@article`          | arXiv preprint |
| 논문 일부 | `@incollection`                | 편저 책 속 논문      |

```bibtex
@misc{tao_blog,
  author = {Terence Tao},
  title = {An epsilon of room},
  note = {Blog post, available at \url{https://terrytao.wordpress.com/}},
  year = {2010}
}
```

---

## ✅ 최종 팁

* 논문은 "간단 + 정제된 용어 + 깔끔한 서술"이 가장 강합니다.
* 수학 논문은 특히 **'과장'을 피하고**, **사실만 정리해서 전달**하는 것이 미덕입니다.
* 문장 쓰는 감각은 실제 논문을 많이 읽어보며 익히는 것이 최고예요.
