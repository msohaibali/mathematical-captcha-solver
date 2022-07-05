# mathematical-captcha-solver
This repo contains a CNN based model trained on Mathematical & logic CAPTCHA images to detect and solve the mathematical equations provided in [CAPTCHA](https://en.wikipedia.org/wiki/CAPTCHA) images.


## PROJECT STRUCTURE
```bash
.
├── .gitignore                            # List of Files/Folders to ignore while commits
├── Captcha_Model                         # Saved Captcha Model (Can be loaded directly using keras load_model function)
├── all_captcha_images                    # Dataset Folder (contains Captcha Images for Model Training and Evalation)
├── Captcha_Recognition_Training.ipynb    # Training Module (contains Jupyter Notebook integrated and built in Google Colab)
├── predictor.py                          # Prediction Module (contains, Image Loading, Scaling, Model Loading and Prediction Module) 
├── LICENSE
├── README.md
└──requirements.txt
```

## Pre-requisites to run the solution
- Python 3.6+ (3.8 recommended)
- clone this repository into your local system or any cloud instance

```git clone https://github.com/msohaibali/mathematical-captcha-solver.git```


### Install Required Packages
If you want to run the server locally, install the required packages first by
```
pip install -r requirements.txt
```

### Run Prediction Module
This Repo contains the keras model which can be loaded and right away start giving predictions on passed image.
Prediction Image path can be changed in predictor.py file. To Get Prediction Result, RUN

```python predictor.py```

## Retrain Model
If for any reason you want to retrain the model on your own data you can do so by uploading ```Captcha_Recognition_Training.ipynb``` file to [Google Colab](https://colab.research.google.com/) and then uploading dataset images folder in the Google Drive while changing these parameters,
- Image Size Dimension (25x65 in my case, can be changed to image dimensions of your dataset)
- Characters (List of Characters that are in the captcha for my case these are 012345679+-*=? [having length 14])
- Change value 5 (in my case I have 5 characters in the Input Captcha Image, Change this according to your dataset)
- Change value 14 (Total Number of Labels, that is equal to characters length)
