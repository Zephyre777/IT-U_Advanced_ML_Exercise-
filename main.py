import kagglehub
import os
from MLP import mlp
# Download latest version

FILE_NAME = 'Clean_Dataset.csv'

if __name__ == "__main__":
    path = kagglehub.dataset_download("shubhambathwal/flight-price-prediction", output_dir='data')
    mlp = mlp(os.path.join(str(os.path.abspath(os.path.curdir)), path, FILE_NAME))