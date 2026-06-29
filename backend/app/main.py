from fastapi import FastAPI

app = FastAPI(
    title="CareCompanion API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "CareCompanion Backend Running 🚀"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
