# Behviour Simulation  

This repo is the codebase for The Task 1 of **Adobe Behaviour Simulation Challenge** from Inter-IIT techmeet 12.0.  

## Table of Contents
* [Introduction](#intro)
* [Methodology](#method)
* [Installation](#install)
* [Dataset](#dataset)
* [Training](#training)
* [Evaluation](#eval)
* [Future Work](#fut)
* [Acknowledgements](#ackn)
* [Support](#sup)

## Introduction <a name="intro"></a> 
In today’s digital age, the effectiveness of marketing strategies is predominantly gauged by their digital engagement metrics. Adobe’s Digital Experience Business, via the Adobe Experience Cloud, empowers businesses to craft and deliver exceptional digital experiences. The capabilities span across creating engaging, personalized customer experiences at scale, leveraging generative AI for content ideation and production, and delivering account-based marketing strategies.

This repository hosts the Adobe Social Media Engagement & Content Generation Challenge which was a part of the Inter-IIT tech meet 12.0 held at IIT Madras, aimed at addressing two crucial aspects of digital marketing:

1. Behavior Simulation: Predicting user engagement on social media content.
2. Content Simulation: Generating engaging content for social media.
   
The challenge is designed to assist marketers in estimating and maximizing user engagement through intelligent content creation and engagement prediction, utilizing tweets from Twitter enterprise accounts as the primary dataset. The challenge is divided into two tasks:  

### Task 1: Behavior Simulation
Given a tweet's content (including text, company, username, media URLs, timestamp), predict user engagement represented by the number of likes.

- **Objective**: Estimate how engaging a tweet will be to the audience.
- **Data**: 300K samples from Twitter enterprise accounts, spanning over the last five years.
- **Evaluation**: RMSE between predicted and actual likes.

### Task 2: Content Simulation
Given tweet metadata (company, username, media URL, timestamp), generate engaging tweet text.

- **Objective**: Create content that resonates with the audience, potentially leading to high engagement metrics.
- **Data**: 300K samples, mirroring Task 1's dataset for consistency.
- **Evaluation**: BLEU, ROUGE, and CIDER scores to measure the quality of generated content.  

## Methodology  <a name="method"></a> 

This repository is focused on our solution of Task 1, which aligned with [this](https://arxiv.org/pdf/2309.00359.pdf) paper which relies on training multimodals for understanding, simluating and optimizing content and behaviour. We finetune a model based on the GIT-LLM framework, which integrates the Generative Image-to-text Transformer (GIT) with Large Language Models (LLMs). This fusion allows for a robust mechanism where the model can predict user engagement based on the content of a tweet, including its textual and visual elements. By harnessing the strengths of both GIT for image understanding and LLMs for rich language understanding, our model offers a comprehensive approach to solve Task 1. 

Specifically, we utilize : 
- Llama-2-7b-chat-hf as our LLM 
- clip-vit-base-patch16 as our Vision Encoder

We also utilize **Low Rank Adaptation (LoRA)** for efficiently training the models using limited hardware. Basically, we finetune the model on Visual Q&A task where we instruct the model to predict number of likes foe the given image. This aligns with the reason for utilizing chat model instead of base model.

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

As mentioned in the introduction of Task 1, the dataset consisted of 300,000 sames from Twitter enterprise acounts, spanning over last five years. It consisted of following columns : 

| Column Name       | Description                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------------------|
| date              | The timestamp when the tweet was posted. Provides contextual timing information.                     |
| content           | The textual content of the tweet, crucial for engaging the audience.                                 |
| username          | The Twitter account's username that posted the tweet, influencing engagement due to its reputation.  |
| media             | URLs to any included media (images, videos) in the tweet, which can significantly impact engagement. |
| inferred company  | The company name associated with the tweet, inferred from the username or content.                   |
| likes (label)           | The number of likes the tweet received, serving as a direct measure of user engagement.              |  

We have following dataset files : 
- ***data/behaviour_simulation_train.xlsx*** : 300K train dataset
- ***data/filtered_data.xlsx*** : 300k train samples with local path i.e. actually used foe training
- ***data/behaviour_simulation_test_company.xlsx*** : 10k samples used for evaluation
  
## Training  <a name="training"></a> 

We used personal hardware which consisted o multiple GPUs for training the model as finetuning LLMs is really hardware intensive. We also utilized deepspeed [zero1](https://www.deepspeed.ai/tutorials/zero/) optimization which helped in significantly encing training speed but it came at a cost of high GPU utilization. We train for 1 epoch which took around 24 hours on our GPU machine. Training was conducted using mixed precision `fp16` and `adamw_torch` optimizer with `5.0e-5` learning rate. We used `wandb` for logging and for tracking loss. Finally, LoRA was employed on `q_proj` and `v_proj` of the Llama2 architecture for parameter efficient training. 

## Evaluation  <a name="eval"></a>  

For evaluation, we provide notebook and checkpoint for testing the model on sample data and also calculate RMSE which was the metric used for evaluation of our model. Follow following steps : 
1. First download the checkpoint of the model using gdown
```
gdown --id 1zc-NCElKHqu1nOorfbXjbYSChM_R8TM3
```

2. Relocate the model
```
output/exp050_llama/checkpoint-9235
```

3. Finally, run the inference notebook. 

## Future Works <a name="fut"></a> 

In this work, we trained a very prelaminary multimodal for the task. To extend this work one can deep dive into the training data and method described in the [paper](https://arxiv.org/pdf/2309.00359.pdf)) which also describes additional pretraining steps. Finally, one can also look at newer models like [Llava](https://github.com/haotian-liu/LLaVA).

## Acknowledgements <a name="ackn"></a> 
The main source for this code : https://github.com/Ino-Ichan/GIT-LLM  

## Support <a name="sup"></a>
There are many ways to support a project - starring⭐️ the GitHub repo is just one. 
