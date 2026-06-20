#IMPORT ALL THE MODULES AND LIBRARIES
import boto3 

#OPEN MANAGEMENT CONSOLE
aws_management_console = boto3.session.Session(profile_name="default")

#OPEN IAM CONSOLE
ec2_console = aws_management_console.client( service_name = "ec2")
# print(ec2_console.meta.region_name)
# result = ec2_console.describe_instances()["Reservations"]
# print(result) 



#CREATING EC2 INSTANCE
# create_ec2 = ec2_console.run_instances(
#     ImageId='ami-023b6eace47afd3b4',
#     InstanceType='t3.micro',
#     MaxCount=1,
#     MinCount=1
# )

#STOPPING EC2 INSTANCE
# stopped= ec2_console.stop_instances(
#     InstanceIds=['']
# )

#RESTART THE SAME INSTANCE
# started= ec2_console.start_instances(
#     InstanceIds=['']
# )

#TERMINATE EC2 INSTANCE
# terminated= ec2_console.terminate_instances(
#     InstanceIds=['']
# )

# Check Which Instance Types Are Free Tier Eligible
# response = ec2_console.describe_instance_types(
#     Filters=[
#         {
#             'Name': 'free-tier-eligible',
#             'Values': ['true']
#         }
#     ]
# )

# for instance in response['InstanceTypes']:
#     print(instance['InstanceType'])


