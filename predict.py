from ultralytics import YOLO

def main():
    # 加载你训练好的模型权重
    # 路径会是 runs/detect/signage_yolov8n_run/weights/best.pt
    model_path = 'D:/data/ultralytics-main/runs/detect/signage_yolov8n_augmented_run_v24/weights/best.pt' # <-- 确保这个 name 和训练时一致
    model = YOLO(model_path)

    # 推理的图片源，因为 2.JPG 就在同一个目录下，所以直接写文件名即可
    source_image = '2.JPG' # <-- 已根据您的截图更正

    # 执行推理
    results = model.predict(source=source_image, save=True, conf=0.5)

    print(f"推理完成！结果已保存。")

if __name__ == '__main__':
    main()