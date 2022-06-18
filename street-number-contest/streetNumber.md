#### [街景字符编码识别](https://tianchi.aliyun.com/competition/entrance/531795/information)

> 正在找个可以应用YOLOv5的竞赛, 结果这个评论区正好有一些使用YOLOv5并且效果不错的题解, 趁机学习一下

##### 1. 数据集
* 保存数据至`data/street-number`文件夹下
* [转化为YOLOv5数据格式`{x, y, w, h, label}`](data_to_yolo.py)
* [测试坐标转换是否正确](street-number-contest/visualize_box.py)
* [设置数据集访问yaml文件](../data/streetNumber.yaml), 设置数据集路径及类别数`nc=10`

##### 2. 训练
> 需要调整用于train的数据集路径, 并根据GPU来选择模型参数规模
> 也可以在命令或者`parameters`中设置以下选项
```bash
python train.py --data data/streatNumber.yaml   # 标注数据集yaml文件及YOLOv5模型参数(如s,m,l,x等)
                --cfg models/yolov5s.yaml       # 选择模型规模
                --weights yolov5s.pt            # 已经训练好的模型权重, 不需要from scratch, 不设置的话效果很差, 需要更多epoch
                --img-size 300
                --batch-size 64
```

##### 3. 测试
```bash
python detect.py --weights runs\train\expXX\weights\best.pt --source data\images\mchar_test_a --save-txt
```
