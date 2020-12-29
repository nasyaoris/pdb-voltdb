dir=$(pwd)
activeCtnPrefixFile=$dir/activeCtnPrefix

if [ -f "$activeCtnPrefixFile" ]; then
  read -r activeCtnPrefix<$activeCtnPrefixFile
  echo 'Injecting Schema ...'
  docker exec -it -w /tmp/config ${activeCtnPrefix}1 bash -c "sqlcmd < ./sql/schema.sql"

  echo 'Building Procedures ...'
  docker exec -it -w /tmp/config ${activeCtnPrefix}1 bash -c 'mkdir ./obj'
  docker exec -it -w /tmp/config ${activeCtnPrefix}1 bash -c 'javac -classpath "./:/opt/voltdb/voltdb/*" -d ./obj ./procedures/*.java'
  docker exec -it -w /tmp/config ${activeCtnPrefix}1 bash -c 'jar cvf myproc.jar -C obj .'

  echo 'Registering Procedures ...'
  docker exec -it -w /tmp/config ${activeCtnPrefix}1 bash -c 'sqlcmd < ./sql/register_procedures.sql';
  docker exec -it -w /tmp/config ${activeCtnPrefix}1 bash -c 'sqlcmd < ./sql/populate.sql';
else
  echo 'No Active Cluster Record Found, please run init_cluster.sh first'
fi
