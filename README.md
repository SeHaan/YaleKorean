# Korean Yale Romanizer (한국어 예일식 로마자 전사 변환기)
Romanizer for Korean following [Yale Romanization](https://en.wikipedia.org/wiki/Yale_romanization_of_Korean). See [Chapter 3](#3-about-korean-yale-romanization) for details.

## 0. History
|date|ver|history|
|:--:|:-:|:-----:|
|20230812|-|Initial commit|
|20230814|0.0.1|test version|

## 1. Installation
```cmd
pip install YaleKorean
```

## 2. Main Functions & Usage
From `YaleKorean`, you can use these three functions.

```python
import YaleKorean
```

### 2.2. `YaleKorean.PUAtoUni(line: str) -> str`
```python
test = '안녕하세요'
print(YaleKorean.PUAtoUni(test))
# 안녕하세요
```

### 2.2. `YaleKorean.YaleCont(line: str) -> str`
```python
test_cont = '다람쥐 헌 쳇바퀴 타고파'
print(YaleKorean.YaleCont(test_cont))
# talamcwi hen cheyspakhwi thakopha
```

### 2.3. `YaleKorean.YaleMid(line: str) -> str`
```python
test_mid = '나랏말ᄊᆞ미 듀ᇰ귁에 달아 문ᄍᆞ와로 서로 ᄉᆞᄆᆞᆺ디 아니ᄒᆞᆯᄊᆡ'
print(YaleKorean.YaleMid(test_mid))
# nalasmalssomi tywungkwikey tala mwunccowalwo selwo somosti aniholssoy
```

## 3. About Korean Yale Romanization
### 3.1. Basic Rule
#### 1) Consonants
|Hangul|Romanized|
|:----:|:-------:|
|ㄱ|k|
|ㄲ|kk|
|ㄴ|n|
|ㄷ|t|
|ㄸ|tt|
|ㄹ|l|
|ㅁ|m|
|ㅂ|p|
|ㅃ|pp|
|ㅅ|s|
|ㅆ|ss|
|ㅇ|ng*|
|ㅈ|c|
|ㅉ|cc|
|ㅊ|ch|
|ㅋ|kh|
|ㅌ|th|
|ㅍ|ph|
|ㅎ|h|

*only for 'ㅇ' in coda position. 'ㅇ' in onset position does not have any sound.

#### 2) Vowels
|Hangul|Romanized|
|:----:|:-------:|
|ㅏ|a|
|ㅓ|e|
|ㅗ|o|
|ㅜ|wu*|
|ㅡ|u|
|ㅣ|i|
|ㅐ|ay|
|ㅔ|ey|
|ㅚ|oy|
|ㅟ|wi|
|ㅑ|ya|
|ㅕ|ye|
|ㅛ|yo|
|ㅠ|yu|
|ㅒ|yay|
|ㅖ|yey|
|ㅘ|wa|
|ㅙ|way|
|ㅝ|we|
|ㅞ|wey|
|ㅢ|uy|

*If 'ㅜ' is posited after bilabial sounds /ㅂ, ㅃ, ㅍ/, 'ㅜ' is romanized as 'u.', It is because that 'ㅜ' and 'ㅡ' is neutralized after bilabial sounds.

### 3.2. Notation for Middle Korean
#### 1) Consonants
|Hangul|Romanized|
|:----:|:-------:|
|ㅸ|W|
|ㅹ|WW*|
|ᄛ|L*|
|ㅱ|M*|
|ㆄ|F*|
|ㅿ|z|
|ㅇ|G**|
|ㆁ|ng|
|ㆆ|q|
|ᄼ|S*|
|ᄽ|SS*|
|ᄾ|Sr*|
|ᄿ|SSr*|
|ᅎ|C*|
|ᅏ|CC*|
|ᅐ|Cr*|
|ᅑ|CCr*|
|ᅔ|Ch*|
|ᅕ|Chr*|

*These notations are not in the standard Yale Romanization.<br>
**This notation of 'ㅇ' is only for 'ㅇ'[ɦ].

#### 2) Vowels
- ㆍ(아래아 alay.a) is notated as 'o'.
  - ```YaleCont(str)```: 'O' (capital 'o')
  - ```YaleMid(str)```: 'o'
- 'ㅜ' does not undergo after bilabial sounds.
  - ```YaleCont(str)```: 'wu', 'u'(after bilabials)
  - ```YaleMid(str)```: 'wu' for all contexts