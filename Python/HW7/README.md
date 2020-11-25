# 1091-Python-THU HW7

### 24
如果這個程式跑第二次會發生什麼？(假設執行目錄下原本沒有"ABC.txt"這個檔案)
``` python
import os.path
if os.path.isfile ("ABC.txt"):
	print ("File already exists.")
else:
	infile = open ("ABC.txt", 'w')
	infile.write ("a\nb\nc\n")
	infile.close ()
```

## 26、28 使用sets簡化下列函數，不用考慮list中的順序。
### 26
``` python
def findItemsInBoth (list1, list2):
	list3 = []
	for item in list1:
		if (item in list2) and (item not in list3):
			list3.append (item)
	return list3
```

### 28
``` python
names = ["Donald Shell", "Harlan Mills", "Donald Knuth", "Alan Kay"]
setLN = set ()	# empty set
for name in names:
	setLN.add (name.split ()[-1])
print (setLN)
```


