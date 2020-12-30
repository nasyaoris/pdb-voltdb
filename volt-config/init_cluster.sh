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
read -r -p 'Container Name: ' ctn

# Check if user want to use their own bridge
read -r -p 'Bridge network to use (create new docker bridge network first if not): ' networkName

# Pull for latest
echo 'Pulling latest docker image ...'
docker pull voltdb/voltdb-community

# Create container
echo 'Creating new container ...'
docker run -d -P -v $dir/deployment.xml:/tmp/deployment.xml -v $dir/sql:/tmp/config/sql -v $dir/procedures:/tmp/config/procedures -v ${ctn}1:/var/voltdb -e HOSTS=${ctn}1,${ctn}2,${ctn}3,${ctn}4,${ctn}5,${ctn}6 --name=${ctn}1 --network=$networkName voltdb/voltdb-community:latest
docker run -d -P -v $dir/deployment.xml:/tmp/deployment.xml -v ${ctn}2:/var/voltdb -e HOSTS=${ctn}1,${ctn}2,${ctn}3,${ctn}4,${ctn}5,${ctn}6 --name=${ctn}2 --network=$networkName voltdb/voltdb-community:latest
docker run -d -P -v $dir/deployment.xml:/tmp/deployment.xml -v ${ctn}3:/var/voltdb -e HOSTS=${ctn}1,${ctn}2,${ctn}3,${ctn}4,${ctn}5,${ctn}6 --name=${ctn}3 --network=$networkName voltdb/voltdb-community:latest
docker run -d -P -v $dir/deployment.xml:/tmp/deployment.xml -v ${ctn}4:/var/voltdb -e HOSTS=${ctn}1,${ctn}2,${ctn}3,${ctn}4,${ctn}5,${ctn}6 --name=${ctn}4 --network=$networkName voltdb/voltdb-community:latest
docker run -d -P -v $dir/deployment.xml:/tmp/deployment.xml -v ${ctn}5:/var/voltdb -e HOSTS=${ctn}1,${ctn}2,${ctn}3,${ctn}4,${ctn}5,${ctn}6 --name=${ctn}5 --network=$networkName voltdb/voltdb-community:latest
docker run -d -P -v $dir/deployment.xml:/tmp/deployment.xml -v ${ctn}6:/var/voltdb -e HOSTS=${ctn}1,${ctn}2,${ctn}3,${ctn}4,${ctn}5,${ctn}6 --name=${ctn}6 --network=$networkName voltdb/voltdb-community:latest

# Print port
echo 'Container created, init successful, you can now access your VoltDB cluster nodes on these ports:'
docker port ${ctn}1 21212
docker port ${ctn}2 21212
docker port ${ctn}3 21212
docker port ${ctn}4 21212
docker port ${ctn}5 21212
docker port ${ctn}6 21212
echo
echo 'You can also access VoltDB web admin via this port:'
docker port ${ctn}1 8080
docker port ${ctn}2 8080
docker port ${ctn}3 8080
docker port ${ctn}4 8080
docker port ${ctn}5 8080
docker port ${ctn}6 8080

# Saving current node prefix name
echo $ctn > activeCtnPrefix
