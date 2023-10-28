# Time Series ARIMA Model with MLOps on GCP using uWSGI Flask

## Business Objective

A time series is simply a series of data points ordered in time. In a time-series, time is often the independent variable, and the goal is usually to make a forecast for the future. Time series data can be helpful for many applications in day-to-day activities like:

- Tracking daily, hourly, or weekly weather data
- Monitoring changes in application performance
- Medical devices to visualize vitals in real-time

Auto-Regressive Integrated Moving Average (ARIMA) model is one of the more popular and widely used statistical methods for time-series forecasting. ARIMA is an acronym that stands for Auto-Regressive Integrated Moving Average. It is a class of statistical algorithms that captures the standard temporal dependencies unique to time-series data. The model is used to understand past data or predict future data in a series. It's used when a metric is recorded in regular intervals, from fractions of a second to daily, weekly, or monthly periods.

ARIMAX (Auto-Regressive Integrated Moving Average Exogenous) is an extension of the ARIMA model, and similarly, SARIMAX (Seasonal Auto-Regressive Integrated Moving Average with Exogenous factors) is also an updated version of the ARIMA model.

MLOps is a set of practices that aims to deploy and maintain machine learning models in production reliably and efficiently. Today, many organizations are turning towards machine learning and Artificial intelligence. AI-based applications promise to deliver new levels of competitiveness, intelligence, and automation for businesses. MLOps is a means of continuous delivery and deployment of these machine learning models. Practicing MLOps means that you advocate for automation and monitoring at all steps of ML system construction, including integration, testing, releasing, deployment, and infrastructure management.

---

## Data Description

The dataset is "Call centers" data. This data is at the month level wherein the calls are segregated at the domain level as the call center operates for various domains. There are also external regressors like the number of channels and the number of phone lines which essentially indicate the traffic prediction of the in-house analyst and the resources available. The total number of rows are 132 and the number of columns are 8:
- Month, healthcare, telecom, banking, technology, insurance, number of phonelines, and number of channels.

---

## Aim

- To build an ARIMA model on the given dataset.

- To create an end-to-end machine learning development process to design, build, and manage reproducible, testable, and evolvable machine learning models using Google Cloud Platform (GCP) for the Time Series ARIMA Project.

---

## Tech Stack

- **Language**: `Python`
- **Services**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels`, `scipy` , `GCP`, `uWSGI`, `Flask`, `Kubernetes`, `Docker`

---

## Approach

1. Import the required libraries and read the dataset
2. Perform descriptive analysis
3. Exploratory Data Analysis (EDA)
    - Data Visualization
4. Check for white noise
5. Check for Random Walk
6. Perform Stationarity tests
    - Augmented Dickey-Fuller test
    - KPSS test
7. Seasonal decomposition plot
8. Holt Winter Exponential Smoothing
    - Create and fit the model
    - Make predictions on the model
    - Plot the results
9. ARIMA model
    - Create models with varying lag values
    - Compare these models using log-likelihood and AIC values
    - Check with the LLR test
    - ACF Plots of residuals
10. ARIMAX model
    - Create a model
    - ACF plots of residuals
11. SARIMAX model
    - Create a model
    - ACF plots of residuals

#### CLOUD BUILD TRIGGER

- In your GCP console, create a new cloud build trigger.
- Point the trigger to your source repository.

#### GOOGLE KUBERNETES ENGINE (GKE)

- From the console launch a Kubernetes cluster.
- Connect to the cluster and create the following two files:
  - `deployment.yaml`
  - `service.yaml`
- Copy the code for both files from the "Kubernetes Files" folder in the cloned repository.
- Execute the following commands:
  - `kubectl apply -f deployment.yaml`
  - `kubectl apply -f service.yaml`
- Get the name of the deployment with the following command:
  - `kubectl get deployments`

#### CLOUD PUB/SUB

- Create a Pub/Sub topic with the name `cloud-build`.
- Provide a subscription for the topic, which is to trigger a cloud function.

#### CLOUD FUNCTIONS

- From Pub/Sub console launch the cloud function window.
- Provide the following Environment variables through the GUI console:
  - `PROJECT` (project name)
  - `ZONE` (Region in which the project is deployed, ex. uscentral-1)
  - `CLUSTER` (Name of the Kubernetes cluster created earlier)
  - `DEPLOYMENT` (Name of the deployment inside the Kubernetes cluster)
- Copy the program code and `requirements.txt` files for the cloud function from the `cloud-function-trigger` folder.
- Configure the Entrypoint for the cloud function as `onNewImage`.
- Deploy the function.

After successful deployment, make a commit to the source repository and the following will happen in sequence:

- Cloud Build will push a message to Pub/Sub upon successful build.
- Pub/Sub will trigger the cloud function.
- Cloud function will deploy the new image on Kubernetes.
- To test the deployment, check the logs on Kubernetes cluster using the following command:
  - `kubectl get pods`
  - `kubectl logs <pod name>`

The deployment will reflect in the logs as well as in the endpoints.

---

## Folder Structure Info

1. **Input** - Data-chillers.csv
2. **Kubernetes files** - this folder contains all the required files to trigger Kubernetes
3. **MLPipeline** - this folder contains all the functions put into different Python files
4. **Notebook** - the time series ARIMA notebook
5. **Output** - the model that is saved in the (.pkl format)
6. `__init__.py` - required empty file
7. `Dockerfile` - The Docker image
8. **Engine** - File where the MLPipeline files are called
9. `Main.py` - file to host Flask API
10. `Readme` - explains the entire approach /steps
11. `Requirements.txt` - all the required libraries
12. `Uwsgi.ini` - uWSGI configuration file

---

## Key Concepts Explored

1. Time series
2. White Noise detection
3. Random Walk detection
4. Stationarity test
5. Seasonality plot
6. Holt Winter Exponential Smoothing model
7. ARIMA model
8. ACF plots
9. Log-likelihood and AIC test
10. ARIMAX model
11. SARIMAX model
12. MLOps architecture in Google Cloud Platform (GCP)
13. Understanding of Flask and uWSGI model files
14. Understanding and building of Docker images
15. Understanding of Kubernetes architecture
16. Various components on GCP
17. Learn how to create a cloud repository in GCP
18. Learn how to clone the git repository with the source repository
19. Learn how to commit changes in the source repository
20. Cloud build component and create a trigger
21. Understand the Pub/Sub component
22. Cloud Shell editor
23. Flask deployment
24. Understanding the cloud function
25. Kubernetes deployment


---

