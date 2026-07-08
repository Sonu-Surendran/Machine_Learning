from fastapi import FastAPI
import uvicorn
import pickle

input_file = "model_1.bin"

with open(input_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = FastAPI()

@app.post("/predict")
def predict(customer: dict):
    x = dv.transform(customer)
    y_pred = model.predict(x)

    if y_pred == 1:
        return {"predict": "churn", "discount": 25}
    else:
        return {"predict": "no churn", "discount": "none"}

if __name__ == "__main__":
    uvicorn.run("load_model:app", host="127.0.0.1", port=8000, reload=True)