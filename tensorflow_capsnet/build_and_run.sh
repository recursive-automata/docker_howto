docker build -t tensorflow_capsule_example .
nvidia-docker run -v a_volume:/home/work tensorflow_capsule_example:latest
