# check https://fastapi.tiangolo.com/tutorial/testing/

import helm
import shell

async def main():

    repo_name = "bitnami"
    repo_url = "https://charts.bitnami.com/bitnami"
    release_name = "redis-local"
    chart = "bitnami/redis"

    add_cmd = helm.get_add_repo_command(repo_name, repo_url)
    remove_cmd = helm.get_remove_repo_command(repo_name)
    install_cmd = helm.get_install_command(release_name, chart)
    upgrade_cmd = helm.get_upgrade_command(release_name, chart)
    uninstall_cmd = helm.get_uninstall_command(release_name)
    rollback_cmd = helm.get_rollback_command(release_name)

    test_command_executions = [
        add_cmd,
        install_cmd,
        upgrade_cmd,
        rollback_cmd,
        uninstall_cmd,
        remove_cmd,
    ]

    for cmd in test_command_executions:
        await shell.run(cmd)
