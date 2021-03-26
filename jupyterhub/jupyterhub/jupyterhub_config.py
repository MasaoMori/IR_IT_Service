import os
import sys

## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = "/lab"

## Authenticator
# from jhub_cas_authenticator.cas_auth import CASAuthenticator
c.Authenticator.admin_users = {"admin"}
c.Authenticator.allowed_users = {"ryu", "tetsuya", "masao"}
c.LocalAuthenticator.create_system_users = True

## Docker spawner
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.DockerSpawner.image = os.environ["NOTEBOOK_CONTAINER"]
c.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ["HUB_IP"]

## Proxy
# c.JupyterHub.base_url = '/hub/'

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR") or "/home/jovyan"
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}

# Other stuff
c.Spawner.cpu_limit = 4
c.Spawner.mem_limit = "10G"

## Services
c.JupyterHub.services = [
    {
        "name": "idle-culler",
        "admin": True,
        "command": [sys.executable, "-m", "jupyterhub_idle_culler", "--timeout=3600"],
    }
]
