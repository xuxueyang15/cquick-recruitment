import cv2
import numpy as np
import os
def color_detect(img_path, out_folder, hsv_low, hsv_high, min_area=500):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    img = cv2.imread(img_path)
    if img is None:
        print("图片读取失败：",{img_path})
        return
    img_copy = img.copy()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hsv_low, hsv_high)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)   
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"\n===== {os.path.basename(img_path)} =====")
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < min_area:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.circle(img_copy, (cx, cy), 4, (0, 255, 0), -1)
        print(f"轮廓面积：{area:.1f} | 中心点坐标(cx,cy)=({cx}, {cy})")
    cv2.imwrite(os.path.join(out_folder, "mask.png"), mask)
    cv2.imwrite(os.path.join(out_folder, "result.png"), img_copy)
    print(f"输出保存至：{out_folder}")
HSV_LOW = np.array([90, 80, 60])
HSV_HIGH = np.array([125, 255, 255])
MIN_CONTOUR_AREA = 600  
img_list = [
    "image/blue1.png",
    "image/blue2.png",
    "image/blue3.png",
]

for idx, img_file in enumerate(img_list):
    output_dir = os.path.join("output task3",f"res_{idx}")
    color_detect(
        img_path=img_file,
        out_folder=output_dir,
        hsv_low=HSV_LOW,
        hsv_high=HSV_HIGH,
        min_area=MIN_CONTOUR_AREA
    )
