#### [小样本商标检测](https://tianchi.aliyun.com/competition/entrance/531948/forum)

##### 1. Data - `fewshot_logo`
**Download**
> Download from [Contest page](https://tianchi.aliyun.com/competition/entrance/531948/information) or [Github](https://github.com/CarryHJR/LogDet)

**Original structure**
```
├── train
   ├── annotations
       ├── instances_train2017.json (in COCO format)
   ├── images
├── test
   ├── annotations
       ├── instances_test2017.json (in COCO format)
   ├── images
```

> Organized in YOLO format
```
├── r1 (for train phase)
    ├── images
        ├── train
        ├── val
    ├── labels
        ├── train
        ├── val
├── Round1 (for test phase)
    ├── images
        ├── train
        ├── val
    ├── labels
        ├── train
        ├── val (empty)
```


##### 2. Format transition
> reference: Weifeng-Chen/DL_tools(https://github.com/Weifeng-Chen/DL_tools)

**COCO to YOLO**
[`./utils/coco2yolo/coco_to_yolo.py`](./utils/coco2yolo/coco_to_yolo.py): transfer COCO into YOLO format (for input data)

**YOLO to COCO**
[`./utils/coco2yolo/yolo_to_coco.py`](./utils/coco2yolo/yolo_to_coco.py): transfer YOLO into COCO format (for output data)


##### 3. Train / Test spliting
[`utils/dataset_split/train_val_split.py`](./utils/dataset_split/train_val_split.py): split `origin-trainset` set with `[train=0.8, val=0.2]`


##### 4. Train YOLOv5
[`data/coco_logo.yaml`](./data/coco_logo.yaml): dataset config, mention that `nc=50`

[`YOLOv5l`](https://objects.githubusercontent.com/github-production-release-asset-2e65be/264818686/fbab4200-9af2-11eb-8e5d-7101b2c3b614?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220617%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220617T094901Z&X-Amz-Expires=300&X-Amz-Signature=133eca3eb04d194a2a0e0b07e87abc5245fb5ca393fc7fd32fa843836533c57c&X-Amz-SignedHeaders=host&actor_id=47021303&key_id=0&repo_id=264818686&response-content-disposition=attachment%3B%20filename%3Dyolov5l.pt&response-content-type=application%2Foctet-stream): Pay attention to version selection!

<img src="./appendix/train.png">


##### 5. Detect on Val set
> Don't know how to use `test.py`...

<img src="./appendix/detect.png">

Then convert the txt folder into json file with [`utils/coco2yolo/yolo_to_coco.py`](./utils/coco2yolo/yolo_to_coco.py)

Done.