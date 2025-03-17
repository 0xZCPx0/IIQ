import time
import random
import sys


def read_identity_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            people_info = content.split('\n\n')
            all_info = []
            for person in people_info:
                info = {}
                lines = person.strip().split('\n')
                for line in lines:
                    key, value = line.split(':', 1)
                    info[key.strip()] = value.strip()
                all_info.append(info)
            return all_info
    except FileNotFoundError:
        print("错误: 文件未找到!")
        return []
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")
        return []


def show_progress():
    messages = ["正在更新源......", "正在访问SGK......", "正在搜索🔍......", "正在索引🔍......"]
    for message in messages:
        print(f"-- {message} --")
        total_length = 50
        for i in range(total_length + 1):
            progress = '#' * i + ' ' * (total_length - i)
            sys.stdout.write(f"\r进度: [{progress}] {i * 2}%")
            sys.stdout.flush()
            # 随机生成一个休眠时间，范围在 0.01 到 0.5 秒之间，使快慢变化更明显
            time.sleep(random.uniform(0.01, 0.05))
        print()


def search_info(all_info, query):
    for info in all_info:
        if query in [info.get('名称'), info.get('手机号'), info.get('QQ'), info.get('微信ID'), info.get('身份证')]:
            return info
    return None


def main():
    file_path = 'identity_info.txt'
    all_info = read_identity_info(file_path)
    if not all_info:
        return
    query = input("请提供信息: ")
    show_progress()
    result = search_info(all_info, query)
    if result:
        print("-- 查找完成✅ --\n", 
                    "❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("-- 查找失败❎ --")
        print("-- 该信息未存入SGK --")


if __name__ == "__main__":
    main()