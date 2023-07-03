#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle

# Khởi tạo cửa sổ đồ họa và con rùa
window = turtle.Screen()
t = turtle.Turtle()

# Khởi tạo giá trị ban đầu
center_radius = 100
num_circles = 10
radius_increment = 20
angle = 360 / num_circles

# Vẽ các hình tròn trồng lên nhau
for _ in range(num_circles):
    t.circle(center_radius)
    center_radius += radius_increment
    t.left(angle)

# Đóng cửa sổ đồ họa khi hoàn thành vẽ
window.bye()

