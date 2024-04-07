# Behviour Simulation  

This repo is the codebase for The Task 1 of **Adobe Behaviour Simulation Challenge** from Inter-IIT techmeet 12.0.  

## Table of Contents
* [Introduction](#intro)
* [Installation](#install)
* [Dataset](#dataset)
* [Training](#training)
* [Evaluation](#eval)
* [Future Work](#fut)
* [Acknowledgements](#ackn)

## Introduction <a name="intro"></a> 
In today’s digital age, the effectiveness of marketing strategies is predominantly gauged by their digital engagement metrics. Adobe’s Digital Experience Business, via the Adobe Experience Cloud, empowers businesses to craft and deliver exceptional digital experiences. The capabilities span across creating engaging, personalized customer experiences at scale, leveraging generative AI for content ideation and production, and delivering account-based marketing strategies.

This repository hosts the Adobe Social Media Engagement & Content Generation Challenge which was a part of the Inter-IIT tech meet 12.0 held at IIT Madras, aimed at addressing two crucial aspects of digital marketing:

1. Behavior Simulation: Predicting user engagement on social media content.
2. Content Simulation: Generating engaging content for social media.
   
The challenge is designed to assist marketers in estimating and maximizing user engagement through intelligent content creation and engagement prediction, utilizing tweets from Twitter enterprise accounts as the primary dataset. The challenge is divided into two tasks:  

### Task 1: Behavior Simulation
Given a tweet's content (including text, company, username, media URLs, timestamp), predict user engagement represented by the number of likes.

Objective: Estimate how engaging a tweet will be to the audience.
Data: 300K samples from Twitter enterprise accounts, spanning over the last five years.
Evaluation: RMSE between predicted and actual likes.  

### Task 2: Content Simulation
Given tweet metadata (company, username, media URL, timestamp), generate engaging tweet text.

Objective: Create content that resonates with the audience, potentially leading to high engagement metrics.
Data: 300K samples, mirroring Task 1's dataset for consistency.
Evaluation: BLEU, ROUGE, and CIDER scores to measure the quality of generated content.  

This repository is focused on our solution of Task 1, which aligned with [this](https://arxiv.org/pdf/2309.00359.pdf) paper which relies on training multimodals for understanding, simluating and optimizing content and behaviour. We finetune a model based on the GIT-LLM framework, which integrates the Generative Image-to-text Transformer (GIT) with Large Language Models (LLMs). The exact models can be found in the config file. This fusion allows for a robust mechanism where the model can predict user engagement based on the content of a tweet, including its textual and visual elements. By harnessing the strengths of both GIT for image understanding and LLMs for rich language understanding, our model offers a comprehensive approach to solve Task 1. 


## Installation  <a name="install"></a> 
1. Clone this repository
```bash
git clone https://github.com/Sanjh-Maheshwari/Behaviour-Simulation-Multimodal
cd Behaviour-Simulation-Multimodal
```

2. Install Packages
```bash
conda create -n git_llm python=3.10 -y
conda activate git_llm
pip install --upgrade pip  # enable PEP 660 support

pip install -r requirements.txt
pip install -e .
```

## Dataset  <a name="dataset"></a> 

## Training  <a name="training"></a> 

## Evaluation  <a name="eval"></a> 

## Future Works <a name="fut"></a> 

## Acknowledgements <a name="ackn"></a> 
The main source for this code : https://github.com/Ino-Ichan/GIT-LLM
