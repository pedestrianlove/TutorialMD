# 109-1 Python HW2

## 中文題目(概要)
### 54
給你收入、支出，
叫你算淨利。
### 56
給你起薪，加薪5%三次，
叫你算出加薪三次後的薪水、漲幅。
### 58
給定年份、利息和未來的價值（某財産），
叫你倒推出現在的投資額。
### 102
輸入一個句子，
叫你輸出第一個單詞和最後一個單詞(不含句點)。
### 104
輸入一個名字(有三段的那種)，
叫你輸出中間的那個單詞。
### 1
給你0~99元(美分)，
叫你分別用25、10、5、1元來找錢。(要分別輸出分部情況)
### 2
給定總貨額(loan)、利息%(interest rate)、年份(years)和公式：
\\[monthlyPayment = \frac{i}{1-(1+i)^{-12\cdot years}} \cdot loan \\]
where \\[i = \frac {interestRate}{1200}\\]
叫你算月付(monthly payment)多少。
### 3
給你face value, coupon interest rate, current market price, years until maturity以及公式如下：
\\[a = \frac{faceValue - currentMarketPrice}{yearsUntilMaturity}\\]
\\[b = \frac{faceValue + currentMarketPrice}{2}\\]
\\[YTM = \frac{couponInterestRate\cdot faceValue + a}{b}\\]
叫你算YTM。
### 4
給你ounces, pounds, 單價，
叫你算每ounces多少$ (1 pound = 16 ounces)
### 5
給你4種ETF的投資額，
叫你算出分別占了多少比例、共投資了多少$。(感覺重點是格式化)
### 6
給你miles, yards, feet, inches，（也給你公式）
叫你算出對應的km, m, cm(有小數點)。
去掉小數的處理中，必需利用int ()。




## References
我寫題目時用到的，可以參考。
### 54, 56, 58: 
https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators 
https://stackoverflow.com/questions/8885663/how-to-format-a-floating-number-to-fixed-width-in-python
https://stackoverflow.com/questions/52953258/underlining-user-input-in-python3
https://careerkarma.com/blog/python-print-without-new-line/

### 102, 104: 
https://www.programiz.com/python-programming/methods/string/rstrip https://www.programiz.com/python-programming/methods/string/split

### 1, 2, 3, 4, 5, 6
https://en.wikipedia.org/wiki/Coins_of_the_United_States_dollar
https://stackoverflow.com/questions/20201706/overflowerror-34-result-too-large
https://docs.python.org/3/library/decimal.html
https://stackoverflow.com/questions/32808383/formatting-numbers-so-they-align-on-decimal-point


