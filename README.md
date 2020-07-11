# Landmark Detection and Tracking - Implementation of SLAM

## Overview

This project from Udacity's nano-degree course "Computer Vision" is about Landmark Detection and Tracking and the Implementation of Simultaneous Localization and Mapping (SLAM) for a virtual robot in a simple grid 2D grid world. The basis for SLAM is to gather information from a robot's sensors and motions over time, and then use information about measurements and motion to re-construct a map of the world.

The project is structured as a series of Jupyter notebooks that are designed to be completed in sequential order:

__Notebook 1__ : Setting up a moving robot with senses in a simple 2D grid world [1. Robot Moving and Sensing](1. Robot Moving and Sensing.ipynb)  

__Notebook 2__ : Introduction to the constraints `omega` and `xi` for Graph SLAM [1_Preliminaries](1_Preliminaries.ipynb)  

__Notebook 3__ : Implementation of SLAM  [3. Landmark Detection and Tracking](3. Landmark Detection and Tracking.ipynb)  



## Installation

### 1. Install Anaconda with Python

In order to run the notebook please download and install [Anaconda](https://docs.anaconda.com/anaconda/install/) with Python 3.6 on your machine. Further packages that are required to run the notebook are installed in a virtual environment using conda.


### 2. Create a Virtual Environment

In order to set up the prerequisites to run the project notebook you should create a virtual environment, e. g. using conda, Anaconda's package manager, and the following command

```
conda create -n computer-vision python=3.6
```

The virtual environment needs to be activated by

```
activate computer-vision
```

### 3. Download the project from github

You can download the project from github as a zip file to your Downloads folder from where you can unpack and move the files to your local project folder. Or you can clone from Github using the terminal window. Therefore, you need to prior install git on your local machine e. g. using

```
conda install -c anaconda git
```

When git is installed you can create your local project version. Clone the repository, and navigate to the download folder. This may take a minute or two to clone due to the included image data.

```
git clone https://github.com/AndiA76/landmark-detection-and-tracking.git
cd landmark-detection-and-tracking
```

### 4. Install requirements 

You need to install a couple of further packages, which are required by the project notebook. The packages are specified in the [requirements.txt](requirements.txt) file (incl. OpenCV for Python). You can install them using pip resp. pip3:

```
pip install -r requirements.txt
```

### 5. Run the notebooks

Now start a Jupyter notebook to run the project using following command

```
jupyter notebook
```

Navigate to your local project folder in the Jupyter notebook, open the notebooks 1...3

[1. Robot Moving and Sensing](1. Robot Moving and Sensing.ipynb)
[1_Preliminaries](1_Preliminaries.ipynb)
[3. Landmark Detection and Tracking](3. Landmark Detection and Tracking.ipynb)

and run them one after another.

