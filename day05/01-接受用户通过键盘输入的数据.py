import argparse
# 执行方式 python xxx.py -number 100
parser = argparse.ArgumentParser(description="这个程序用来演示参数处理")
# -number 表示 number 参数是可选参数 不加 - 表示必选
parser.add_argument('-number1', type=int, default=10, help='输入一个数字')
# 强制转换参数类型和设置默认值
parser.add_argument('-number2', type=int, default=20, help='输入一个数字')
args = parser.parse_args()
print(f"你输入的两数之和是 {args.number1+args.number2}")
