# 3. Kiểm tra số dòng và số cột của dữ liệu

import pandas as pd

# Đọc dữ liệu
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
tags = pd.read_csv("data/tags.csv")
links = pd.read_csv("data/links.csv")

# Hiển thị số dòng và số cột
print("=== KÍCH THƯỚC CÁC BẢNG DỮ LIỆU ===")

print("Movies:", movies.shape)
print("Ratings:", ratings.shape)
print("Tags:", tags.shape)
print("Links:", links.shape)

# Tạo bảng tổng hợp
summary = pd.DataFrame({
    "Tên file": ["movies.csv", "ratings.csv", "tags.csv", "links.csv"],
    "Số dòng": [
        movies.shape[0],
        ratings.shape[0],
        tags.shape[0],
        links.shape[0]
    ],
    "Số cột": [
        movies.shape[1],
        ratings.shape[1],
        tags.shape[1],
        links.shape[1]
    ]
})

print("\n=== BẢNG TỔNG HỢP ===")
print(summary)