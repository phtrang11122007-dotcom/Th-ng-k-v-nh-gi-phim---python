# 9. Thống kê tổng quan dữ liệu

import pandas as pd

# Đọc dữ liệu
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Tính toán các chỉ tiêu
total_movies = movies["movieId"].nunique()
total_ratings = len(ratings)
total_users = ratings["userId"].nunique()
rated_movies = ratings["movieId"].nunique()
average_rating = ratings["rating"].mean()

# Hiển thị kết quả
print("=== THỐNG KÊ TỔNG QUAN MOVIELENS ===")

print("Tổng số phim:", total_movies)
print("Tổng số lượt đánh giá:", total_ratings)
print("Số lượng người dùng:", total_users)
print("Số phim có lượt đánh giá:", rated_movies)
print("Điểm đánh giá trung bình:", round(average_rating, 2))