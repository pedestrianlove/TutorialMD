# 10901 Python HW10

## 6.3
### 畫筆顏色參考
![](https://i.imgur.com/y1KoWNA.png)

### 第1~8題，不可以使用`drawLine`, `drawRectangle`, `drawFilledRectangle`或`drawDot`函數。

#### 2.
畫出一條藍色的水平線，相切一個直徑為100 pixel的紅點。

#### 4.
畫出一條從(25, 55)連到(80, 40)的紫色線段，並且兩端都要有小點。

#### 6.
畫出一個orange色的正方形，邊長80 pixel，並且有著紅色的邊界，置中於turtle的視窗當中。

#### 8.
畫出一個正三角形，邊長為100 pixel。

#### 10 ~ 20
![](https://i.imgur.com/quItTpo.png)

### 22~26, 除了24是正方形之外，高寛比皆為2:3
#### 22
畫出Niger的國旗:  
![](https://i.imgur.com/IGGQjlN.png)


#### 24
畫出Switzerland的國旗:  
![](https://i.imgur.com/qc0F65m.png)


#### 26
畫出Panama的國旗:  
![](https://i.imgur.com/5GImNme.png)


#### 28 (High Schools)
畫出以下長條圖:  
![](https://i.imgur.com/wUTffbl.png)


#### 30 (Life Goals)
![](https://i.imgur.com/k9rhqaM.png)  
使用以上數據畫出以下線條圖：  
![](https://i.imgur.com/mFPuIn5.png)




## 6.4

#### 8. (Sequence of Numbers)
考慮以下程式碼：
```python
def displaySequenceOfNumbers (m, n):
	while m <= n:
		print (m)
		m = m + 1
```
請將以上程式片段改寫為recursive的形式。

#### 10. (Fibonacci Sequence)
求出費氏數列的第n項。該數列從第一項開始依序為: 1, 1, 2, 3, 5, 8, 13...
```
Enter a positive integer: 7
Fibonacci number: 13
```

#### 12. (Mortgage)
房貣計算方式如下：  
p: 貨款額度  
pmt: 月付額  
r: 年rate  
n: 期數  
balance函數則表示在經過n期後所欠的款項。 (note: 在n=0時，balance為p)  
```python
balance (p, pmt, r, n) = (1 + (r / 1200)) * balance (p, pmt, r, n - 1) - pmt
```
```
Enter the principal: 204700
Enter the annual rate of interest: 4.8
Enter the monthly payment: 1073.99
Enter the number of monthly payments made: 300
The amount still owed is $57,188.74.
```
