# 5. Hiển thị 5 dòng dữ liệu đầu tiên

import pandas as pd

# Đọc dữ liệu
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
tags = pd.read_csv("data/tags.csv")
links = pd.read_csv("data/links.csv")

# Hiển thị dữ liệu mẫu
print("=== 5 DÒNG ĐẦU TIÊN CỦA MOVIES ===")
print(movies.head())

print("\n=== 5 DÒNG ĐẦU TIÊN CỦA RATINGS ===")
print(ratings.head())

print("\n=== 5 DÒNG ĐẦU TIÊN CỦA TAGS ===")
print(tags.head())

print("\n=== 5 DÒNG ĐẦU TIÊN CỦA LINKS ===")
print(links.head())