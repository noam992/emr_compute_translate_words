import json;
import boto3;

client = boto3.client('emr')


def lambda_handler(event, context):
    
    word = 'home'
    print("translate word : ",word)
    
    backend_code="s3://datalake-stock/assets/emr_code_stg/emr_stg.py"
    spark_submit = [
        'spark-submit',
        '--master', 'yarn',
        '--deploy-mode', 'cluster',
        backend_code,
        word
    ]
    print("Spark Submit : ",spark_submit)
    
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
            LogUri="s3://datalake-stock/spark-logs/",
            ReleaseLabel= 'emr-6.15.0',
            Steps=[{
                "Name": "testJobGURU",
                'ActionOnFailure': 'CONTINUE',
                'HadoopJarStep': {
                    'Jar': 'command-runner.jar',
                    'Args': spark_submit
                }
            }],
        BootstrapActions=[],
        VisibleToAllUsers=True,
        JobFlowRole="EMR_EC2_DefaultRole",
        ServiceRole="EMR_DefaultRole",
        Applications = [ {'Name': 'Spark'},{'Name':'Hive'},{'Name':'Hadoop'},{'Name':'JupyterEnterpriseGateway'},{'Name':'Livy'}]
    )