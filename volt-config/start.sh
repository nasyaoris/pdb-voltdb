dir=$(pwd)
activeNodeFile=$dir/activeNode

echo $activeNodeFile

if [ -f "$activeNodeFile" ]; then
  read -r activeNode<$activeNodeFile
  echo 'Starting Docker Container ...'
  docker start $activeNode > /dev/null 2>&1
  echo
  echo 'Container started, you can access VoltDB via this port:'
  docker port $activeNode 21212
else
  echo 'No Active Node Record Found, please run init.sh first'
fi

