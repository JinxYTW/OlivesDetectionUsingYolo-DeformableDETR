# Olive Detection with YOLO & Deformable DETR

## 📌 Description
This project was carried out during an internship at **FESB (Faculty of Electrical Engineering, Mechanical Engineering and Naval Architecture), University of Split**.  
The goal was to develop an **Artificial Intelligence model for olive detection on olive trees**, comparing two state-of-the-art computer vision approaches:  

- **YOLO (You Only Look Once)**: a convolutional neural network (CNN)-based model  
- **Deformable DETR**: a Transformer-based model  

## 📂 Repository Structure
├── Datasets/ # Datasets used for training and validation
├── YOLO/ # Notebooks for training and evaluating YOLO
├── DeformableDETR/ # Notebooks for training and evaluating Deformable DETR
├── Metrics/ # Notebooks for performance evaluation (mAP, IoU, etc.)
├── Docs/ # Bibliographic references and related documents
└── README.md # Project documentation

## ⚙️ Requirements
This project is mainly based on **Jupyter notebooks**.  
Before running, install Jupyter and the required libraries:  

```bash
pip install jupyter torch torchvision pandas
pip install transformers   # for Deformable DETR
pip install ultralytics    # for YOLO
```
💡 Alternatively, you can run the notebooks directly on Google Colab without local installation.

## 📊 Results
Models were compared using several metrics (mAP, IoU, precision, recall):
| Model           | mAP@0.5 | Precision | Recall |
| --------------- | ------- | --------- | ------ |
| YOLOv8m         | 0.80    | 0.80      | 0.72   |
| Deformable DETR | 0.75    | 0.95      | 0.90   |

## 👤 Author

Project carried out by Turpin Yohann during an internship at FESB, Split.
