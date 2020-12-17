#!/bin/sh
dir=$(pwd)

echo '🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀'
echo
echo '🌏                                     VoltDB Quick Docker Install Script                                           🌏'
echo
echo '🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀  🚀'

echo
echo 'First, provide the docker container name to initiate, and make sure this directory also contains deployment.xml file'
echo

# Should be unique, otherwise we can't create a duplicate container on docker, will fail if not
read -r -p 'Container Name: ' containerName

# Check if user want to use their own bridge
read -r -p 'Bridge network to use (create new docker bridge network first if not): ' networkName

# Pull for latest
echo 'Pulling latest docker image ...'
docker pull voltdb/voltdb-community

# Create container
echo 'Creating new container ...'
docker run -d -P -v $dir/deployment.xml:/tmp/deployment.xml -v $dir:/var/voltdb -e HOSTS=$containerName --name=$containerName --network=$networkName voltdb/voltdb-community:latest

# Print port
echo 'Container created, init successful, you can now access your VoltDB instance on this port:'
docker port $containerName 21212

# Saving current node name
echo $containerName > activeNode
