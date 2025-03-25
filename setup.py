from setuptools import setup, find_packages

setup(
    name="fraud_detect_ml",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "joblib",
        "pydantic",
        "pandas",
        "scikit-learn"
    ],
)