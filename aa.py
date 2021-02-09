import numpy as np

arr = []
a0 = [""]*115
a1 = [" "]*4 + ["|"] + ["="]*109+["|"]
a2 = [" "]*4 + ["|"] + [" ","P","r","e","s","s"," ","[","P","]"," ","o","r"," ","[","p","]"," ","t","o"," ","p","a","u","s","e"] + [" "]*58 + ["P","r","e","s","s"," ","[","Q","]"," ","o","r"," ","[","q","]"," ","t","o"," ","q","u","i","t"," ","|"]
a3 = [" "]*4 + ["|"] + ["-"]*109+["|"]
a4 = [" "]*4 + ["|"] + [" "]*3 +["L","i","v","e","s"," ",":"," "] + [" "]*31 +["L","e","v","e","l"," ",":"," "] + [" "]*21 + ["S","c","o","r","e"," ",":"," "] + [" "]*30 + ["|"]
a5 = [" "]*4 + ["|"] + ["-"]*109+["|"]
a6 = [" "]*4 + ["|"] + [" "]*109+["|"]
a7 = [" "]*4 + ["|"] + [" "]*109+["|"]
a8 = [" "]*4 + ["|"] + ["/","\\"]*54 + ["/","|"]
a9 = [" "]*4 + ["|"]*111
aa = [" "]*4 + ["|"," "] + ["X"]*107 + [" ","|"]
arr.append(a0)
arr.append(a0)
arr.append(a0)
arr.append(a1)
arr.append(a2)
arr.append(a3)
arr.append(a4)
arr.append(a5)
arr.append(a6)
print(arr)
print("\n\n\n\n")
arr = []
for i in range(8,17):
    arr.append(aa)
print(arr)
print("\n\n\n\n")
arr = []
for i in range(17,30):
    arr.append(a7)
arr.append(a8)
arr.append(a1)
print(arr)
print("\n\n\n\n")
arr = []
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        print(arr[i][j],end="")
    print("\n",end="")

print(arr)
# arr.append(a)
# arr.append(a)
# b = ["*"]*10
# brr = []
# brr.append(b)
# brr.append(b)
# print(arr)
# print(brr)
# arr = np.array(arr)
# brr = np.array(brr)

# b = np.vstack([arr,brr])

# print(b)