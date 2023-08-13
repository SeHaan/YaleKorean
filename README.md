# Korean Yale Romanizer (한국어 예일식 로마자 전사 변환기)
|제작자|최종 수정일|
|:--:|:--------:|
|강민하|2023년 8월 14일|

## 1. Main Functions & Usage
From `YaleKorean`, you can use these three functions.

```python
import YaleKorean
```

### 1.1. `YaleKorean.PUAtoUni`
```python
test = '안녕하세요'
print(YaleKorean.PUAtoUni(test))
# 안녕하세요
```

### 1.2. `YaleKorean.YaleCont`
```python
test_cont = '다람쥐 헌 쳇바퀴 타고파'
print(YaleKorean.YaleCont(test_cont))
# talamcwi hen cheyspakhwi thakopha
```

### 1.3. `YaleKorean.YaleMid`
```python
test_mid = '나랏말ᄊᆞ미 듀ᇰ귁에 달아 문ᄍᆞ와로 서로 ᄉᆞᄆᆞᆺ디 아니ᄒᆞᆯᄊᆡ'
print(YaleKorean.YaleMid(test_mid))
# nalasmalssomi tywungkwikey tala mwunccowalwo selwo somosti aniholssoy
```

## 2. About Korean Yale Romanization
to be continued... 으윽...