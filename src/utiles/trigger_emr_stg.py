import json;
import boto3;

client = boto3.client('emr')


def lambda_handler(event, context):
    
    word = 'family'
    print("translate word : ",word)

    init_bash_script = 's3://datalake-translate-words/scripts/config/hadoop_config.sh'
    hadoop_config = [
        "bash",
        "-c",
        f" aws s3 cp {init_bash_script} ~/.; chmod +x ~/hadoop_config.sh; ~/hadoop_config.sh; rm ~/hadoop_config.sh "
    ]
    print("Spark Submit Bash: ",hadoop_config)

    backend_code_raw="s3://datalake-translate-words/scripts/raw.py"
    spark_submit_raw = [
        'spark-submit',
        '--master', 'yarn',
        '--deploy-mode', 'cluster',
        backend_code_raw,
        word
    ]
    print("Spark Submit Raw: ",spark_submit_raw)
    
    backend_code_curated="s3://datalake-translate-words/scripts/curated.py"
    spark_submit_curated = [
        'spark-submit',
        '--master', 'yarn',
        '--deploy-mode', 'cluster',
        backend_code_curated
    ]
    print("Spark Submit Curated: ",spark_submit_curated)
    
    cluster_id = client.run_job_flow(
        Name="transformation_staging_and_curated",
        Instances={
                'InstanceGroups': [
                    {
                        'Name': "Master",
                        'Market': 'ON_DEMAND',
                        'InstanceRole': 'MASTER',
                        'InstanceType': 'm4.large',
                        'InstanceCount': 1,
                    },
                    {
                        'Name': "Slave",
                        'Market': 'ON_DEMAND',
                        'InstanceRole': 'CORE',
                        'InstanceType': 'm4.large',
                        'InstanceCount': 1,
                    },
                    {
                        'Name': "Slave",
                        'Market': 'ON_DEMAND',
                        'InstanceRole': 'TASK',
                        'InstanceType': 'm4.large',
                        'InstanceCount': 1,
                    }
                ],
                'Ec2KeyName': 'cluster-key-vs-pm',
                'KeepJobFlowAliveWhenNoSteps': False,
                'TerminationProtected': False,
                'Ec2SubnetId': 'subnet-0097481e6feb2f4a7',
            },
            LogUri="s3://datalake-translate-words/spark-logs/",
            ReleaseLabel= 'emr-6.15.0',
            Steps=[{
                "Name": "Setup Hadoop configuration - additional python libraries",
                "ActionOnFailure": "CONTINUE",
                "HadoopJarStep": {
                    "Jar": "command-runner.jar",
                    "Args": hadoop_config
                }
            },
            {
                "Name": "raw_data",
                'ActionOnFailure': 'CONTINUE',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': spark_submit_raw
                }
            },
            {
                "Name": "curated_data",
                'ActionOnFailure': 'CONTINUE',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': spark_submit_curated
                }
            }],
        BootstrapActions=[],
        VisibleToAllUsers=True,
        JobFlowRole="EMR_EC2_DefaultRole",
        ServiceRole="EMR_DefaultRole",
        Applications = [ {'Name': 'Spark'},{'Name':'Hive'},{'Name':'Hadoop'},{'Name':'JupyterEnterpriseGateway'},{'Name':'Livy'}]
    )