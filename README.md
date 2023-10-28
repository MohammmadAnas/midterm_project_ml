# midterm_project_ml
## Predict Health Insurance Owners' who will be interested in Vehicle Insurance

### Problem Statement : The data we are trying to work on is of an insurance company's customer and we are trying to build a model to predict whether the policyholders (customers) from past year will also be interested in Vehicle insurance provided by the company.

### Data

Data is available in the data folder. The train.csv file contains the training set.

Dataset reference: https://www.kaggle.com/competitions/spaceship-titanic/data

Note: In order to download data from kaggle, you need to create an account on kaggle.com and download the kaggle.json file from your account. Then, you need to put this file in the ~/.kaggle folder. Then execute the ml/download_data.py script to download the data under the data folder.

#### Run with Docker

You can run the project with Docker. To do so, you need to have Docker installed on your machine. Then, you need to build the image with the following command:

```bash
sudo docker build -t insurance_pred .
```

Then, you can run the project with the following command:

```bash
python predict-test.py
```

Sample data which I used in predict-test.py

customer = {"Gender": 2.0,
 "Age": 35.0,
 "Driving_License": 1.0,
 "Region_Code": 47.0,
 "Previously_Insured": 1.0,
 "Vehicle_Age": 1.0,
 "Vehicle_Damage": 1.0,
 "Annual_Premium": 15000.0,
 "Policy_Sales_Channel": 151.0,
 "Vintage": 148.0}
 
 If you want to use other data you can find it in at "insurance_pred/test.csv" file. Format it in the similar form above before using it. 


 Sample output of prediction :

![output_midterm](https://github.com/MohammmadAnas/midterm_project_ml/assets/127856326/ed5d719a-5f3f-4e99-b943-ec48b460111b)





 
