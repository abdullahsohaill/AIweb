# Pix2Pix Video
**URL:** https://huggingface.co/spaces/fffiloni/Pix2Pix-Video
**Page Title:** Pix2Pix Video - a Hugging Face Space by fffiloni
--------------------


## build error

## Job failed with exit code: 1. Reason: cache miss: [root 2/2] RUN apt-get update && apt-get install -y fakeroot &&     mv /usr/bin/apt-get /usr/bin/.apt-get &&     echo '#!/usr/bin/env sh\nfakeroot /usr/bin/.apt-get $@' > /usr/bin/apt-get &&     chmod +x /usr/bin/apt-get && 	rm -rf /var/lib/apt/lists/* && 	useradd -m -u 1000 user
cache miss: [run 2/2] COPY --from=pipfreeze --link --chown=1000 /tmp/freeze.txt /tmp/freeze.txt
cache miss: [base 9/9] RUN pip install --no-cache-dir 	gradio[oauth,mcp]==5.45.0 	"uvicorn>=0.14.0" 	spaces
cache miss: [base 5/9] RUN pyenv install 3.10 && 	pyenv global 3.10 && 	pyenv rehash
cache miss: [run 2/2] LINK COPY --from=pipfreeze --link --chown=1000 /tmp/freeze.txt /tmp/freeze.txt
cache miss: [base 8/9] RUN --mount=target=/tmp/requirements.txt,source=requirements.txt     pip install --no-cache-dir -r /tmp/requirements.txt
cache miss: [run 1/2] LINK COPY --link --chown=1000 ./ /home/user/app
cache miss: [run 1/2] COPY --link --chown=1000 ./ /home/user/app
cache miss: [base 7/9] RUN 	apt-get update && 	apt-get install -y curl && 	curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && 	apt-get install -y nodejs && 	rm -rf /var/lib/apt/lists/* && apt-get clean
cache miss: [base 2/9] WORKDIR /home/user/app
cache miss: [base 3/9] RUN apt-get update && apt-get install -y 	git rsync 	make build-essential libssl-dev zlib1g-dev 	libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm 	libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git-lfs  	ffmpeg libsm6 libxext6 cmake libgl1 	&& rm -rf /var/lib/apt/lists/* 	&& git lfs install
cache miss: [base 1/9] COPY --chown=1000:1000 --from=root / /
cache miss: [pipfreeze 1/1] RUN pip freeze > /tmp/freeze.txt
cache miss: [base 6/9] RUN pip install --no-cache-dir pip -U && 	pip install --no-cache-dir 	datasets 	"huggingface-hub>=0.19" "hf_xet>=1.0.0,<2.0.0" "hf-transfer>=0.1.4" "protobuf<4" "click<8.1" "pydantic==2.10.6"
cache miss: [base 4/9] RUN curl https://pyenv.run | bash
{"total":27,"completed":22,"user_total":16,"user_cached":0,"user_completed":11,"user_cacheable":15,"from":1,"miss":15,"client_duration_ms":233887}

Build logs:

--------------------