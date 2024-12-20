FROM makukha/multipython:latest

RUN --mount=type=bind,from=dattached/bootstrap,dst=/b <<EOT
apt-get update
bash /b/debian-apt-install-devtools.sh
rm -rf /var/lib/apt/lists/*
EOT

RUN <<EOT
apt-get update
apt-get install -y --no-install-recommends \
    chromium \
    nodejs \
    npm
rm -rf /var/lib/apt/lists/*
npm install -g @mermaid-js/mermaid-cli
EOT

COPY <<EOF /root/puppeteer-config.json
{
    "executablePath": "/usr/bin/chromium",
    "args": [
        "--no-sandbox"
    ]
}
EOF

COPY --from=ghcr.io/astral-sh/uv /uv /uvx /bin/
COPY .dev/requirements.*.txt /tmp/
RUN uv pip install --system -r /tmp/requirements.dev.txt -r /tmp/requirements.doc.txt

WORKDIR /project
EXPOSE 8000
