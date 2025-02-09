from fastapi import FastAPI, File, UploadFile
import pandas as pd
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

tags = [
    {
        'name':'Maths',
        'description' : 'Operations related to Math'
    },
        {
        'name':'Models',
        'description' : 'Operations related to Models'
    }
]

app = FastAPI(
    title="My FastApi App",
              description="heu ouai carrément",
              version="0.0.1 beta",
              openapi_tags=tags
              )

@app.get("/", tags=['Models'])
def default_root():
    return "Hello FastApi"

@app.get("/square", tags=['Maths'])
def square_root(n:int = 1) -> str:
    return str(n**2)

from pydantic import BaseModel

class Data(BaseModel):
    name:str = "Yohan"
    city:str = "Lyon"
    
class DataModel(BaseModel):
    
    Gender: str = "Male"
    Age: int = 22
    Graduated: str = "No"
    Profession: str = "Healthcare"
    Work_Experience: float = 1.0
    Spending_Score: str = "Low"
    Family_Size: float = 4.0
    Segmentation: str = "D"

@app.post("/formulaire", tags=['Maths'])
def formulaire(data:Data) -> str:
    return f"Hello {data.name} from {data.city}"

@app.post("/upload", tags=['Maths'])
def upload_file(file:UploadFile=File(...)):
    return file.filename

@app.post("/predict", tags=['Models'])
def model_endpoint(data:DataModel):
    df = pd.DataFrame([dict(data)])
    result = model.predict(df)
    return int(result[0])


@app.post("/predict_file", tags=['Maths'])
def predict_file(file:UploadFile=File(...)):
    df = pd.read_csv(file.file)
    df = df.drop(["ID", "Var_1"], axis=1).dropna()
    if 'Gender' not in df.columns or 'Graduated' not in df.columns:
        return False
    else :
        X = df.drop(["Ever_Married"], axis=1)
    
    return [int(i) for i in model.predict(X)]

@app.get("/test_deploys", tags=['Models'])
def model_endpoint():
    return int(3)

