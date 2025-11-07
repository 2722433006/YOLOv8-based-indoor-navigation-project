YOLOv8-based-indoor-navigation-project
https://img.shields.io/badge/python-3.9-blue.svg
https://img.shields.io/badge/PyTorch-2.5.1-red.svg
https://img.shields.io/badge/License-AGPL_v3-blue.svg

This project is based on YOLOv8 and developed as an indoor navigation sign recognition system for university-enterprise collaboration projects.

We created and trained a custom dataset of common mall signage. The model can accurately recognize various key indoor signs in real-time, providing support for indoor navigation or visual assistance systems.

💡 Core Features
The model can accurately recognize the following common mall signage:

🚻 Restroom Sign

🚹 Men's Restroom Sign

🚺 Women's Restroom Sign

♿ Accessible Restroom Sign

🔀 Staircase Sign

🆘 Emergency Exit Sign

🚀 Quick Installation (Recommended)
Please follow these 4 steps:

1. Clone the Project
bash
git clone https://github.com/2722433006/YOLOv8-based-indoor-navigation-project.git
cd YOLOv8-based-indoor-navigation-project
2. Download Dataset
The dataset (datasets folder) is too large to be uploaded to GitHub (ignored via .gitignore).

Please manually download datasets.zip from the link below and extract it to the project root directory:

➡️ Download Dataset (datasets.zip)
(迅雷网盘链接, extraction code: fiA1)

3. Create Conda Environment
This project requires Python 3.9.23, PyTorch 2.5.1 and CUDA 12.1.

We provide a complete environment configuration file py36.yaml to create the environment with one command.

bash
conda env create -f py36.yaml
4. Activate and Use
bash
# Activate environment
conda activate yolo_env
Now you're ready to use the project!

🎮 How to Use
Make sure you have activated the yolo_env environment. This project includes several key custom scripts:

1. Train Model
The dataset is already configured. You can use the train.py script to start training:

bash
# (Recommended) Use your custom script
python train.py
Alternatively, you can use the ultralytics command line (make sure the .yaml configuration file path in datasets/ directory is correct):

bash
# (Or) Use Ultralytics command line
yolo train data=datasets/your_data.yaml model=yolov8n.pt epochs=100 imgsz=640
2. Make Predictions
After training, the best model will be saved in runs/detect/train/weights/best.pt.

Test on images (using predict.py):

bash
python predict.py --source path/to/your/image.jpg
Test on videos (using predict_video.py):

bash
python predict_video.py --source path/to/your/video.mp4
Run custom testing (using my_test.py):

bash
python my_test.py
📄 License
This project is licensed under the AGPL-3.0 License.
