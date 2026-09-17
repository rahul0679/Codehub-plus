from fastapi import FastAPI
from app.schemas import RepoAnalyzeRequest, RepoMetadataResponse
from app.services import extract_owner_and_repo, fetch_github_metadata

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

@app.post("/api/repo/analyze", response_model=RepoMetadataResponse)
async def analyze_repo(payload: RepoAnalyzeRequest):
    owner, repo_name = extract_owner_and_repo(str(payload.repo_url))
    metadata = await fetch_github_metadata(owner, repo_name)
    return metadata