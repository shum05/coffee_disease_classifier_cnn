# coffee_disease_classifier_cnn (Hemileia vastatrix)

## Development and Implementation Procedures

Update config.yaml
	--> Update secrets.yaml
 		--> Update params.yaml
   			--> Update the entity
      				--> Update the configuration manager in src config
	  				--> Update the components
       						--> Update the pipeline
	     						--> Update the main.py


### Dataset URL (for images):
[Click here to download data](https://github.com/shum05/Imgs_coffee_disease_DL/raw/main/imgs_coffee.zip)

## Youtube Playlist of this project implementation:
[Click here](https://www.youtube.com/playlist?list=PLs_a5ZoT8LiSNMbw0iZoaJk8kh-MV37Vx_)

# How to run this project on your machine
	Clone the ff repository

```bash
https://github.com/shum05/coffee_disease_classifier_cnn
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.7 -y
```
 ### -And  activate it
```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

```bash
open up you local host and port
```

```bash
Author: Shu Tef
	Data/Analyst/Data Scientist/Data Eng'r
Email: tshumetie5@gmail.com
Linkedln: www.linkedin.com/in/shumetie-a-tefera527
website: https://s3shumetie23.com/
```
# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 493556374360.dkr.ecr.us-east-1.amazonaws.com/coffeeleafrust
	
                    
	
## 4. Create EC2 machine (Ubuntu) 
   - t2 large
## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	# check if docker is installed correctly
	    # docker --version
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID= ??????xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx???????

    AWS_SECRET_ACCESS_KEY= ??????????xxxxxxxxxxxxxxxxxxxxxx?????

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 493556374360.dkr.ecr.us-east-1.amazonaws.com

    ECR_REPOSITORY_NAME = coffee-app
