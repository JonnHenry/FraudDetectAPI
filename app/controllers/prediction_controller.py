from fastapi import APIRouter , HTTPException, status
from app.models.models import PredictionInput,PredictionOutput
from app.utils.utils import PrepareData, PredictionModel

router = APIRouter()
prepare_data = PrepareData()
prediction_model = PredictionModel()

@router.post('/fraud/predict',status_code=status.HTTP_200_OK,response_model=PredictionOutput)
def create_stroke(pred_input: PredictionInput):
    try:
        df_pred_input = prepare_data.transform_data_to_predict(pred_input)
        result_prediction = prediction_model.load_model_ml().predict(df_pred_input)
        return PredictionOutput(prediction=result_prediction)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocurrió un error inesperado: {str(e)}"
        )