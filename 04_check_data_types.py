# 4. Kiểm tra kiểu dữ liệu của các cột

import pandas as pd

# Đọc dữ liệu
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
tags = pd.read_csv("data/tags.csv")
links = pd.read_csv("data/links.csv")

# Kiểm tra kiểu dữ liệu
print("=== KIỂU DỮ LIỆU MOVIES ===")
print(movies.dtypes)

print("\n=== KIỂU DỮ LIỆU RATINGS ===")
print(ratings.dtypes)

print("\n=== KIỂU DỮ LIỆU TAGS ===")
print(tags.dtypes)

print("\n=== KIỂU DỮ LIỆU LINKS ===")
print(links.dtypes)