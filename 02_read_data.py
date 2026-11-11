# 2. Đọc dữ liệu MovieLens

import pandas as pd

# Đọc 4 file CSV từ thư mục data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
tags = pd.read_csv("data/tags.csv")
links = pd.read_csv("data/links.csv")

# Thông báo đọc dữ liệu thành công
print("Đọc dữ liệu thành công!")

# Hiển thị 5 dòng đầu tiên của mỗi bảng
print("\nDữ liệu movies:")
print(movies.head())

print("\nDữ liệu ratings:")
print(ratings.head())

print("\nDữ liệu tags:")
print(tags.head())

print("\nDữ liệu links:")
print(links.head())