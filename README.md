# Coccidiosis Disease Detections- A Deep Learning Approach

[![Python 3.10.12](https://img.shields.io/badge/python-3.10.12-blue.svg)](https://www.python.org/downloads/release/python-31012/)
![Static Badge](https://img.shields.io/badge/Tensorflow-orange.svg)


This project aims to detect the presence of coccidiosis, a common parasitic disease in Poultry(Chickens), using deep learning techniques. The app utilizes a transfer learning approach with the VGG16 architecture to classify input images as either indicative of coccidiosis or not.

## Problem Statement

Coccidiosis is a significant concern in poultry farms as it affects the health and productivity of various species. Early detection of coccidiosis is crucial for effective treatment and prevention of its spread. Traditional methods of diagnosis can be time-consuming and often require expert intervention. This project addresses the need for a rapid and automated coccidiosis detection system by leveraging deep learning techniques.

## Key Features

- **Image Classification:** The core functionality of this web app is to classify input images of chicken feaces as either positive for coccidiosis or negative. This classification is based on a trained VGG16 model.

- **User-Friendly Interface:** The web app provides an intuitive user interface where users can upload images for analysis. The results, indicating whether coccidiosis is detected or not, are displayed in a user-friendly manner.

- **Quick Analysis:** By utilizing pre-trained weights from VGG16, the app enables quick analysis of input images, providing users with timely information for decision-making.

## Model and Transfer Learning

The project employs transfer learning with the VGG16 architecture. Transfer learning involves using a pre-trained model (VGG16 in this case). The last layers of the pre-trained model are fine-tuned to suit the specific classification task of coccidiosis detection.

## Dataset

For this project, a well-labeled dataset of coccidiosis-positive and coccidiosis-negative images was used for training and validation. The dataset was preprocessed to ensure consistency and appropriate formatting for training the model.

https://www.kaggle.com/datasets/allandclive/chicken-disease-1


## **Tools & Techniques**

*   `Code versioning` using Git
*   `Modular coding` with separate files for data ingestion, training, evaluation, Configuration, constants, secret keys, artifacts etc
*   `DVC Trainnig Pipeline`
*   `CI / CD Pipeline` using GitHub Actions
*   `Docker` for creating container
*   Custome `logger`
*   Custom `Exception Handler`
*   `Package building` using setuptools
*   `Deplyment` tested on **Auzre**, and on **AWS EC2 instance CI/CD** using Github Action Runner


## **Deployments**

*   Azure
*   AWS EC2

## Installation and Usage

To use the Coccidiosis Detection Web App, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/junaid-o/DL-Coccidiosis_Disease_Detection.git
   cd DL-Coccidiosis_Disease_Detection
   ```

2. **Create a conda environment after opening the repository**

   ```bash
   conda create --prefix env python=3.10.12 -y
   ```

   ```bash
   conda activate cnncls
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App:**

   ```bash
   python app.py
   ```

5. **Access the App:**
   Open your web browser and go to `http://localhost:8000` to access the web app.

6. **Upload Images:**
   Upload the images you want to analyze using the provided interface.

7. **View Results:**
   The app will display the classification results along with an indication of whether coccidiosis is detected or not.

## Model Training

   ```bash
   python main.py
   ```
   or

   ```bash
   dvc repro
   ```
   
   ```
   http://localhost:8000/train
   ```
   
## DVC Commands

1. `dvc init` to initialize the dvc in the project dir
2. `dvc repro` to trigger the training pipeline
3. `dvc dag` to visualize the pipline architechture


# Docker

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Docker images can be used to create containers, which are isolated environments that run your application. This is useful because it ensures that your application runs in the same environment regardless of where it is being deployed.

To build and run this project using Docker, follow these steps:

1.  Install Docker on your machine if you haven't already.
2.  Open a terminal window and navigate to the project root directory.
3.  Build the Docker image by running the following command:

    ```
    docker build -t <image-name>:<version> <location-of-docker-file for curren directory just add dot (.)>

    ```
    or

    ```
    docker build -t <image-name>:<version> .
    
    ```

4.  To Check List of Docker Images
    ```
    docker images
    ```    

5.  Start a container using the following command, replacing <image-name> and <version> with the values you used in step 3:

    ```
    docker run -p <host-port>:<container-port> <image-name>:<version>

    ```

    or

    ```
    docker run -p 5000:5000 -e PORT=5000 <Image-ID>
    ```

6.  Open a web browser and go to `http://localhost:<host-port>` to see the application running.

7.  Check Running Containers in docker

    ```
    docker ps
    ```

8.  Stop Docker Container

    ```
    docker stop <container_id>
    ```    


# AWS-CICD-Deployment-with-Github-Actions

1. Login to AWS console

2. Create IAM user for deployment

	**with specific access**

    
	1. *EC2 access : It is virtual machine*

	2. *ECR: Elastic Container registry to save your docker image in aws*

	**_Description:_** About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	**_Policy:_**

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
3. Create ECR repo to store/save docker image

    - Save the `URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken`

4. Create EC2 machine (Ubuntu) 

5. Open EC2 and Install docker in EC2 Machine:

    **_optinal_**

    ```bash
    sudo apt-get update -y
    ```
	
	```bash
	sudo apt-get upgrade
	```	

	**_required_**

	```bash
	curl -fsSL https://get.docker.com -o get-docker.sh
	```
	```bash
	sudo sh get-docker.sh
	```

	```bash
	sudo usermod -aG docker ubuntu
	```

	```bash
	newgrp docker
	```
	
6. Configure EC2 as self-hosted runner:
   
   `setting>actions>runner>new self hosted runner> choose os> then run command one by one`


7. Setup github secrets:

    `AWS_ACCESS_KEY_ID`

    `AWS_SECRET_ACCESS_KEY`=

    `AWS_REGION = us-east-1`

    `AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com`

    `ECR_REPOSITORY_NAME = simple-app`

# AZURE-CICD-Deployment-with-Github-Actions

**Description**

- Open `Container Registery` and create a container registry with name `chickenapp`.
- Go to Resource > Access Keys > Copy login Server and Password
- Open WebApp For Containers. Here Docker image is needed.
- Build the docker image on your local terminal
- loging to azure docke via your local terminal as mentioned and push the docker image
- Complete the remaining steps on azure.
- Go to Deployment Center and adjust settings
- YAML file will be auomaticallypushed to github workflows folder in github repo

**Save pass:**

`s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6`

**Run from terminal:**

  `
  docker build -t <login server>/<Project Image Name>:latest .
  `

  ```bash
  docker build -t chickenapp.azurecr.io/chicken:latest .
  ```

  ```bash
  docker login chickenapp.azurecr.io
  ```
  
  ```bash
  docker push chickenapp.azurecr.io/chicken:latest
  ```


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 

# Other Instructions: Workflows for code writing

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

# Project Structure

```
DL-Coccidiosis_Disease_Detection
├─ .dvc
├─ .dvcignore
├─ .git
├─ .github
│  └─ workflows
│     ├─ .gitkeep
│     ├─ main.yaml
│     └─ main_chickenapp.yml
├─ .gitignore
├─ app.py
├─ config
│  └─ config.yaml
├─ Dockerfile
├─ dvc.lock
├─ dvc.yaml
├─ LICENSE
├─ logs
├─ main.py
├─ params.yaml
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ research
│  ├─ 01_data_ingestion.ipynb
│  ├─ 02_prepare_base_model.ipynb
│  ├─ 03_prepare_callbacks.ipynb
│  ├─ 04_training.ipynb
│  ├─ 05_model_evaluation.ipynb
│  └─ trials.ipynb
├─ scores.json
├─ setup.py
├─ src
│  └─ CoccidiosisDetector
│     ├─ components
│     │  ├─ data_ingestion.py
│     │  ├─ evaluation.py
│     │  ├─ prepare_base_model.py
│     │  ├─ prepare_callbacks.py
│     │  ├─ training.py
│     │  └─ __init__.py
│     ├─ config
│     │  ├─ configuration.py
│     │  └─ __init__.py
│     ├─ constants
│     │  └─ __init__.py
│     ├─ entity
│     │  ├─ config_entity.py
│     │  └─ __init__.py
│     ├─ exception
│     │  └─ __init__.py
│     ├─ logger
│     │  └─ __init__.py
│     ├─ pipeline
│     │  ├─ predict.py
│     │  ├─ stage_01_data_ingestion.py
│     │  ├─ stage_02_prepare_base_model.py
│     │  ├─ stage_03_training.py
│     │  ├─ stage_04_evaluation.py
│     │  └─ __init__.py
│     ├─ utils
│     │  ├─ utils.py
│     │  └─ __init__.py
│     └─ __init__.py
├─ template.py
└─ templates
   └─ index.html

```
