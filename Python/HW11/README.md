# 10901 Python HW11 @ THU

## 7.1

#### 14. (兩點之間的距離)
寫一個程式來索取兩個點的座標，並輸出兩點之間的距離。

### Dice
```python
import random
class PairOfDice:
	def __init__ (self):
		self._redDie = 0
		self._blueDie = 0
	
	def getRedDie (self):
		return self._redDie
	
	def getBlueDie (self):
		return self._BlueDie
	
	def roll (self):
		self._redDie = random.choice (range (1, 7))
		self._blueDie = random.choice (range (1, 7))
	
	def sum (self):
		return self._redDie + self._blueDie
```
#### 16
寫一個程式來模擬兩個玩家拋dice比大小的結果(大的win，且該程式要使用兩個基於`PairOfDice`的物件)：
```
Player 1: 8
Player 2: 6
Player 1 wins.
```
```
Player 1: 7
Player 2: 7
TIE
```

#### 18
寫一個程式來模擬"一個玩家拋一雙dice共24次"的事件10,000次，並算出"至少出現一次雙六"的百分比。
(答案應該要很靠近0.4914)。

### Cards
把以下程式碼放入`pCard.py`的檔案裡，並把該檔案放在同一個目錄下(跟其它作業的.py檔同一個目錄)。
```python
# pCard.py
import random

class PlayingCard:
	def __init__ (self, rank="queen", suit="hearts"):
		self._rank = rank
		self._suit = suit

	def setRank (self, rank):
		self._rank = rank

	def setSuit (self, suit):
		self._suit = suit

	def getRank (self):
		return self._rank

	def getSuit (self):
		return self._suit

	def selectAtRandom (self):
		## 隨機選取一個數字和牌色
		ranks = ['2', '3', '4', '5', '6', '7', '8', '9', "10", "jack", "queen", "king", "ace"]
		self._rank = random.choice (ranks)
		self._suit = random.choice (["spades", "hearts", "clubs", "diamonds"])
	
	def __str__ (self):
		return (self._rank + " of " + self._suit)
```
#### 26
寫一個程式來隨機抽出一張diamond的牌，並顯示在畫面上。(需使用上面的`pCard.py`中的`PlayingCard`的class)

#### 34
寫一個程式來隨機選出13張牌。這13張牌需要依牌色來排序(spades, hearts, diamonds, clubs)。
(需使用`PlayingCard`這個class, 並生成一個52張牌的list)
```
4 of spades
7 of spades
     .
     .
     .
3 of hearts
queen of diamonds
jack of clubs
8 of clubs
```

### Fraction
寫一個class，裡面需包含:
變數： 分子(numerator)、分母(denominator)。
方法： 化簡該分數至最簡(互除最大公因數)。
這個class需放在`fraction.py`裡，並放在同一個目錄下。

#### 28
寫一個程式來索取分數，並化簡分數至最簡。(使用上述的`Fraction`class)
```
Enter numerator of fraction: 12
Enter denominator of fraction: 30
Reduction to lowest terms: 2/5
```

#### 30
寫一個程式來索取一個一元二次式的系數，並判斷是否有實數解。(使用`b^2 - 4 * a * c >= 0`)
```
Enter numerical coefficient a: 6
Enter numerical coefficient b: 3
Enter numerical coefficient c: -63
The roots are 3.0 and -3.5
```

#### 32 (小考成績)
寫一個程式來索取6個成績(滿分10分)，並算出平均值。
此程式需使用一個叫`Quizzes`的class，其包含:
變數：一個變數來存放6個成績。
方法：名叫`average`，用來算出成績平均。
方法：名叫`__str__`，用來回傳"Quiz average: 平均成績"。


#### 36 (收費站登錄)
寫一個程式來記下經過的車輛數及收集的金錢總額。(每輛車收1元、卡車則收2元)
該程式需使用一個class，叫`Register`，並有以下內容：
變數：經過的車輛數、收集的總金額。
```
Enter type of vehicle (car/truck): car
Number of vehicles: 1
Money Collected: $1.00
Do you want to enter more vehicles (Y/N)? Y
Enter type of vehicle (car/truck): truck
Number of vehicles: 2
Money Collected: $3.00
Do you want to enter more vehicles (Y/N)? N
Have a good day.
```

## 7.2




## 8.1

## 8.2

## 8.3
