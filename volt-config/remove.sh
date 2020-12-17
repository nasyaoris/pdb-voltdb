dir=$(pwd)
activeNodeFile=$dir/activeNode

if [ -f "$activeNodeFile" ]; then
  read -r activeNode<$activeNodeFile
  echo 'Removing active docker container...'
  docker container rm $activeNode > /dev/null 2>&1
  rm $activeNodeFile
  echo 'VoltDB container has been removed, run init.sh again to create another'
else
  echo 'No Active Node Record Found, please run init.sh first'
fi

