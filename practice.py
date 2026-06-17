#IMPORT ALL THE MODULES AND LIBRARIES
import boto3 

#OPEN MANAGEMENT CONSOLE
aws_management_console = boto3.session.Session(profile_name="default")

#OPEN IAM CONSOLE
iam_console = aws_management_console.client( service_name = "iam")
response = iam_console.list_users()

# for user in response['Users']:
#     print(user['UserName'])
