FROM python:3.13-bookworm AS base
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    --mount=type=bind,from=dattached/bootstrap,dst=/b \
<<EOT
apt-get update
bash /b/debian-apt-install-devtools.sh
apt-get install -y build-essential gdb lcov pkg-config \
      libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
      libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
      lzma lzma-dev tk-dev uuid-dev zlib1g-dev libmpdec-dev
curl https://pyenv.run | sh
ln -s /root/.pyenv/bin/pyenv /usr/local/bin
pyenv update
rm -rf /tmp/* /var/tmp/*
EOT

FROM base AS py27
RUN pyenv install 2.7

FROM base AS py35
RUN pyenv install 3.5

FROM base AS py36
RUN pyenv install 3.6

FROM base AS py37
RUN pyenv install 3.7

FROM base AS py38
RUN pyenv install 3.8

FROM base AS py39
RUN pyenv install 3.9

FROM base AS py310
RUN pyenv install 3.10

FROM base AS py311
RUN pyenv install 3.11

FROM base AS py312
RUN pyenv install 3.12

FROM base AS py314
RUN pyenv install 3.14.0a1


FROM base AS dev
RUN --mount=type=bind,from=py27,src=/root/.pyenv,dst=/tmp/py27 \
    --mount=type=bind,from=py35,src=/root/.pyenv,dst=/tmp/py35 \
    --mount=type=bind,from=py36,src=/root/.pyenv,dst=/tmp/py36 \
    --mount=type=bind,from=py37,src=/root/.pyenv,dst=/tmp/py37 \
    --mount=type=bind,from=py38,src=/root/.pyenv,dst=/tmp/py38 \
    --mount=type=bind,from=py39,src=/root/.pyenv,dst=/tmp/py39 \
    --mount=type=bind,from=py310,src=/root/.pyenv,dst=/tmp/py310 \
    --mount=type=bind,from=py311,src=/root/.pyenv,dst=/tmp/py311 \
    --mount=type=bind,from=py312,src=/root/.pyenv,dst=/tmp/py312 \
    --mount=type=bind,from=py314,src=/root/.pyenv,dst=/tmp/py314 \
<<EOT
mkdir -p /root/.pyenv/versions
cp -a /tmp/py*/versions/* /root/.pyenv/versions
pyenv install --skip-existing 2.7 3.5 3.6 3.7 3.8 3.9 3.10 3.11 3.12 3.14.0a1
EOT
COPY .dev/requirements.*.txt /tmp/
RUN --mount=type=cache,dst=/root/.cache/pip \
    --mount=type=cache,dst=/root/.cache/uv \
<<EOT
pip install uv
uv pip install --system -r /tmp/requirements.dev.txt -r /tmp/requirements.doc.txt
EOT
ENV VIRTUALENV_DISCOVERY=pyenv
WORKDIR /project
EXPOSE 8000
