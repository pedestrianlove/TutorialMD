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


## 7.2




## 8.1

## 8.2

## 8.3
