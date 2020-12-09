# 10901-Python-THU HW9

## `random`的用法
其中又有分:
### `random.randint (x, y)`
如果我今天使用了`random.randint (x, y)`:
```python
x = 1
y = 5
print (random.randint (x, y))
```

就會生出：  
1 ~ 5的其中一個數字。(包含了x=1, y=5本身)  
也就是1 or 2 or 3 or 4 or 5的其中一個數字。

### `random.sample (sth, size)`
如果我今天使用了`random.sample (sth, size)`，就可以print出以下的東西:  
(`sth`今天可以是所有包含一系列元素的物件，如list, set, tuple, string)
```python
sth = ['apple', 'orange', 'pineapple', 'strawberries']
print (random.sample (sth, 2))
```
就可能會生出:
```python
['apple', 'strawberries']
```
也就是在原本的物件中，隨機取出`size=2`個元素，並做成list回傳。

### `random.shuffle (sth)`
`sth`在這裡是list。使用方法如下:
```python
sth = ['apple', 'orange', 'pineapple', 'strawberries']
random.shuffle (sth)
print (sth)
```
就可能會print出:
```python
['pineapple', 'orange', 'apple', 'strawberries']

```
也就是把原本的物件的順序直接打亂(會改變原本的物件)。


## 6.1
`stateCapital`這個list的構造需要用`StatesANC.txt`來完成。
### 30 (State Capitals)
假設`stateCapitals`這個list包含了50個美國的洲首府。  
寫一段小程式來跟使用者索取一個洲首府的名字，並把其從該list中移除。
```
Enter a state capital to delete: Chicago
Not a state capital.
Enter a state capital to delete: Springfield
Capital deleted.
```


## 6.2  

### 10 (Perfect Square)
從1~10,000中隨機秀出一個完全平方數(包含端點)。


### 12 (Vowel)
隨機秀出一個母音('a', 'e', 'i', 'o', 'u')。


### 14 (Dice)
拋一雙dice 100,000次，並秀出總和為7的機會。

### 16 (U.S. States)
`StatesAlpha.txt`這個檔案中包含了50個美國的洲名(以字母序排序)，請寫一個程式來打亂其順序並寫入`RandomStates.txt`裡。

### 18 (Rock, Paper, Scissors)
寫一個程式來模擬"剪刀、石頭、布"這個遊戲，並秀出其結果。(兩方出手都是隨機的)
```
Player 1: paper
Player 2: scissors
Player 2 wins.
```

### 20 (Powerball Lottery)
該樂透的中獎號碼的産生方式為：  
隨機從編號1 ~ 59的白球中取出5顆，並1~35的紅球中選出一顆(Powerball)。
寫出一個程式來模擬100,000次的白球選取，每次都取出五顆。找出該五顆球具有兩個(含)以上連續的數字的機會。
```
31% of the time there were at least two consecutive numbers in the set of five numbers.
```
Note: 可以利用random.sample ((range (1, 60)), 5)的方法來産生隨機結果。

### 22 (Locate First Ace)
假設你洗了一疊52張牌的牌組，並一張一張翻開直到看見第一張A為止。  
平均而言，你至少要翻幾次牌才能看到第一張A的出現？  
寫一個程式來洗100,000次牌並根據這100,000次的資料來估計平均要翻開幾張牌才能看到A。  
Note: 你算出來的可能會跟範例不同，但應該會很接近10.6。
```
The average number of cards turned up was 10.61.
```
### 24 (State Capital Quiz)
利用`StatesANC.txt`中包含的洲名、洲名簡寫、洲的小名以及洲首府來製作一個測驗。
寫一個程式來隨機出5個洲名，並問使用者該洲的洲首府為何，並取得使用者的輸入。  
程式的最後要輸出總共錯了幾題，並幫使用者訂正答案。
```
What is the capital of Minnesota? Saint Paul
What is the capital of California? Sacramento
What is the capital of Illinois? Chicago
What is the capital of Alabama? Montgomery
What is the capital of Massachusetts? Boston

You missed 1 question.
Springfield is the capital of Illinois.
```
