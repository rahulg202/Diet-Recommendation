# Diet Recommendation System

A **Personalized Diet and Workout Recommendation System** that leverages advanced transformer-based approaches to deliver tailored diet and fitness suggestions. This system is powered by a fine-tuned **LLaMA 3-8B model with LoRA (Low-Rank Adaptation)**, trained on a curated dataset of diets, nutrition, lifestyles, and health conditions. The platform ensures actionable insights for users to improve their health and fitness outcomes.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Approach](#approach)
  - [Traditional Machine Learning](#traditional-machine-learning)
  - [Transformer-Based Approach](#transformer-based-approach)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [System Architecture](#system-architecture)
- [Usage](#usage)
- [Contact](#contact)

---

## Overview

This project addresses the lack of personalized diet and workout recommendations tailored to individual lifestyles, health conditions, and fitness goals. It combines custom dataset creation, transformer-based modeling, and an intuitive deployment framework to offer a robust solution.

---

## Features

- **Personalized Recommendations**: Tailored diet and workout plans based on user inputs such as demographics, health conditions, and goals.
- **Advanced AI Model**: Fine-tuned **LLaMA 3-8B model** using **LoRA** for efficient training.
- **Custom Dataset**: Curated data on diets, nutrition, and lifestyles scraped from reliable sources.
- **Scalable Deployment**: Flask-based API for easy integration into web and mobile applications.

---

## Approach

### Traditional Machine Learning

Initially, traditional classification models like **Random Forest** and **XGBoost**, as well as **content-based filtering**, were explored. However, due to:
- Limited availability of data on personalized diet recommendations based on lifestyle and health conditions.
- Lack of personalization capabilities in traditional models.

### Transformer-Based Approach

To overcome these challenges:
1. **Custom Dataset**: Scraped data from reliable online articles and resources on diets, health conditions, and lifestyles.
2. **Fine-tuning**: The **LLaMA 3-8B model** was fine-tuned using **LoRA** for efficient adaptation.
3. **Deployment**: Deployed using Flask for seamless integration and user interaction.

---

## Dataset

The dataset is curated by scraping the web for articles and data related to:
- Diet recommendations for specific health conditions.
- Lifestyles such as sedentary, active, and athletic.
- Nutritional needs based on demographics like age, gender, and BMI.

> **Note**: The dataset is private. For access, contact [rahul.gupta312002@gmail.com](mailto:rahul.gupta312002@gmail.com).

---

## Model Training

### Tools and Frameworks:
- **Model**: LLaMA 3-8B
- **Fine-Tuning Framework**: LoRA (Low-Rank Adaptation)
- **Dataset Processing**: Python, Pandas
- **Training Framework**: PyTorch, Transformers

### Steps:
1. **Data Preprocessing**:
   - Cleaning and structuring the scraped data.
   - Filtering relevant content for health conditions and dietary needs.
2. **Model Fine-Tuning**:
   - Adapted LLaMA 3-8B using LoRA to ensure efficient training with limited resources.
   - Loss optimization for accurate diet and workout predictions.
3. **Validation**:
   - Tested model accuracy with synthetic and real-world data scenarios.

---

## System Architecture

1. **Frontend**: (Optional) User Interface for input and results visualization.
2. **Backend**: Flask API serving the fine-tuned LLaMA model.
3. **Database**: For user profiles and caching results.
4. **Deployment**: Hosted on a cloud platform for scalability.

---

## Usage

### Input
1. Demographics: Age, gender, height, weight.  
2. Health conditions: Diabetes, hypertension, etc.  
3. Lifestyle: Sedentary, active, or athletic.  

### Example
| ![Image 1](https://github.com/user-attachments/assets/23a760ec-3ada-4788-a781-b994e8381e1b) | ![Image 2](https://github.com/user-attachments/assets/e1f2dea2-b7c7-415a-b0a1-968426902bfc) | ![Image 3](https://github.com/user-attachments/assets/206d12d6-6c29-409a-9acb-f4bc4bd3fe66) |
|:-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|



   
### Output
- Personalized diet and workout recommendations.
![image](https://github.com/user-attachments/assets/9693edc5-b141-4282-8e98-75340d7af611)

---

## Contact

For access to the custom dataset or any queries, contact:  
**Rahul Gupta**  
📧 [rahul.gupta312002@gmail.com](mailto:rahul.gupta312002@gmail.com)
