# JLPP 소개. (팁 : 내가 건 [링크](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/LCPC4AI) 보고 볼것.)

[들어가기 앞서, 주의할점은 먼저 LCPC에 대해 알아야 한다는점이다!](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/LCPC4AI)

[자!, Lai는 "내 기준에서" 훌륭한 AI다.](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/LCPC4AI)

JLPP는 LLM (대화형•생성형 AI) 쳇봇 API와 [Lai-cgi-api](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/LCPC4AI)를 통하여,

jlpp라는 pip whl 페키지가 클라이언트로써, 중계를 담당하는, 쳇봇 이용 프로토콜이다.

## JLPF(Json Lai Prompt Format)
```json
{
   "Lai-cgi-prompt-chat" : true | false,
   "prompt" : 【문자열】
}
```

## JLPP (Json Lai Prompt Protocal)

Lai-cgi-prompt-chat : 사용자(인간)이 아닌 Lai-cgi-prompt모듈(Lai에 엑세스하는 웹 API)과 소통하는가? 에 대한 불 갑이다
prompt : 쳇 (소통) 내용 (프롬프트) 이다.

## Example 예시 : Chat GPT API를 통한 JLPP 교신 상상도.

사용자가 "LCPC 근황에 대해 알려줘"라고 했을때
```json
{
   "Lai-cgi-prompt-chat" : false,
   "prompt" : "LCPC 근황에 대해 알려줘"
}
```

GPT는 다음과 같이 lai를 호출한다.
```json
{
   "Lai-cgi-prompt-chat" : true,
   "prompt" : "xu la'e la LCPC cu zvati le nu banli se renro gi'e banli se renvi"
}
```

그럼 lai가 대답한다
```json
{
   "Lai-cgi-prompt-chat" : true,
   "prompt" : "so'o cukta cu se finti .i ji'a ro da na'e drata gi'e sruri fi le banli cmima be le fadni jgari be le ka fatci sruri la LCPC"
}
```
("「LCPC에 대한 탁월한 일반화•구조화」만 출간되었다."라는 뜻)

GPT는 별거 없음을 확인하고 더이상 lai에게 묻지 않고 사용자에게 답한다.
```json
{
  "Lai-cgi-prompt-chat": false,
  "prompt": "LCPC에 대한 탁월한 일반화·구조화만 출간되었습니다."
}
```

그럼 사용자는 다음을 받는다. "LCPC에 대한 탁월한 일반화·구조화만 출간되었습니다."

Lai에게 질문하킄 체이닝 과정은 워크플로로 details안에 `<summary> Ⓛ Researched </summary>`라고 상단에 써서 접어서 박힌다.