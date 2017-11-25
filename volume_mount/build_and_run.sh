docker build -t volume_mount_hello_world .

docker run \
    -v a_volume:/home/work \
    volume_mount_hello_world:latest

# TODO: read path from docker inspect a_volume
sudo ls /var/lib/docker/volumes/a_volume/_data/
sudo cat /var/lib/docker/volumes/a_volume/_data/out.txt
