# PDB KELOMPOK 15 - VOLTDB

# HOW TO RUN TEST-SIMULATOR APP

# 1. Run Volt Configuration Base.

This folder contains scripts to setup, run, stop, and clear VoltDB clusters used to develop this online test app. There are 5 scripts:

## Prerequisites
- Docker
- run `docker network create -d bridge anyNameYouWant`
- Preferably openjdk installed
- Preferably voltdb community edition installed, the included `sqlcmd` package will help massively in doing query from terminal.

## Scripts
There are 5 main scripts in this helper app, here is what each of them do:

### init_cluster.sh
Run this script for initial cluster setup, you will be asked about your cluster name and the bridge network to be used (the one you create on prerequisite section above). After filling that, just wait for the script to initiate 6 docker containers forming a 2-node cluster with each node containing 3 containers running in k-safety mode (means if even 2 of them fails, the system can still operate). After running this script, you will be given each VoltDB instance mapped port you can use to access the VoltDB on the cluster, and the VoltDB admin website mapped port that you can open in the browser (localhost:mappedPort)

### init_db.sh
Run this script after `init_cluster.sh` to setup initial db schema, stored procedures, and populating data. Run this a little bit after `init_cluster.sh` is finished or whenever the voltdb instance finished booting up (check with sqlcmd to the port or open the web admin).

### stop_cluster.sh
Stop all running containers in the cluster

### start_cluster.sh
Restart all container in the cluster, starts back with the latest stored snapshot in the database

### remove_cluster.sh
Make sure you do `stop_cluster.sh` before running this, this removes all container nodes in the cluster, if you want you can also remove each container volumes to fully remove the stored snapshot data of each containers to do a fresh start. If you dont remove the volumes, you can just do `init_cluster.sh` and it will start with the stored snapshot data. If you removed the volume, you also have to redo the `init_db.sh` and all the previously saved data will be gone.

## DB Schema & Data Definition
All SQL related queries used to setup the database is stored under the `sql` folder. Schema is defined under `schema.sql`, custom stored procedures is registered in `register_procedures.sql`, and dummy data to populate the empty database is stored under `populate.sql`

## Stored Procedures
All custom stored procedures are written under the `procedures` folder, defined under `onlinetest.procedures` package. To add, just create another `.java` file with the same package, and don't forget to register the custom stored procedures to VoltDB inside the `sql/register_procedures.sql` to activate it in VoltDB.


# 2. Run Django Application.
First things first change client port in FastSeriliezers at every views.py to 212121/tcp port
you can check it at `docker port voltdb1`
## a. Use Docker Compose
1. install docker-compose
2. Run in your terminal `docker-compose up -d`
3. Application should be running at `localhost:80/registration/loginPage`

## b. Run Manually
1. install python 3.7
2. install pip
3. run `pip3 install requirements.txt`
4. run `python3 manage.py runserver`
