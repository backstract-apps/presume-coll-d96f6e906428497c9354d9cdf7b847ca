from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - presume-coll-d96f6e906428497c9354d9cdf7b847ca',debug=False,docs_url='/bold-dev-be7000749c3d11efb2930242c0a8b00333/docs',openapi_url='/bold-dev-be7000749c3d11efb2930242c0a8b00333/openapi.json')

app.include_router(router, prefix='/bold-dev-be7000749c3d11efb2930242c0a8b00333/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()