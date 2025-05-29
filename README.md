# Cardiac Diagnostic: Detecting RWMA in 2D Echocardiography

This project presents a deep learning-based system for the automated detection of Regional Wall Motion Abnormalities (RWMA) in 2D echocardiographic images. By integrating classification and segmentation modules, the system aims to enhance diagnostic accuracy and assist clinicians in cardiac assessments.

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Datasets](#datasets)
- [Methodology](#methodology)
- [Results](#results)
- [Visualizations](#visualizations)
- [Interactive Notebooks](#interactive-notebooks)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [References](#references)

## Introduction

Regional Wall Motion Abnormalities are critical indicators of myocardial dysfunction, often associated with ischemic heart disease. Traditional manual interpretation of echocardiographic images is time-consuming and subject to variability. This project leverages advanced deep learning techniques to automate the detection and analysis of RWMA, aiming to improve diagnostic efficiency and accuracy.

## Project Overview

The system comprises two primary components:

1. **Abnormality Detection Module**: Utilizes CNN architectures (Custom VGGNet, ResNet, and EfficientNet) to classify echocardiographic images as normal or exhibiting RWMA.

2. **Segmentation Module**: Employs a Custom U-Net model to segment regions of interest (e.g., left ventricle) in 2D echocardiographic images, providing detailed anatomical information to support the classification task.

By combining these modules, the system enhances interpretability and provides a comprehensive tool for cardiac diagnostics.

## Datasets

- **EchoNet-Dynamic**: A large-scale dataset of echocardiogram videos with labeled measurements, used for training and evaluating the classification models.

- **CAMUS**: Contains annotated 2-chamber and 4-chamber echocardiographic images, utilized for training the segmentation model.

## Methodology

- **Classification Models**: Implemented Custom VGGNet, ResNet, and EfficientNet architectures using the TensorFlow framework to classify images based on the presence of RWMA.

- **Segmentation Model**: Developed a Custom U-Net model to accurately segment the left ventricle and other relevant cardiac structures.

- **Integration**: Combined the outputs of both modules to provide a comprehensive diagnostic tool that not only detects abnormalities but also localizes them within the cardiac anatomy.

## Results

- **Classification Performance**:
  - EfficientNet achieved the highest accuracy in detecting RWMA among the tested models.

- **Segmentation Performance**:
  - The Custom U-Net model attained a Dice coefficient of 0.89, indicating high overlap between predicted and ground truth masks.

These results demonstrate the effectiveness of the integrated approach in accurately detecting and localizing RWMA in 2D echocardiographic images.

## Visualizations

The following visualizations provide insights into the model architectures, training processes, and results:

- **Model Architectures**:
  - **![VGGNet Architecture]**![VGGNet Architecture](https://github.com/user-attachments/assets/147ed695-3210-4c1d-b8e4-369dcc9748e0)

  - **![UNet Architecture]**![UNet Architecture](https://github.com/user-attachments/assets/2b747cfe-37e8-48fb-b521-7e37368d74d5)


- **Training Metrics**:
  - ![Classification Loss]![loss echo](https://github.com/user-attachments/assets/deaaff9e-82f7-4fe6-b597-dfcc3e1e0054)

  - ![Classification Accuracy]![training echo](https://github.com/user-attachments/assets/b5298db1-ac6a-4659-84e8-11bb61764762)

  - ![Segmentation Loss]![segment loss](https://github.com/user-attachments/assets/62a64c5f-0571-460d-b2a6-33e4a86097a2)

  - ![Segmentation Dice Score]![segment dice](https://github.com/user-attachments/assets/cd5a2846-b1be-484d-8c35-68bdbd45aa88)

  - ![Segmentation Training Progress]![segment train](https://github.com/user-attachments/assets/ad9e5e1b-74ba-4664-b539-9a250abb4b23)


- **Results**:
  - ![Classification Result]![Result](https://github.com/user-attachments/assets/7f6b1c5c-3041-4366-9018-161f5101f27d)

  - ![Segmentation Output]![Segmentation](https://github.com/user-attachments/assets/3a007e59-46af-4e8a-8d7c-8a11f8e195cd)


## Interactive Notebooks

Explore the project's code and results through the following interactive files:

- [Echocardiographic_Abnormality.html](Echocardiographic_Abnormality.html): Detailed analysis and visualization of the classification module.

- [Echocardiographic_Image_Segmentation.html](Echocardiographic_Image_Segmentation.html): Comprehensive overview of the segmentation process and results.

- [Echocardiographic_Image_Segmentation.ipynb](Echocardiographic_Image_Segmentation.ipynb): Jupyter Notebook containing the code for the segmentation model.

## Conclusion

The integration of classification and segmentation modules using advanced CNN architectures has proven effective in detecting RWMA in 2D echocardiographic images. EfficientNet demonstrated superior performance in classifying images, while the Custom U-Net model provided accurate segmentation of cardiac structures. This combined approach enhances the interpretability and reliability of automated RWMA detection, offering a valuable tool to assist clinicians in cardiac diagnostics.

## Future Work

- Incorporate temporal dynamics by analyzing echocardiographic video sequences to capture motion patterns.

- Expand the system to detect other cardiac abnormalities and pathologies.

- Integrate the tool into clinical workflows and evaluate its performance in real-world settings.

## References

- [EchoNet-Dynamic Dataset](https://echonet.github.io/dynamic/)
- [CAMUS Dataset](https://www.creatis.insa-lyon.fr/Challenge/camus/)

---

*Note: For optimal viewing of the interactive HTML files, please open them in a web browser.*
