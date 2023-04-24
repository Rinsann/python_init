tuple1 = ('米津玄师', '11', ['football', 'music'])

print(f"年龄所在的下标是 {tuple1.index('11')}")
print(f"学生的姓名是 {tuple1[0]}")


# 删除 tuple1 中 的 football
del tuple1[2][0]
print(f"删除后 {tuple1}")

# 增加爱好 coding 到 tuple1的list内
tuple1[2].append('coding')
print(tuple1)
