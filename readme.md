# ARIMA Time Series Model with MLOps on GCP using uWSGI Flask

## Business Objective

A time series is a series of data points ordered in time, where time is often the independent variable. Time series data is valuable for various applications, such as:

- Tracking weather data at different intervals
- Monitoring application performance changes
- Visualizing real-time vital statistics in medical devices

The Auto-Regressive Integrated Moving Average (ARIMA) model is a widely used statistical method for time-series forecasting. ARIMA stands for Auto-Regressive Integrated Moving Average and is used to analyze and predict time-series data. It is suitable for metrics recorded at regular intervals, from fractions of a second to daily, weekly, or monthly periods. ARIMAX and SARIMAX are extensions of the ARIMA model.

MLOps is a set of practices that ensure reliable and efficient deployment and maintenance of machine learning models in production. Many organizations are adopting machine learning and artificial intelligence to gain a competitive edge, automate processes, and make data-driven decisions. MLOps advocates for automation and monitoring at all stages of machine learning system development, including integration, testing, releasing, deployment, and infrastructure management.

---

## Data Description

The dataset contains "Call centers" data, recorded at the monthly level. The dataset categorizes calls by domain as the call center operates for various domains. It also includes external regressors like the number of phone lines and channels, which indicate traffic prediction and resource availability. The dataset has 132 rows and 8 columns:

- Month, healthcare, telecom, banking, technology, insurance, number of phone lines, and number of channels.

---

## Aim

- Build an ARIMA model using the provided dataset.
- Create an end-to-end machine learning development process on Google Cloud Platform (GCP) to design, build, and manage reproducible, testable, and evolvable machine learning models.

---

## Tech Stack

- **Language**: Python
- **Libraries**: pandas, numpy, matplotlib, seaborn, statsmodels, scipy
- **Cloud Services**: Google Cloud Platform (GCP)
- **Web Technologies**: uWSGI, Flask
- **Containerization**: Docker
- **Container Orchestration**: Kubernetes

---

## Approach

1. Import the necessary libraries and load the dataset.
2. Perform descriptive analysis.
3. Explore the data through Exploratory Data Analysis (EDA) and data visualization.
4. Check for white noise and random walk in the time series.
5. Conduct stationarity tests, including Augmented Dickey-Fuller and KPSS tests.
6. Create a seasonal decomposition plot.
7. Apply Holt Winter Exponential Smoothing.
8. Develop an ARIMA model:
    - Experiment with different lag values.
    - Compare models using log-likelihood and AIC values.
    - Conduct the LLR test.
    - Analyze ACF plots of residuals.
9. Implement an ARIMAX model.
    - Analyze ACF plots of residuals.
10. Explore SARIMAX modeling.
    - Analyze ACF plots of residuals.

### Cloud Build Trigger

- Create a new Cloud Build trigger in the GCP console.
- Link the trigger to your source repository.

### Google Kubernetes Engine (GKE)

- Launch a Kubernetes cluster from the console.
- Connect to the cluster and create the following two files:
  - `deployment.yaml`
  - `service.yaml`
- Copy the code from the "Kubernetes Files" folder in the cloned repository.
- Execute the following commands:
  - `kubectl apply -f deployment.yaml`
  - `kubectl apply -f service.yaml`
- Obtain the deployment name with the command: `kubectl get deployments`

### Cloud Pub/Sub

- Create a Pub/Sub topic named `cloud-build`.
- Set up a subscription to trigger a cloud function.

### Cloud Functions

- Launch the cloud function from the Pub/Sub console.
- Configure environment variables through the GUI console, including `PROJECT`, `ZONE`, `CLUSTER`, and `DEPLOYMENT`.
- Copy the code and `requirements.txt` files for the cloud function from the `cloud-function-trigger` folder.
- Set the Entrypoint for the cloud function as `onNewImage`.
- Deploy the function.

After successful deployment, commit changes to the source repository, triggering the following sequence:

- Cloud Build sends a message to Pub/Sub upon successful build.
- Pub/Sub triggers the cloud function.
- The cloud function deploys the new image on Kubernetes.
- To test the deployment, check the logs on the Kubernetes cluster using the following commands:
  - `kubectl get pods`
  - `kubectl logs <pod name>`

The deployment status is reflected in the logs and endpoints.

---

## Cpde Structure

1. **Input**: Contains the "Data-chillers.csv" dataset.
2. **Kubernetes files**: Includes files to trigger Kubernetes.
3. **MLPipeline**: Contains functions in different Python files.
4. **Notebook**: The time series ARIMA notebook.
5. **Output**: Stores the model in (.pkl) format.
6. `__init__.py`: An empty required file.
7. `Dockerfile`: The Docker image configuration.
8. **Engine**: Where the MLPipeline files are called.
9. `Main.py`: Hosts the Flask API.
10. `Readme`: Provides an explanation of the entire approach and steps.
11. `Requirements.txt`: Lists all required libraries.
12. `Uwsgi.ini`: uWSGI configuration file.

---


