from pydantic import BaseModel, HttpUrl
from typing import Optional

# User jab repository analyze karne bhejega
class RepoAnalyzeRequest(BaseModel):
    repo_url: HttpUrl

# GitHub se laayi gayi details ka format
class RepoMetadataResponse(BaseModel):
    owner: str
    name: str
    description: Optional[str] = None
    stars: int
    forks: int
    open_issues: int
    default_branch: str
    language: Optional[str] = None