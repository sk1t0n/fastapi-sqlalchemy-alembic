from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello'}


if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, debug=True)
