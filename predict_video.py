import cv2

from ultralytics import YOLO


def main():
    # --- 1. 定义模型和视频路径 ---
    model_path = r"D:/data/ultralytics-main/runs/detect/signage_yolov8n_augmented_run_v24/weights/best.pt"
    video_path = r"D:\data\ultralytics-main\video.mp4"

    # --- 2. 加载模型和视频 ---
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"错误：无法打开视频文件 {video_path}")
        return

    # --- (第一处：新增代码) 初始化视频写入对象 ---
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    output_path = "predicted_video.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    # ------------------------------------

    # --- 3. 循环处理视频的每一帧 ---
    while cap.isOpened():
        success, frame = cap.read()
        if success:
            results = model(frame, stream=True)
            for r in results:
                annotated_frame = r.plot()
                cv2.imshow("YOLOv8 视频预测", annotated_frame)

                # --- (第二处：新增代码) 将处理后的帧写入视频文件 ---
                writer.write(annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    # --- 4. 释放资源 ---
    cap.release()
    # --- (第三处：新增代码) 释放写入对象 ---
    writer.release()
    cv2.destroyAllWindows()

    print(f"处理完成，预测结果已保存到文件: {output_path}")


if __name__ == "__main__":
    main()
