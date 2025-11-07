from ultralytics import YOLO

# ------------------- 1. 加载模型 -------------------
# 加载一个官方预训练的YOLOv8n模型
# YOLO() 会自动在当前文件夹寻找模型文件，如果找不到就会尝试自动下载
print("正在加载 YOLOv8n 模型...")
model = YOLO("yolov8n.pt")
print("模型加载成功！")

# ------------------- 2. 指定图片并进行预测 -------------------
# 这就是您指定的测试图片
image_path = "2.JPG"

# 使用模型对图片进行预测
print(f"正在对图片 '{image_path}' 进行预测...")
results = model(image_path)
print("预测完成！")

# ------------------- 3. 显示并保存预测结果 -------------------
print("正在处理和显示结果... 按键盘上的任意键可以关闭弹出的图片窗口。")
# 遍历所有的预测结果（虽然只有一张图，但results总是一个列表）
for r in results:
    r.show()  # 这会弹出一个窗口显示带有标注的结果图

    # 将结果图保存到文件
    save_path = "result_2.jpg"
    r.save(filename=save_path)
    print(f"结果图已保存为: {save_path}")
