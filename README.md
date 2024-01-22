# emr_compute_translate_words

Extracting translation of words. AWS infra services (EMR, Lambda Function)

# Extra details - Methods

## Spark - Cluster Compute

### Driver resources

**WORKER** - a worker node is a machine within a cluster responsible for performing computational tasks.
**CORE** - a core is a processing unit within the CPU of that node. The number of cores in a node can affect its ability to handle parallel workloads efficiently.
In a cluster, the combination of multiple worker nodes and the cores within each node allows for distributed and parallel processing of tasks

## Spark Deploy Modes – Client vs Cluster

Using spark-submit --deploy-mode <client/cluster>, you can specify where to run the Spark application driver program.
**client** - the driver runs locally from where you are submitting your application. majorly used for interactive and debugging purposes
**cluster** - the driver runs on one of the worker nodes. run production jobs for big data processes

## Cluster Managers (–master)

specify what cluster manager to use to run your application
**yarn** - Use yarn if your cluster resources are managed by Hadoop Yarn.
**local** - Use local to run locally with a one worker thread.
Use local[k] and specify k with the number of cores you have locally, this runs application with k worker threads.

## Hadoop

### Hadoop - Storage

**HDFS (Hadoop Distributed File System)** is not a traditional database but a distributed file system designed to store and process big data.
**HDFS, NameNode** is the FS of the Master node.
**HDFS, DataNode** is the FS of the Slave node.
In AWS there is an alternative to use S3 as FS (FIle System) instead of HDFS

### Hadoop - Compute Handler

YARN is responsible for allocating system resources to the various applications running and scheduling tasks to be executed on different cluster nodes.
**YARN, ResourceManager** of the Master node
**YARN, NodeManagers** of the Slave node

### Hadoop - Query Data

Hive gives an SQL-like interface to query data stored in various databases and file systems that integrate with Hadoop
In AWS on top of disturbuted file in S3, we can running a crawler to query the data using Athena (Hive too)




