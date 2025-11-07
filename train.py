from ultralytics import YOLO

def main():
    # 加载预训练模型
    model = YOLO('yolov8n.pt')

    # 开始训练，并加入自定义的数据增强参数
    results = model.train(
        data='signage_data.yaml',
        epochs=300,
        imgsz=640,
        batch=8,
        patience=50,
        name='signage_yolov8n_augmented_run_v2', # 建议换个新名字，以防覆盖旧的训练结果

        # --- 在这里添加或修改数据增强参数 ---

        # 几何变换增强
        degrees=30,      # 随机旋转的角度范围 (+/- 30 度)
        translate=0.1,   # 随机平移的范围 (+/- 10%)=
        scale=0.5,       # 随机缩放的范围 (0.5 - 1.5倍)
        shear=10,        # 随机剪切的角度范围 (+/- 10 度)
        perspective=0.001, # 随机透视变换的系数

        # 翻转增强
        flipud=0.0,      # 上下翻转的概率 (默认是0，对于很多物体如人、车不适用，但对某些标志牌可能有用)
        fliplr=0.0,      # 左右翻转的概率 (默认是0.5，非常常用)

        # 色彩空间增强 (默认值已经很好了，这里只是举例)
        hsv_h=0.015,     # 色调 (Hue) 增强范围
        hsv_s=0.7,       # 饱和度 (Saturation) 增强范围
        hsv_v=0.4,       # 明度 (Value) 增强范围

        # 高级增强 (YOLOv8默认开启，可以通过设置0来关闭)
        mosaic=1.0,      # Mosaic增强的概率 (将4张图拼接成1张)
        mixup=0.1,       # MixUp增强的概率 (将2张图混合)
        copy_paste=0.1   # Copy-Paste增强的概率 (将目标从一张图复制到另一张)
    )
    print("训练完成！")

if __name__ == '__main__':
    main()