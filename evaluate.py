from ultralytics import YOLO


def main():
    # --- 关键：加载您自己训练好的模型 ---
    # 请将这里的路径替换成您在runs文件夹里找到的 best.pt 文件的真实路径
    model_path = "D:/data/ultralytics-main/runs/detect/signage_yolov8n_augmented_run_v24/weights/best.pt"
    model = YOLO(model_path)

    # --- 运行验证 ---
    # model.val() 会加载数据集，进行评估，并打印出带有完整标题的结果表格
    print("正在对模型进行评估...")
    model.val(data="signage_data.yaml")

    print("\n评估完成！")
    # 您还可以单独访问某个指标，例如：
    # print("mAP50-95:", metrics.box.map)
    # print("mAP50:", metrics.box.map50)


if __name__ == "__main__":
    main()
