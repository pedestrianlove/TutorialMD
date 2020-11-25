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

### 26
