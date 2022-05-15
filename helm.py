
def get_add_repo_command(repo_name, url):

    return f"helm repo add {repo_name} {url}"


def get_remove_repo_command(repo_name):

    return f"helm repo remove {repo_name}"


def get_install_command(release_name, chart):

    # 1. [MUST SUPPORT] By chart reference: helm install mymaria example/mariadb
    # 2. [NOT SUPPORTED] By path to a packaged chart: helm install mynginx ./nginx-1.2.3.tgz
    # 3. [NOT SUPPORTED] By path to an unpacked chart directory: helm install mynginx ./nginx
    # 4. [CAN SUPPORT, but nobody will use it] By absolute URL: helm install mynginx https://example.com/charts/nginx-1.2.3.tgz
    # 5. [SHOULD SUPPORT] By chart reference and repo url: helm install --repo https://example.com/charts/ mynginx nginx

    return f"helm install {release_name} {chart}"


def get_upgrade_command(release_name, chart):

    return f"helm upgrade {release_name} {chart}"


def get_uninstall_command(release_name):

    return f"helm uninstall {release_name}"


def get_rollback_command(release_name):

    return f"helm rollback {release_name}"