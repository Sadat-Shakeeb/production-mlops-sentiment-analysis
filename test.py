from mlflow.tracking import MlflowClient
c = MlflowClient(tracking_uri="https://dagshub.com/Sadat-Shakeeb/production-mlops-sentiment-analysis.mlflow")
print(c.search_registered_models())
print(c.search_model_versions('name="my_model"'))