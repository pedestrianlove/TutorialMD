# input
arr = input ("Enter a list of numbers seperated by spaces: ").strip ().split ()

# sort
for i in range (len (arr)):
        # i從0開始(arr的第一項)
        
        # 先假設沒找到比i項更小的值的話, 誰要跟i項交換(i自己)
        min_idx = i

        # 找出最小值所在的index (j從i項開始跑)
        for j in range (i, len (arr)):
                if arr[min_idx] > arr[j]:
                        min_idx = j

        # 把最小值放在arr的第i個位置 (i以前的已排好了)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# output
print (' '.join (arr))
