# -*- coding: utf-8 -*-
import os  # 导入os模块，模块的概念后面讲到

print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x*x)
print(L)

# 列表生成式

print([x*x for x in range(1, 11)])


print([x*x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in "ABC" for n in "XYZ"])


print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录


d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k, v in d.items():
#     print(k, '=', v)

print([k + '=' + v for k, v in d.items()])


L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

print([x for x in range(1, 11) if x % 2 == 0])


print([x if x % 2 == 0 else -x for x in range(1, 11)])

L1 = ['Hello', 'World', 18, 'Apple', None]
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L2 = [s.lower() for s in L1 if isinstance(s, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
