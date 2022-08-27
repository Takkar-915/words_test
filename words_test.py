import pandas as pd

# csvファイルの読み込み
file = open("./BBC_words.csv", "r", encoding="utf-8", newline="")

df = pd.read_csv(file, header=0, sep=",")

# csvファイルからテストを作成

test_data = {}

for i in range(len(df)):
    test_data[df.at[i, '単語']] = df.at[i, '意味']

# テスト開始
correctSum = 0
questionSum = len(test_data)
wrong_question = []  # 間違った単語を記録

print("英単語テストを開始します\n")
for key in test_data:
    correctAnswer = test_data[key]
    ans = input(key + "の意味を入力してください:")
    if ans == correctAnswer:
        print("正解！")
        correctSum += 1
    else:
        print("不正解！")
        print("正解は:" + correctAnswer)
        wrong_question.append([key, correctAnswer])

# 結果を表示
# 小数点第1位以下四捨五入
correctPercentage = round((correctSum / questionSum) * 100, 1)
print("テスト終了。正答率は" + str(correctPercentage) + "%です！")
print("以下は不正解だった単語です")


for k in range(len(wrong_question)):
    for l in range(len(wrong_question[k])):
        if l == 0:
            print("単語:" + wrong_question[k][l])
        elif l == 1:
            print("意味:" + wrong_question[k][l])
