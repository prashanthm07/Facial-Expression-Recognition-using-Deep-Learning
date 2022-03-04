![Python 3.7](https://img.shields.io/badge/Python-3.7-brightgreen.svg)![Tensorflow](https://aleen42.github.io/badges/src/tensorflow.svg)![stackoverflow](https://aleen42.github.io/badges/src/stackoverflow.svg)![Github](https://aleen42.github.io/badges/src/github.svg)

## Deployment of Facial Expression Recognition Model using Flask micro framework.

### Description :
- **app.py :** The app.py file is the main file in which I've written the code needed for flask deployment.
- **model.py :** In this file we've defined our helper functions which we use during predictions.
- **camera.py :** In this file, openCV is used to access your camera & also the model weights and architecture are loaded in this file. If you want to update the weights and architecture with your latest model, do change them at line 6 of this script.
- **haarcascade_frontalface_default.xml :** - This xml file is used to detect faces in the given frame. This is a [haar cascade](https://github.com/opencv/opencv/tree/master/data/haarcascades) built by Viola Jones.

### Usage:
- I'd always recommend you to create different virtual environment for deployment and development. as it helps. 
- Create the new conda virtual environment :
- `conda create -n faceexpressiondeployment python=3.7 -y`
- Activate the created venv :
- `conda activate faceexpressiondeployment`
- Install all the dependencies needed for deployment using single pip command
- `pip install -r requirements.txt`
- Finally, once the dependency installtion is completed, run our flask app
- `python app.py`

- You'd see something like this in your terminal 

![Terminal](https://github.com/mangipudiprashanth7/Facial-Expression-Recognition-using-Deep-Learning/blob/deployment/terminal.PNG)
- Now, in your browser open the url **http://0.0.0.0:5000/** or **localhost:5000**

- Below is the demo of the app that you'd see.

![OUTPUT](https://github.com/mangipudiprashanth7/Facial-Expression-Recognition-using-Deep-Learning/blob/deployment/webapp-demo.gif)
