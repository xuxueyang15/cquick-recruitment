import cv2
import os
out_dir = "./output task1"
img_path1 = "./images/IMG_0179.JPG"
img_path2 = "./images/IMG_0528.JPG"
def a(img_path, name):
    img = cv2.imread(img_path)
    if img is None:
        print("图片读取失败：", img_path)
        return
    h, w, c = img.shape
    print(name, "|高度=", h, "宽度=", w, "通道数=", c)
    img_resize = cv2.resize(img, (400, 300))
    cv2.imwrite(os.path.join(out_dir, name + "_resize.jpg"), img_resize)
    img_crop = img[0:200, 0:250]
    cv2.imwrite(os.path.join(out_dir, name + "_crop.jpg"), img_crop)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(out_dir, name + "_gray.jpg"), img_gray)
a(img_path1, "img1")
a(img_path2, "img2")
