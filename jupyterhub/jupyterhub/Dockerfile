FROM jupyterhub/jupyterhub:1.3.0

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

RUN pip install \
    dockerspawner \
    jupyterhub-idle-culler
RUN useradd -ms /bin/bash admin
RUN echo 'admin:password' | chpasswd
RUN useradd -ms /bin/bash ryu
RUN echo 'ryu:password' | chpasswd
RUN useradd -ms /bin/bash bob
RUN echo 'bob:password' | chpasswd
RUN useradd -ms /bin/bash alice
RUN echo 'alice:password' | chpasswd

CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]
