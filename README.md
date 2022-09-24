# File Transfer System

Traffic sign classification is the process of automatically recognizing traffic signs along the road, including yield signs, pedestrians, children crossing, priority signs etc. Automatic recognition of traffic signs enables us to build "smarter cars". In order to understand and properly parse the roadway, Self-driving cars need traffic sign recognition. Similarly, “driver alert” systems inside cars need to understand the roadway around them to help aid and protect drivers. Traffic sign recognition is just one of the problems that computer vision and deep learning can solve.

While building a self-driving car, it is necessary to make sure it identifies the traffic signs with a high degree of accuracy, otherwise the results might be catastrophic. To solve this problem we use CNN and Keras and built a deep neural network model that can classify traffic signs present in the image into different categories.

This repository contains:

1. The [python code](Traffic_Sign_Classifier.py)
2. The [GUI Outputs](GUI.png)
3. [Datasets](https://github.com/Viknesh-Rajaramon/Traffic-Sign-Classification/tree/main/Datasets)
4. [Loss graph](Training_and_Testing_loss_graph.jpg)
5. [Accuracy graph](Training_and_Testing_accuracy_graph.jpg)
6. [ReadMe file](README.md) itself


## GUI Output
![Traffic Sign Classification GUI](https://github.com/Viknesh-Rajaramon/Traffic-Sign-Classification/blob/main/GUI.png "Title")


## Result
Achieved an accuracy score of 94.37%.
<br>
CNN training loss and testing loss graph:
<br>
<img src = "https://github.com/Viknesh-Rajaramon/Traffic-Sign-Classification/blob/main/Training_and_Testing_loss_graph.jpg" width="600">
<br>
CNN training accuracy and testing accuracy graph:
<br>
<img src = "https://github.com/Viknesh-Rajaramon/Traffic-Sign-Classification/blob/main/Training_and_Testing_accuracy_graph.jpg" width="600">


## To Run

Download the [Datasets](https://github.com/Viknesh-Rajaramon/Traffic-Sign-Classification/tree/main/Datasets) and save the downloaded folders in a folder titled 'omniglot'. Save the [python code](Traffic_Sign_Classifier.py) in the same directory as the 'datasets'.

```
Traffic_Sign_Classifier.py
Datasets
│___  Input
│___  Test
│___  Train
│___  Test.csv
│___  Train.csv
```

Make sure you have the following libraries installed to run the code.
```
numpy
pandas
matplotlib
scikit-learn
keras
tkinter
pillow
```

Download the following files in the same directory.
```
Traffic_Sign_Classifier.py
```

Run Traffic_Sign_Classifier.py
```
cd directory-where-the-files-are-saved
python3 Traffic_Sign_Classifier.py
```


## Team Members

Rithic Kumar
<br>
Sreedhar Arumugam
<br>
[Shresta M](https://github.com/shresta-m/Traffic_sign_classification)
<br>
R Shreja
