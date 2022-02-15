# Image Tagging Challenge
For workshop

BigData & AILab activity from Sep 29th 2021.

## To-do list
1. Create Fasteners and wire components dataset
2. Create Multi-label Image classification model whitch can add Japanese and English tags
3. Create a sample project to explain how to use created model
4. Write an article on note.com

## Dataset
We focus on fasteners and wire components.

I am the only one in charge of this project, so I'll save the dataset locally.

## About notebook
The lastest notebook about this project is on Google colab.[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18YxYSgaUemib1lpAY4RtaZQZtO86oLsj?usp=sharing)

## Sample project
[scenery-tagging-app(GitHub)](https://github.com/ryu-i-engineer/scenery-tagging-app)

## Flowchart
```mermaid
flowchart TD
  A[Start] --> B[Scraping images];
  B --> C[Data cleaning];
  C --> D[(Scenry Images Dataset)];
  D --> E{Is the dataset qualified?};
  E -- Yes --> F[Create a model and train];
  E -- No, get more images --> B;
  F --> G{How much is the loss?};
  G -- Less than 20% --> H[Create pairs of English and Japanese. Like these 1. Sky: 空 2. Mountain: 山 3. River: 川];
  G -- Greater than 20% --> E;
  H --> I[Create a web app using with created model];
  I --> J[Write an article about this project] --> END;
```
