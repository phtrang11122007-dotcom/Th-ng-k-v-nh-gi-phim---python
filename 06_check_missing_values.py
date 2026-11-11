# 6. Kiểm tra dữ liệu bị thiếu

import pandas as pd

# Đọc dữ liệu
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
tags = pd.read_csv("data/tags.csv")
links = pd.read_csv("data/links.csv")

# Kiểm tra dữ liệu thiếu
print("=== DỮ LIỆU THIẾU TRONG MOVIES ===")
print(movies.isnull().sum())

print("\n=== DỮ LIỆU THIẾU TRONG RATINGS ===")
print(ratings.isnull().sum())

print("\n=== DỮ LIỆU THIẾU TRONG TAGS ===")
print(tags.isnull().sum())

print("\n=== DỮ LIỆU THIẾU TRONG LINKS ===")
print(links.isnull().sum())