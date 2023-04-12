import random
import numpy as np
import cv2
from PIL import Image

size = {
	"width" : 500, 
	"height" : 500
}

rgb = [0, 0, 0]


IMAGE_PATH = "C:/Users/inkat/Code/python/Gadation/image/image01.png"

# グラデーションの生成
gradient = np.tile(0, (size["height"], size["width"], 3))
h=0
w=0
while h < size["height"]:
	while w < size["width"]:
		if h==0 and w==0:
			rgb[0] = np.float64(random.uniform(0,255))
			rgb[1] = np.float64(random.uniform(0,255))
			rgb[2] = np.float64(random.uniform(0,255))
		elif h==0:
			rgb[0] = np.float64(max(0,min(255, gradient[0][w-1][0]+random.uniform(-9, 10))))
			rgb[1] = np.float64(max(0,min(255, gradient[0][w-1][1]+random.uniform(-9, 10))))
			rgb[2] = np.float64(max(0,min(255, gradient[0][w-1][2]+random.uniform(-9, 10))))
		elif w==0:
			rgb[0] = np.float64(max(0,min(255, gradient[h-1][0][0]+random.uniform(-9, 10))))
			rgb[1] = np.float64(max(0,min(255, gradient[h-1][0][1]+random.uniform(-9, 10))))
			rgb[2] = np.float64(max(0,min(255, gradient[h-1][0][2]+random.uniform(-9, 10))))
		else:
			rgb[0] = np.float64(max(0,min(255, (gradient[h][w-1][0]+gradient[h-1][w][0])/2+random.uniform(-9, 10))))
			rgb[1] = np.float64(max(0,min(255, (gradient[h][w-1][1]+gradient[h-1][w][1])/2+random.uniform(-9, 10))))
			rgb[2] = np.float64(max(0,min(255, (gradient[h][w-1][2]+gradient[h-1][w][2])/2+random.uniform(-9, 10))))
		gradient[h][w][0] = rgb[0]
		gradient[h][w][1] = rgb[1]
		gradient[h][w][2] = rgb[2]
		w+=1
	w=0
	h+=1
# グラデーション画像の保存
# BGRで保存される
cv2.imwrite(IMAGE_PATH, gradient)
