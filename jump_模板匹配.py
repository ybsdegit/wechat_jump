#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/7/10 10:16
# @author: Paulson●Wier
# @file: jump_模板匹配.py
# @desc:
import time

import cv2

# 读取待检测图像
img = cv2.imread('game1.png', 0)
# 读取模板图像
temple = cv2.imread('temple.png', 0)
#
# # 显示灰度处理后的待检测图像
# cv2.namedWindow('sample', 0)
# cv2.resizeWindow('sample', 400, 600)
# cv2.imshow('sample', img)
#
# # 显示灰度处理后的模板图像
# cv2.namedWindow('target', 0)
# cv2.resizeWindow('target', 400, 600)
# cv2.imshow('target', temple)
# # cv2.waitKey(20)
# # time.sleep(2)

# 获取模板图像的高和宽
th, tw = temple.shape[:2]
# print(th, tw)

# 使用标准相关系数匹配，1表示完美匹配， -1表示糟糕匹配， 0表示没有任何相关性
result = cv2.matchTemplate(img, temple, cv2.TM_CCOEFF_NORMED)

# TM_CCOEFF_NORMED 方法处理后的结果图像
# cv2.namedWindow('match_r', 0)
# cv2.resizeWindow('match_r', 400, 600)
# cv2.imshow('match_r', result)
# cv2.waitKey(10)

# 使用函数 minMaxloc, 确定匹配结果矩阵的最大值和最小值（val），以及它们的位置（loc）
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# 此处选取最大值的位置，为图像的左上角
t1 = max_loc
# 获取图像的右下角
br = (t1[0] + tw, t1[1] + th)
# 绘制矩形框
cv2.rectangle(img, t1, br, (0,0,225),2)
print("矩形框坐标",t1,br)
t_x_center = (t1[0]+br[0]) // 2
t_y_center = int(max_loc[1]*0.25 + br[1]*0.75)
print(f"跳块中心点坐标({t_x_center},{t_y_center})")
# 绘制以方块中心点为圆心的圆
cv2.circle(img, (t_x_center, t_y_center), 33, (255, 0, 0), 3)

cv2.namedWindow('result', 0)
cv2.resizeWindow('result', 400, 600)
cv2.imshow('result', img)

# 设置显示窗口
cv2.namedWindow('match', 0)
cv2.resizeWindow('match', 400, 600)
# 显示窗口
cv2.imshow('match', img)

# 结束
cv2.waitKey(0)
cv2.destroyAllWindows()