from app.models.models import PredictionInput
from joblib import load
from app.constants import categorical_columns, numerical_columns, features_model, PATH_ENCODER,PATH_MODEL_ML,PATH_SCALER
import pandas as pd
import os

class PredictionModel:
    def __init__(self):
        self.encoder=None
        self.scaler=None
        self.model=None

    def load_encoder(self):
        try:
            if self.encoder is None:
                self.encoder = load(os.path.join(os.path.dirname(os.path.abspath(__file__)), PATH_ENCODER))
            return self.encoder
        except FileNotFoundError:
            print("Error: No se encontró el archivo del encoder.")
            return None
        
    def load_scaler(self):
        try:
            if self.scaler is None:
                self.scaler=load(os.path.join(os.path.dirname(os.path.abspath(__file__)), PATH_SCALER)) 
            return self.scaler
        except FileNotFoundError:
            print("Error: No se encontró el archivo del scaler.")
            return None     

    def load_model_ml(self):
        try:
            if self.model is None:
                self.model=load(os.path.join(os.path.dirname(os.path.abspath(__file__)), PATH_MODEL_ML))
            return self.model
        except FileNotFoundError:
            print("Error: No se encontró el archivo del modelo.")
            return None   


class PrepareData:
    def __init__(self):
        self.prediction_model=PredictionModel()

    def transform_data_to_predict(self,prediction_input: PredictionInput) -> pd.DataFrame:
        df_input_data = prediction_input.to_dataframe()
        encoder = self.prediction_model.load_encoder()
        encoded_array = encoder.transform(df_input_data[categorical_columns])
        df_encoded = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(categorical_columns))
        columns_enconded_list = df_encoded.columns.to_list()
        df_input_data[columns_enconded_list] = df_encoded[columns_enconded_list]
        scaler = self.prediction_model.load_scaler()
        df_input_data[numerical_columns] = scaler.transform(df_input_data[numerical_columns])
        df_input_data.drop(columns=categorical_columns, inplace=True)
        return df_input_data[features_model]
 
