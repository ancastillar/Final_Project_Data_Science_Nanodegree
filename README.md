# Default analysis: Credit cards

The objective of this project is to predict the probability of default on a given obligation, in this case, credit cards. This will allow the generation of strategies that minimize the risk of deterioration of the client's financial health. Additionally, to facilitate the development of collection strategies, it is proposed to use clustering algorithms to find homogeneous segments within the population and thus provide differential treatment to each customer.

## Link for web app: https://defaultappnataliacastilla.herokuapp.com/
![plot](./imgs/web_app.PNG)
![plot](./imgs/web_app1.PNG)


## About this repository
In this repository you will find everything you need to reproduce my work

* notebooks: You will find the code to reproduce everything.
* models: You will find all the models made
* imgs: You will find all the images made in the exploration, preprocessing and clustering.
* data: Source of data used: https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients

* Web app: Contains the you to deploy the web application.


## Models and results

To select the model, for each cluster, we trained 4 different binary classification models: SVM, XGB, KNN, NB (each of a different nature). To guarantee the performance of each one we used K-fold in which we partition the data 10 times. In this way we obtain a list of scores from which we can obtain some basic statistics: standard deviation, mean, average; The metrics used for the evaluation in each Fold were: AUC, F1-Score and Acuraccy. To balance the data we used SMOTE-TOMEK which creates an artificial sample according to the nearest neighbors of each point.

The best performing model was Xgboost for both cases, a summary of the metrics obtained is shown below.
**Model 1: Cluster 1

![plot](./imgs/resultados_modelo1_test.PNG)

**Model 2: Cluster 2**
![plot](./imgs/resultados_modelo2_test.PNG)


## Conclusions

* We use a clustering algorithm to find the best segmentation within the population. We find customers with relatively larger quotas who have better payment habits and the standard deviation in payments is higher than the other segment.
* Strategies should be developed to reduce the non-compliance rate in small quotas $(5000,50000].
* The age range with the highest rate of noncompliance (44.1%) was found to be (71-91] years.
* An AUC of 0.81 was determined for model 2 and 0.78 for model 1.
* 

## Prerequisites


* python3
* python packages in the requirements.txt file

Instala los paquetes con:

* pip install -r requirements.txt

