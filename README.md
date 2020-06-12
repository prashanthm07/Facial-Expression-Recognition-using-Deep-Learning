![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.7-brightgreen.svg)![Tensorflow](https://aleen42.github.io/badges/src/tensorflow.svg)![stackoverflow](https://aleen42.github.io/badges/src/stackoverflow.svg)![Github](https://aleen42.github.io/badges/src/github.svg)

## Facial Expressions Recognition using Convolutional Neural Networks


### Description:
* Facial Expression Detection (csv) - This notebook contains the implementation of Convolutional Neural Networks using fer2013.csv dataset directly. 
* Facial Expression Detection (dir) - This notebook contains the implementation of Convolutional Neural Networks using fer2013.csv dataset using **Datagenerator Class of Keras** after splitting the csv dataset to directories. The code for converting the fer2013.csv file to directories is in **convertodir.py** 
* model_weights.h5 & model.json - These weights file and architecture file as json are generated after training the CNN model in **Facial Expression Detection (dir)** notebook. 
* model_filter.h5 & fer.json - These weights file and architecture file as json are generated after training the CNN model in **Facial Expression Detection (csv)** notebook.

### Dependencies:
* Python=3.7
* Tensorflow>=2.1
* opencv>=4.0.1
* keras>=2.3.1
#### Note: You can also create virtual environment using python3.7 and the use requirements.txt file as follows
`pip install -r requirements.txt`

* Once your dependencies installation is done, you can run the notebook files on jupyter notebook(if you are using Anaconda). 

### Real-Time Testing of our model:
* This can be done just by running **RealtimePredictions.py** 

`python RealtimePredictions.py` 

* You'll see a window pop up and you can find the predictions on your screen. (See the demo file below)




 Badges Copyright-[MIT © aleen42](https://github.com/aleen42/badges)