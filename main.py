from fastapi import FastAPI, HTTPException

import models
import controllers


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/repo/add")
async def add_repo(repo: models.Repo):

    if not repo.url:
        raise HTTPException(status_code=400, detail="url for repository is required")

    response = await controllers.add_repository_to_helm(repo)
    return response


@app.post("/repo/remove")
async def remove_repo(repo: models.Repo):
    
    response = await controllers.remove_repository_from_helm(repo)
    return response


@app.post("/chart/install")
async def install_chart(release: models.Release):

    if not release.chart_name:
        raise HTTPException(status_code=400, detail="chart name is required")

    response = await controllers.install_release_from_chart(release)
    return response


@app.post("/chart/upgrade")
async def upgrade_chart(release: models.Release):

    if not release.chart_name:
        raise HTTPException(status_code=400, detail="chart name is required")

    response = await controllers.upgrade_release_from_chart(release)
    return response


@app.post("/chart/uninstall")
async def uninstall_chart(release: models.Release):

    response = await controllers.uninstall_release(release)
    return response


@app.post("/chart/rollback")
async def rollback_chart(release: models.Release):

    response = await controllers.rollback_release(release)
    return response
