This is  guide you through the process of deploying a machine learning model using FastAPI and heroku, a free-tier platform. With a passion for AI-driven applications, this tutorial will cover the complete journey - from preparing the machine learning model ,setting up the FastAPI application, and deploying it on heroku, to automating the deployment process with GitHub Actions.

1.train_model.py- this file make the "iris_model.pkl" file,Load the Iris dataset from sklearn.datasets, Split the data into training and test sets and Train a RandomForestClassifier
2.main.py       - this file is fastapi application code.(main sourse code)
3.requirements.txt- is necessary libraries.
4.Procfile      - tells Heroku how to run your app.
5..github       -Workflow File

![Screenshot (171)_LI](https://github.com/user-attachments/assets/9c216f35-94d4-4afa-bd29-6aaabe4f6496)

Automating deployment with GitHub Actions allows us to continuously deploy updates to our FastAPI app on Render directly from our GitHub repository. By integrating a CI/CD (Continuous Integration/Continuous Deployment) pipeline, we ensure that every change pushed to our repository triggers an automated deployment process, streamlining our workflow and minimizing manual intervention.
