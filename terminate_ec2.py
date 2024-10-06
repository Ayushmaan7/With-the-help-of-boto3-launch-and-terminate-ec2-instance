import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.client('ec2')

# Replace with your instance ID
instance_id = 'i-0abcd1234efgh5678'

# Terminate the instance
response = ec2.terminate_instances(InstanceIds=[instance_id])

print(f"Terminated instance: {instance_id}")
