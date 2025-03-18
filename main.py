import time
import random


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            people = content.split('\n\n')
            result = []
            for person in people:
                lines = person.strip().split('\n')
                info = {}
                for line in lines:
                    if ': ' in line:
                        key, value = line.split(': ', 1)
                        info[key] = value
                result.append(info)
            return result
    except FileNotFoundError:
        print("错误: 文件未找到!")
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")
    return []


def simulate_progress():
    messages = [
        "正在更新源......",
        "正在访问SGK......",
        "正在搜索🔍......",
        "正在索引🔍......"
    ]
    for _ in range(3):
        message = random.choice(messages)
        print(message)
        time.sleep(random.uniform(0.2, 0.7))


def search_info(data, query):
    for person in data:
        values = list(person.values())
        if query in values:
            for key, value in person.items():
                print(f"{key}: {value}")
            return True
    return False


if __name__ == "__main__":
    file_path = 'identity_info.txt'
    data = read_file(file_path)
    if data:
        query = input("请提供信息: ")
        simulate_progress()
        if search_info(data, query):
            print("-- 查找完成✅ --")
        else:
            print("-- 查找失败❎ --")
            print("-- 该信息未存入SGK --")
    