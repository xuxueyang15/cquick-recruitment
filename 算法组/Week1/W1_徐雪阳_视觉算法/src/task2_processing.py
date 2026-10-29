import cv2
import numpy as np
import os
def a(img_path, out_folder):
    img = cv2.imread(img_path)
    if img is None:
        print("图片读取失败：", img_path)
        return
    cv2.imwrite(os.path.join(out_folder, "original.jpg"), img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(out_folder, "gray.jpg"), gray)
    gauss_light = cv2.GaussianBlur(gray, (3, 3), sigmaX=1)
    cv2.imwrite(os.path.join(out_folder, "blur_light_3x3.jpg"), gauss_light)
    gauss_heavy = cv2.GaussianBlur(gray, (7, 7), sigmaX=3)
    cv2.imwrite(os.path.join(out_folder, "blur_heavy_7x7.jpg"), gauss_heavy)
    ret_low, thresh_80 = cv2.threshold(gauss_heavy, 80, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(out_folder, "3_thresh_80.jpg"), thresh_80)
    ret_high, thresh_150 = cv2.threshold(gauss_heavy, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(out_folder, "3_thresh_150.jpg"), thresh_150)
    canny_low = cv2.Canny(gauss_heavy, threshold1=30, threshold2=100)
    cv2.imwrite(os.path.join(out_folder, "4_Canny_30_100.jpg"), canny_low)
    canny_high = cv2.Canny(gauss_heavy, threshold1=80, threshold2=200)
    cv2.imwrite(os.path.join(out_folder, "4_Canny_80_200.jpg"), canny_high)
    kernel = np.ones((5, 5), np.uint8)
    morph_close = cv2.morphologyEx(thresh_80, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(os.path.join(out_folder, "5_morph.jpg"), morph_close)
    print("✅任务二处理完成，输出目录：",out_folder)
IMG_FILE = "images/redcup.jpg"
OUT_DIR = "output task2"
a(IMG_FILE, OUT_DIR)
