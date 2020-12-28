dir=$(pwd)
activeCtnPrefixFile=$dir/activeCtnPrefix

if [ -f "$activeCtnPrefixFile" ]; then
  read -r activeCtnPrefix<$activeCtnPrefixFile
  echo 'Starting Docker Container ...'
  docker start ${activeCtnPrefix}1 > /dev/null 2>&1
  docker start ${activeCtnPrefix}2 > /dev/null 2>&1
  docker start ${activeCtnPrefix}3 > /dev/null 2>&1
  docker start ${activeCtnPrefix}4 > /dev/null 2>&1
  docker start ${activeCtnPrefix}5 > /dev/null 2>&1
  docker start ${activeCtnPrefix}6 > /dev/null 2>&1
  echo
  echo 'Container started, you can access VoltDB nodes via this port:'
  docker port ${activeCtnPrefix}1 21212
  docker port ${activeCtnPrefix}2 21212
  docker port ${activeCtnPrefix}3 21212
  docker port ${activeCtnPrefix}4 21212
  docker port ${activeCtnPrefix}5 21212
  docker port ${activeCtnPrefix}6 21212
  echo
  echo 'You can also access VoltDB web admin via this port:'
  docker port ${activeCtnPrefix}1 8080
  docker port ${activeCtnPrefix}2 8080
  docker port ${activeCtnPrefix}3 8080
  docker port ${activeCtnPrefix}4 8080
  docker port ${activeCtnPrefix}5 8080
  docker port ${activeCtnPrefix}6 8080
else
  echo 'No Active Cluster Record Found, please run init_cluster.sh first'
fi
