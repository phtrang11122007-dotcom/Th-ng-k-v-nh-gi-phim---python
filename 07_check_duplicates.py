# 7. Kiểm tra dữ liệu trùng lặp

import pandas as pd

# Đọc dữ liệu
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
tags = pd.read_csv("data/tags.csv")
links = pd.read_csv("data/links.csv")

# Đếm số dòng trùng lặp
print("Số dòng trùng lặp trong movies:", movies.duplicated().sum())
print("Số dòng trùng lặp trong ratings:", ratings.duplicated().sum())
print("Số dòng trùng lặp trong tags:", tags.duplicated().sum())
print("Số dòng trùng lặp trong links:", links.duplicated().sum())