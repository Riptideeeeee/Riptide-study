# 编写两个函数：
# 1. celsius_to_fahrenheit(c)：摄氏转华氏（公式：°F = °C × 1.8 + 32）
# 2. fahrenheit_to_celsius(f)：华氏转摄氏（公式：°C = (°F - 32) ÷ 1.8）
f=0
c=0
def celsius_to_fahrenheit(c):
    f=c*1.8+32
    return f  # 请填写

def fahrenheit_to_celsius(f):
    c=(f-32)*5/9
    return c # 请填写

# 测试
print(celsius_to_fahrenheit(0))    # 32
print(celsius_to_fahrenheit(100))  # 212
print(fahrenheit_to_celsius(32))   # 0