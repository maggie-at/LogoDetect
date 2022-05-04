import json
import cv2

json_dir = '../data/street-number/mchar_val.json'  # json文件路径
out_dir = '../data/street-number/labels/mchar_val/'  # 输出的 txt 文件路径
img_dir = '../data/street-number/images/mchar_val/'  # 图片所在路径


def json_to_yolo():
    """
    将streetNumber数据集转为YOLOv5格式
    :return:
    """
    # 读取 json 文件数据
    with open(json_dir, 'r') as load_f:
        content = json.load(load_f)
    # 循环处理
    for t, value in content.items():
        tmp = t.split('.')
        filename = out_dir + tmp[0] + '.txt'

        # 左上角坐标(并非YOLOv5所要求的中心坐标)
        left = value['left']
        # 左上角坐标(并非YOLOv5所要求的中心坐标)
        top = value['top']
        # 字符高度 h
        height = value['height']
        # 字符宽度 w
        width = value['width']
        # 字符值
        label = value['label']

        # 获取全图宽、高
        image_cv = cv2.imread(img_dir + tmp[0] + '.png')
        image_height = image_cv.shape[0]
        image_width = image_cv.shape[1]

        for index in range(len(left)):
            bbox1 = top[index]  # 上
            bbox3 = bbox1 + height[index]  # 下
            bbox0 = left[index]  # 左
            bbox2 = bbox0 + width[index]  # 右

            # 计算 YOLOv5 数据格式所需要的作为中心点的比例形式的x, y, 以及比例形式的w, h
            x = ((bbox0 + bbox2) / 2) / image_width
            y = ((bbox1 + bbox3) / 2) / image_height
            w = (bbox2 - bbox0) / image_width
            h = (bbox3 - bbox1) / image_height

            fp = open(filename, mode="a+", encoding="utf-8")

            # 类别
            theLabel = label[index]

            # YOLOv5格式
            file_str = str(theLabel) + ' ' + str(round(x, 6)) + ' ' + str(round(y, 6)) + ' ' + str(round(w, 6)) + ' ' + str(round(h, 6))
            fp.write(file_str + '\n')

            fp.close()


json_to_yolo()
