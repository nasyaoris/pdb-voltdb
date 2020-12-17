dir=$(pwd)
activeNodeFile=$dir/activeNode

if [ -f "$activeNodeFile" ]; then
  read -r activeNode<$activeNodeFile
  echo 'Stopping active docker container...'
  docker stop $activeNode > /dev/null 2>&1
  echo 'VoltDB container has been stopped, run start.sh to run it again'
else
  echo 'No Active Node Record Found, please run init.sh first'
fi

