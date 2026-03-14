import os
import mlflow


def promote_model():

    dagshub_token = os.getenv("CAPSTONE_TEST")
    if not dagshub_token:
        raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
    os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

    dagshub_url = "https://dagshub.com"
    repo_owner = "Sadat-Shakeeb"
    repo_name = "production-mlops-sentiment-analysis"

    mlflow.set_tracking_uri(f"{dagshub_url}/{repo_owner}/{repo_name}.mlflow")

    client = mlflow.MlflowClient()
    model_name = "my_model"

    # Get latest model version
    versions = client.search_model_versions(f"name='{model_name}'")
    latest_version = max(int(v.version) for v in versions)

    # Assign production alias
    client.set_registered_model_alias(
        name=model_name,
        alias="champion",
        version=latest_version
    )

    print(f"Model version {latest_version} promoted as 'champion'")


if __name__ == "__main__":
    promote_model()