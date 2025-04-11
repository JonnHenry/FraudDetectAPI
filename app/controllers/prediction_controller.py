from fastapi import APIRouter , HTTPException, status
from app.models.models import PredictionInput,PredictionOutput
from app.utils.utils import PrepareData, PredictionModel
from fastapi.responses import RedirectResponse

router = APIRouter()
prepare_data = PrepareData()
prediction_model = PredictionModel()

@router.post('/fraud/predict',status_code=status.HTTP_200_OK,response_model=PredictionOutput)
def predict(pred_input: PredictionInput):
    try:
        df_pred_input = prepare_data.transform_data_to_predict(pred_input)
        probabilities  = prediction_model.load_model_ml().predict_proba(df_pred_input)
        predicted_class = int(probabilities[0][1] >= 0.5)
        fraud_probability = float(probabilities[0][1])

        return PredictionOutput(
            prediction=predicted_class,
            probability=fraud_probability  # <-- nuevo campo
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocurrió un error inesperado: {str(e)}"
        )
    

@router.get("/",include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")