dir=$(pwd)
activeCtnPrefixFile=$dir/activeCtnPrefix

if [ -f "$activeCtnPrefixFile" ]; then
  read -r activeCtnPrefix<$activeCtnPrefixFile
  echo 'Stopping active docker container...'
  docker stop ${activeCtnPrefix}1 > /dev/null 2>&1
  docker stop ${activeCtnPrefix}2 > /dev/null 2>&1
  docker stop ${activeCtnPrefix}3 > /dev/null 2>&1
  docker stop ${activeCtnPrefix}4 > /dev/null 2>&1
  docker stop ${activeCtnPrefix}5 > /dev/null 2>&1
  docker stop ${activeCtnPrefix}6 > /dev/null 2>&1
  echo 'VoltDB container has been stopped, run start_cluster.sh to run it again'
else
  echo 'No Active Cluster Record Found, please run init_cluster.sh first'
fi
