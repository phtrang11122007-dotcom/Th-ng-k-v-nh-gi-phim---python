# 8. Kiểm tra điểm đánh giá bất thường

import pandas as pd

# Đọc dữ liệu
ratings = pd.read_csv("data/ratings.csv")

# Tìm điểm đánh giá nhỏ nhất và lớn nhất
print("Điểm đánh giá thấp nhất:", ratings["rating"].min())
print("Điểm đánh giá cao nhất:", ratings["rating"].max())

# Kiểm tra điểm đánh giá ngoài khoảng 0.5 đến 5.0
invalid_ratings = ratings[
    (ratings["rating"] < 0.5) |
    (ratings["rating"] > 5.0)
]

print("Số điểm đánh giá bất thường:", len(invalid_ratings))

# Hiển thị dữ liệu bất thường nếu có
print(invalid_ratings)