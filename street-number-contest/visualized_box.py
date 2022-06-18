import torch
import numpy as np
import cv2

label_path = '../data/street-number/labels/mchar_train/000012.txt'
image_path = '../data/street-number/images/mchar_train/000012.png'


# 坐标转换，原始存储的是YOLOv5格式
# Convert nx4 boxes from [x, y, w, h] normalized to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
def yolo_to_XY(x, w=640, h=640, padw=0, padh=0):
    """
    :param x: yolo-x
    :param w: yolo-w
    :param h: yolo-h
    :param padw:
    :param padh:
    :return:
    """
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = w * (x[:, 0] - x[:, 2] / 2) + padw  # top left x
    y[:, 1] = h * (x[:, 1] - x[:, 3] / 2) + padh  # top left y
    y[:, 2] = w * (x[:, 0] + x[:, 2] / 2) + padw  # bottom right x
    y[:, 3] = h * (x[:, 1] + x[:, 3] / 2) + padh  # bottom right y
    return y


def visualize():
    """
    借助cv2显示box和label, 检查定位是否准确
    :return:
    """
    # 读取labels
    with open(label_path, 'r') as f:
        lb = np.array([x.split() for x in f.read().strip().splitlines()], dtype=np.float32)  # labels
    # 读取图像文件
    img = cv2.imread(str(image_path))
    h, w = img.shape[:2]
    lb[:, 1:] = yolo_to_XY(lb[:, 1:], w, h, 0, 0)  # 反归一化
    print(lb)

    # 绘图
    for _, x in enumerate(lb):
        class_label = int(x[0])  # class
        # 圈出box
        cv2.rectangle(img, (round(x[1]), round(x[2])), (round(x[3]), round(x[4])), (0, 255, 0))
        # 显示label
        cv2.putText(img, str(class_label), (int(x[1]), int(x[2] - 2)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=(0, 0, 255), thickness=2)
    cv2.imwrite('../data/test.jpg', img)


visualize()
