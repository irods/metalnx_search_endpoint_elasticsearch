# Docker Testing Framework for Metalnx 

This testing framework provides a disposable docker image of a running metalnx, including the metalnx database. This arrangement is meant to use the iRODS configuration found in the [Jargon Docker Testing Framework] (https://github.com/DICE-UNC/jargon/blob/master/DOCKERTEST.md), utilizing the same testing properties and setup facilities across all the services.

# Steps to set up test environment

### run iRODS

Follow steps in [Jargon Docker Testing Framework] (https://github.com/DICE-UNC/jargon/blob/master/DOCKERTEST.md) to start up an iRODS instance

You should be able to issue a docker ps command and see these services running

```
LMBP-02010755:docker-test-framework conwaymc$ docker ps
CONTAINER ID        IMAGE                                  COMMAND                  CREATED             STATUS              PORTS                              NAMES
77f0c2c2fe20        metalnx                                "/runit.sh"              About an hour ago   Up 15 minutes       0.0.0.0:8080->8080/tcp             metalnx
2d94c58fd077        4-2_irods-catalog-consumer-resource1   "./start_consumer.sh"    20 hours ago        Up 20 hours         1247-1248/tcp                      irods-catalog-consumer-resource1
072086ac44e1        4-2_irods-catalog-provider             "./start_provider.sh"    20 hours ago        Up 20 hours         0.0.0.0:1247->1247/tcp, 1248/tcp   irods-catalog-provider
c7e102bd061d        4-2_maven                              "/usr/local/bin/mvn-…"   20 hours ago        Up 20 hours                                            maven
ALMBP-02010755:docker-test-framework conwaymc$ 


```

### Set an environment variable to point to the required etc config files 

in this subdirectory is an etc/irods-ext directory, set the variable to point to this local location and mount in the docker image. Open a terminal to the docker-test-framework subdirectory and issue:

```

export METADATA_IRODS_EXT_LOCATION=`pwd`/etc/irods-ext


```

If you have variations you may copy or edit properties in place and reposition the environment variable

### run docker-compose build from the docker-test-framework directory

from the docker-test-framework directory, run the docker-compose build command so that the proper docker image is created
```

From this location, build the necessary docker images

```
docker-compose build

```


### Start ES and the search plugin via this docker compose file

```
docker-compose up -d 

```

You should now be able to start the metalnx complex from https://github.com/irods-contrib/metalnx-web/blob/master/docker-test-framework/README.md

The iRODS, search, and metalnx containers should all be able to find each other. You should start this search plugin before
the metalnx startup so it is discovered on init