#!/bin/bash

# Update the system
apt update && apt upgrade -y 

# Termina a nano, il resto è custom
apt install -y --no-install-recommends \
	make \
	build-essential \
	libssl-dev \
	zlib1g-dev \
	libbz2-dev \
	libreadline-dev \
	libsqlite3-dev \
	curl \
	llvm \
	libncursesw5-dev \
	xz-utils \
	tk-dev \
	libxml2-dev \
	libxmlsec1-dev \
	libffi-dev \
	liblzma-dev \
	git \
	nano \
	vim \
	wget 

# Altro custom:

# uv
curl -LsSf https://astral.sh/uv/install.sh | sh