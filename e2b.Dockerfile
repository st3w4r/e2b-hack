# You can use most of the Debian-based base images
FROM e2bdev/code-interpreter:latest

# Install dependencies and customize sandbox
RUN apt update \
	&& apt install sudo


RUN pip install playwright

RUN playwright install