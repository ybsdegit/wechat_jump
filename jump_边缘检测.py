#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/7/10 14:04
# @author: Paulson●Wier
# @file: jump_边缘检测.py
# @desc:

import cv2
import numpy as np

# 读取原图像
img = cv2.imread('game.png', 0)

# 显示原图像
cv2.namedWindow('img', 0)
cv2.resizeWindow('img', 400, 600)
cv2.imshow('img', img)

# 高斯模糊
img_rgb = cv2.GaussianBlur(img, (5,5), 0)
canny_img = cv2.Canny(img_rgb, 1, 10)

# 显示边缘检测图像
cv2.namedWindow('canny', 0)
cv2.resizeWindow('canny', 400, 600)
cv2.imshow('canny', canny_img)



# 输出边缘检测图像的高和宽
H, W = canny_img.shape
print(H, W)

# 第一个顶点的高度，row为列表（代表每一行的像素值）， max(row) 获取列表中最大的像素值
# 对图像高度大于400的行进行遍历（这样可以去除上方数字以及小程序块的影响）。
# np.nonzero() 表示获取列表元素数值不为0的位置，
y_top = np.nonzero([max(row) for row in canny_img[420:]])[0][0] + 420
print('y_top: ',y_top)


# 获取第一个顶点的宽度值
x_top = int(np.mean(np.nonzero(canny_img[y_top])))
print('x_top: ',x_top)

# 跳过小白圈，然后遍历
y_bottom = y_top + 125
for row in range(y_bottom, H):
    if canny_img[row, x_top] != 0:
        y_bottom = row
        break

# 得到方块的中心点
x_center, y_center = x_top, (y_top + y_bottom)//2

# 绘制以方块中心点为圆心的圆
cv2.circle(canny_img, (x_center, y_center), 33, (255, 0, 0), 3)

cv2.namedWindow('result', 0)
cv2.resizeWindow('result', 400, 600)
cv2.imshow('result', canny_img)

print(f"目标方块中心点({x_center},{y_center})",)
cv2.waitKey(0)
cv2.destroyAllWindows()