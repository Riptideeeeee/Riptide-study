from openai import OpenAI
import sys
import json

try :#导入提示词
    with open("content1.txt","r",encoding="utf-8") as f:
        content1 = f.read()
    if content1 == "":
        content1 = "You are a helpful assistant"
        with open("content1.txt", "w", encoding="utf-8") as f:
            f.write(content1)
except FileNotFoundError:
    with open("content1.txt","w",encoding="utf-8") as f:
        content1 = "You are a helpful assistant"
        f.write(content1)

try :#导入api-key
    with open("api-key.txt","r",encoding="utf-8") as f:
        key = f.read()
    if key == "":
        print("你还没有在api-key.txt里面输入你的key！")
        with open("api-key.txt", "w", encoding="utf-8") as f:
            f.write(key)
except FileNotFoundError:
    print("你还没有在api-key.txt里面输入你的key！")
    with open("api-key.txt", "w", encoding="utf-8") as f:
        f.write('')
    sys.exit()

try:#导入历史对话
    with open("chat_history.json", "r", encoding="utf-8") as f:
        messages = json.load(f)  # 直接还原成Python列表
    print(f"成功加载 {len(messages)} 条历史消息")
except FileNotFoundError:
    # 如果文件不存在，就初始化一个新的对话
    messages = [{"role": "system", "content": content1}]
client = OpenAI(
        api_key=key,
        base_url="https://api.deepseek.com")
while True:
    content2 = input("请输入你的问题（输入 stop 结束对话）:")
    if content2 == "stop":
        break
    messages.append({"role": "user", "content": content2})

    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages,
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 分别提取并打印
    reasoning = response.choices[0].message.reasoning_content
    answer = response.choices[0].message.content
    print("\n" + "=" * 40 + "\n")
    print("🧠 思考过程：")
    print(reasoning)
    print("\n" + "=" * 40 + "\n")
    print("💬 最终回答：")
    print(answer)
    print("\n" + "=" * 40 + "\n")
    messages.append({"role": "assistant", "content": answer})
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
        print("\n==对话历史保存成功！==\n")
    print("\n" + "=" * 40 + "\n")

print("已结束对话")
# 保存为JSON文件
with open("chat_history.json", "w", encoding="utf-8") as f:
    json.dump(messages, f, ensure_ascii=False, indent=2)
    print("\n==对话历史保存成功！==\n")
print("\n" + "=" * 40 + "\n")
