# YOLOv8-based-indoor-navigation-project
![Python 3.9+](https://img.shields.io/badge/python-3.9-blue.svg) ![PyTorch 2.5.1](https://img.shields.io/badge/PyTorch-2.5.1-red.svg) ![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)

本项目基于 **YOLOv8**，是一个为大学与企业实际合作项目开发的室内导航标识识别系统。

本项目创建并训练了一个自定义的常见商场标识符数据集。该模型能够实时、准确地识别多种关键室内标识，为室内导航或辅助视觉系统提供支持。

## 💡 核心功能

本模型能够准确识别以下常见商场标识符：

* 🚻 **通用洗手间标识**
* 🚹 **男洗手间标识**
* 🚺 **女洗手间标识**
* ♿ **无障碍洗手间标识**
* 🔀 **楼梯间标识**
* 🆘 **紧急出口标识**

## 🚀 快速安装 (推荐)

本项目包含一个完整的 Conda 环境配置文件 `environment.yml`（基于 `py36.yaml`），可一键复现所有依赖。

### 1. 克隆项目

```bash
git clone [https://github.com/2722433006/YOLOv8-based-indoor-navigation-project.git](https://github.com/2722433006/YOLOv8-based-indoor-navigation-project.git)
cd YOLOv8-based-indoor-navigation-project
# 1. (推荐) 使用 environment.yml 一键创建
# (如果你上传的文件名是 py36.yaml, 请把这里改成 -f py36.yaml)
conda env create -f environment.yml

### 2. 激活环境
```bash
conda activate yolo_env
# (推荐) 使用你的自定义脚本
python train.py
python predict.py --source path/to/your/image.jpg
python my_test.py
