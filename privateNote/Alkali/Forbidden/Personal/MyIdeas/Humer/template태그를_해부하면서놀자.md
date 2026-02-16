# template tag를 최적화 하면서 놀자

(데코는 명곡제조기야 ㄹㅇ)

그럼에도 사실상 /((DEFINE)?
    (?<spacing>[\s\t]+)
    (?<__eq__> (?&spacing)=(?&spacing))
    (?<PCDATA> (.*?))
    (?<CDATA> "(?<CDATAValue> (?:[^"\\]|\\.))*")
    (?<NMTOKEN> "(?<NMTOKENValue> [_:0-9\-\.\w]*)")
    (?<NMTOKENS> "(?&NMTOKENValue)((?&spacing)(?&NMTOKENValue))*")
    (?<ID> (?![\d])(?&NMTOKEN))
    (?<rtlORltr> ((?<rtl> "rtl")|(?<ltr> "ltr")))
    (?<id> (?&spacing)(id(?&__eq__)(?&ID))?)
    (?<dir> (?&spacing)(dir(?&__eq__)(?&rtlORltr))?)
    (?<lang> (?&spacing)(lang(?&__eq__)(?&NMTOKEN))?)
    (?<class> (?&spacing)(class(?&__eq__)(?&NMTOKENS))?)
    (?<data-any> (?&spacing)(data-(?&NMTOKENValue)(?&__eq__)(?&CDATA))?)
    (?<style> (?&spacing)(style(?&__eq__)(?&CDATA))?)
    (?<title> (?&spacing)(title(?&__eq__)(?&CDATA))?)
    (?<template-attlist_0> ((?&style)(?&data-any) | (?&style)(?&data-any))
    (?<template-attrlist_1> ((?&dir)(?&template-attlist_0)|(?&template-attlist_0)(?&dir)))
    (?<template-attlist_2> ((?&lang)(?&template-attrlist_1)|(?&template-attrlist_1)(?&lang)))
    (?<template-attlist_3> ((?&title)(?&template-attrlist_2)|(?&template-attrlist_2)(?&title)))
    (?<template-attrlist_4> ((?&class)(?&template-attrlist_3)|(?&template-attrlist_3)(?&class)))
    (?<template-attrlist> ((?&id)(?&template-attrlist_4)|(?&template-attrlist_4)(?&id))
    (?<template> \<template(?&template-attrlist)\>(?&PCDATA)\</template\>)
    | (?<main> (?&template))
) (?&main)/인 셈이잖아. template태그가 그냥 구조체로 취급되면 참 좋으련만...

id
class • lang
title • data-any

typedef unsigned char uch;

enum flagmask : uch {
    idAttrExist = 1;
    classAttrExist = 2;
    langAttrExist = 4;
    titleAttrExist = 8;
    styleAttrExist = 16;
    dataClanystarAttrExist = 32;
    divAttrExist = 64;
    divIsLtrOrNot = 128;
};

typedef struct TemplateTag {
    uch flag;
} template_tag;

#pragma pack(push, 1)
typedef struct {
    size_t idLength;
    size_t classLength;
    size_t langLength;
    size_t titleLength;
    size_t styleLength;
    size_t dataClanystarLength;
} attlist_length;
#pragma pack(pop)

#pragma pack(push, 1)
template <uch flag, attlist_length original>
struct factual_attlist_length {
    size_t idLength = (flag & idAttrExist)?original.idLength:0;
    size_t classLength = (flag & classAttrExist)?original.classLength:0;
    size_t langLength = (flag & langAttrExist)?original.langLength:0;
    size_t titleLength = (flag & titleAttrExist)?original.titleLength:0;
    size_t styleLength = (flag & styleAttrExist)?original.styleLength:0;
    size_t dataClanystarLength = (flag & dataClanystarAttrExist)?original.dataClanystarLength:0;
};
#pragma pack(pop)

#pragma pack(push, 1)
template <attlist_length L>
struct attlist_info {
    size_t idOffset = 0;
    size_t classOffset = L.idLength;
    size_t langOffset = L.idLength + L.classLength;
    size_t titleOffset = L.idLength + L.classLength + L.langLength;
    size_t styleOffset = L.idLength + L.classLength + L.langLength + L.titleLength;
    size_t dataClanystarOffset = L.idLength + L.classLength + L.langLength + L.titleLength + L.styleLength;
    size_t Length = L.idLength + L.classLength + L.langLength + L.titleLength + L.styleLength + L.dataClanystarLength;
};
#pragma pack(pop)

엄.... 생각이 안난다 어떻게든 직렬화 가능할것 같은데...

직렬화된다면 HTTP Header에 저걸 Base64로 담으면 되잖아 ㅠㅠ