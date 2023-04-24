mylist = [21, 25, 21, 23, 22, 20]

mylist.append(31)

mylist.extend([29, 33, 30])

print(f"从列表中取出第一个元素{mylist[0]}")

print(f"从列表中取出最后一个元素{mylist[-1]}")


print(f"元素31的下标位置是 {mylist.index(31)}")
print(mylist)
