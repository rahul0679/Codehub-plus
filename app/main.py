from fastapi import FastAPI

# App ka metadata jo Swagger docs me dikhega
app = FastAPI(
    title="Codehub+ API",
    description="AI-powered developer productivity & code intelligence platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "project": "Codehub+",
        "status": "online",
        "message": "Welcome to Codehub+ Engine"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}