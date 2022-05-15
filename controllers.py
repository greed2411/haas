from dataclasses import asdict

import helm
import shell
import models


async def add_repository_to_helm(repo: models.Repo):

    cmd = helm.get_add_repo_command(repo.name, repo.url)
    print(f"adding helm repository for {repo.name} @ {repo.url}")
    ros: shell.RunOnShell = await shell.run(cmd)

    response = asdict(ros)
    
    if ros.return_code == 0:
        response["status"] = "success"
        response["repo_name"] = repo.name
    else:
        response["status"] = "failure"
    
    return response



async def remove_repository_from_helm(repo: models.Repo):

    cmd = helm.get_remove_repo_command(repo.name)
    print(f"removing {repo.name} helm repository")
    ros: shell.RunOnShell = await shell.run(cmd)

    response = asdict(ros)

    if ros.return_code == 0:
        response["status"] = "success"
        response["repo_name"] = repo.name
    else:
        response["status"] = "failure"
    
    return response



async def install_release_from_chart(release: models.Release):

    cmd = helm.get_install_command(release.name, release.chart_name)
    print(f"installing release {release.name} for chart: {release.chart_name}")
    ros: shell.RunOnShell = await shell.run(cmd)

    response = asdict(ros)

    if ros.return_code == 0:
        response["status"] = "success"
        response["release_name"] = release.name
        response["chart_name"] = release.chart_name
    else:
        response["status"] = "failure"
    
    return response


async def upgrade_release_from_chart(release: models.Release):

    cmd = helm.get_upgrade_command(release.name, release.chart_name)
    print(f"upgrading release {release.name} for chart: {release.chart_name}")
    ros: shell.RunOnShell = await shell.run(cmd)

    response = asdict(ros)

    if ros.return_code == 0:
        response["status"] = "success"
        response["release_name"] = release.name
        response["chart_name"] = release.chart_name
    else:
        response["status"] = "failure"
    
    return response


async def uninstall_release(release: models.Release):

    cmd = helm.get_uninstall_command(release.name)
    print(f"uninstalling release {release.name}")
    ros: shell.RunOnShell = await shell.run(cmd)

    response = asdict(ros)

    if ros.return_code == 0:
        response["status"] = "success"
        response["release_name"] = release.name
    else:
        response["status"] = "failure"
    
    return response


async def rollback_release(release: models.Release):

    cmd = helm.get_rollback_command(release.name)
    print(f"rolling back release {release.name}")
    ros: shell.RunOnShell = await shell.run(cmd)

    response = asdict(ros)

    if ros.return_code == 0:
        response["status"] = "success"
        response["release_name"] = release.name
    else:
        response["status"] = "failure"
    
    return response
