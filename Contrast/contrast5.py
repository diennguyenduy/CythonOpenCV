import cv2
import time
import contrast_ceil
import numpy as np
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw_low.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
print(f'width = {img.shape[1]}, height = {img.shape[0]}')
start_time = time.time()

outimg = contrast_ceil.adjust_contrast(img, 3)

elapsed_time = time.time() - start_time
print(elapsed_time)


cv2.imshow('image', np.array(outimg))
cv2.waitKey(0)
cv2.destroyAllWindows()