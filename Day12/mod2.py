def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 수정 전
# print(add(1, 4))
# print(sub(4, 2))

# 수정 후
# if __name__ == "__main__": 구문 추가
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))