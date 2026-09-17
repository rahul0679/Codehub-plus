import httpx
from urllib.parse import urlparse
from fastapi import HTTPException

def extract_owner_and_repo(url: str):
    """
    URL se owner aur repo name extract karta hai.
    Example: 'https://github.com/fastapi/fastapi' -> ('fastapi', 'fastapi')
    """
    parsed = urlparse(str(url))
    parts = parsed.path.strip("/").split("/")
    if len(parts) < 2:
        raise HTTPException(
            status_code=400, 
            detail="Invalid GitHub URL. Format hona chahiye: https://github.com/owner/repo"
        )
    return parts[0], parts[1]

async def fetch_github_metadata(owner: str, repo: str) -> dict:
    """
    GitHub Public API se repository ka metadata fetch karta hai.
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Codehub-Plus-Engine"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url, headers=headers)

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="GitHub repository nahi mili. Check karo URL public hai ya nahi.")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="GitHub API call fail ho gayi.")

    data = response.json()
    
    return {
        "owner": data.get("owner", {}).get("login", owner),
        "name": data.get("name", repo),
        "description": data.get("description"),
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "open_issues": data.get("open_issues_count", 0),
        "default_branch": data.get("default_branch", "main"),
        "language": data.get("language")
    }