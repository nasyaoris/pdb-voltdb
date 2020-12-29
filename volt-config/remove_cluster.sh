dir=$(pwd)
activeCtnPrefixFile=$dir/activeCtnPrefix

if [ -f "$activeCtnPrefixFile" ]
then
  read -r activeCtnPrefix<$activeCtnPrefixFile
  echo 'Removing active docker containers and cluster...'
  docker container rm ${activeCtnPrefix}1 > /dev/null 2>&1
  docker container rm ${activeCtnPrefix}2 > /dev/null 2>&1
  docker container rm ${activeCtnPrefix}3 > /dev/null 2>&1
  docker container rm ${activeCtnPrefix}4 > /dev/null 2>&1
  docker container rm ${activeCtnPrefix}5 > /dev/null 2>&1
  docker container rm ${activeCtnPrefix}6 > /dev/null 2>&1

  echo
  echo 'Do you want to remove the stored snapshots and clear the entire database?'
  echo

  # Does the user wants to delete docker volumes containing snapshot?
  read -p 'Clear? (yes/no): ' confirmClear

  if [ "$confirmClear" = "yes" ]
  then
    echo 'Removing docker volume information...'
    docker volume rm ${activeCtnPrefix}1 > /dev/null 2>&1
    docker volume rm ${activeCtnPrefix}2 > /dev/null 2>&1
    docker volume rm ${activeCtnPrefix}3 > /dev/null 2>&1
    docker volume rm ${activeCtnPrefix}4 > /dev/null 2>&1
    docker volume rm ${activeCtnPrefix}5 > /dev/null 2>&1
    docker volume rm ${activeCtnPrefix}6 > /dev/null 2>&1
  fi
  rm $activeCtnPrefixFile
  echo 'VoltDB cluster has been removed, run init_cluster.sh again to create another'
else
  echo 'No Active Cluster Record Found, please run init_cluster.sh first'
fi
