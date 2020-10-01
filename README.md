![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg) ![Python 3.7](https://img.shields.io/badge/Python-3.7-brightgreen.svg)![Tensorflow](https://aleen42.github.io/badges/src/tensorflow.svg)![stackoverflow](https://aleen42.github.io/badges/src/stackoverflow.svg)![Github](https://aleen42.github.io/badges/src/github.svg)

## Facial Expressions Recognition using Convolutional Neural Networks
### Branches:
- **master** : Contains files related to training the model and realtime testing. 
- **[deployment](https://github.com/mangipudiprashanth7/Facial-Expression-Recognition-using-Deep-Learning/tree/deployment)** : Contains files related to deployment of the deep learning model on web using **flask** micro framework.
- Either clone the repo or download the Zip file based on your need, and start working.
### Description:
* fer2013.csv.zip - This is the dataset I've used. Do extract that on to your local system.
* Facial Expression Detection (csv) - This notebook contains the implementation of Convolutional Neural Networks using fer2013.csv dataset directly. 
* Facial Expression Detection (dir) - This notebook contains the implementation of Convolutional Neural Networks using fer2013.csv dataset using **Datagenerator Class of Keras** after splitting the csv dataset to directories. The code for converting the fer2013.csv file to directories is in **convertodir.py** 
* model_weights.h5 & model.json - These weights file and architecture file as json are generated after training the CNN model in **Facial Expression Detection (dir)** notebook. 
* model_filter.h5 & fer.json - These weights file and architecture file as json are generated after training the CNN model in **Facial Expression Detection (csv)** notebook.

### Dependencies:
* Python=3.7
* Tensorflow>=2.1
* opencv>=4.0.1
* keras>=2.3.1
#### Installation of dependencies using Anaconda distribution
- Create a new virtual environment using conda 

  ```PowerShell
  conda create -n faceexpressions python=3.7 -y
  ```
- Activating our new virtual environment
 
  ```PowerShell
  conda activate faceexpressions
  ```
- Installing necessary libraries
 
  ```PowerShell
  pip install ipykernel
  ```
- I'd recommend you to use the display name same as environment name
 
  ```PowerShell
  python -m ipykernel install --user --name faceexpressions --display-name "faceexpressions"
  ```

- If you have want to install Tensorflow GPU then use below command

  ```PowerShell
  conda install tensorflow-gpu==2.0.0
  ```

- If you have want to install Tensorflow CPU then use below command

  ```PowerShell
  conda install tensorflow==2.0.0
  ```

- The below pip command installs keras, opencv, pandas, matplotlib, scikit-learn

  ```PowerShell
  pip install keras opencv-contrib-python pandas numpy matplotlib scikit-learn
  ```

- The below command install jupyter notebook on Anaconda Distribution

  ```PowerShell
  conda install jupyter
  ```

- Once your dependencies installation is done, you can run the notebook files on jupyter notebook(if you are using Anaconda) using below command. 

  ```PowerShell
  jupyter notebook
  ```

### Real-Time Testing of our model:
* This can be done just by running **RealtimePredictions.py** 

  ```PowerShell
  python RealtimePredictions.py
  ```

* You'll see a window pop up and you can find the predictions on your screen(I've cropped the window). (See the demo file below)

![GIF](https://github.com/mangipudiprashanth7/Facial-Expression-Recognition-using-Deep-Learning/blob/master/demo.gif)


### Result :
- The architechture that I've built is very pretty simple, and I was able to get an validation accuracy of around 60.25 and training accuracy around 85.25. 
- The accuracy can still be improved by tuning the hyperparameters of the model. We can even make this more accurate by also using Transfer Learning. 
 
 
 ###### Badges Copyright-[MIT © aleen42](https://github.com/aleen42/badges)
