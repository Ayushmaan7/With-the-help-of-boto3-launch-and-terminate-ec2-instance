import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')

# Launch EC2 instance
instances = ec2.create_instances(
    ImageId='ami-12345678',  # Replace with the correct AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Type of instance (t2.micro is free-tier eligible)
    KeyName='your-key-pair',  # Replace with your key pair name
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'MyBoto3Instance'
                }
            ]
        }
    ]
)

print(f"Instance launched with ID: {instances[0].id}")
