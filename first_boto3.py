import boto3

aws_management_console= boto3.session.Session(profile_name="default")

iam_console = aws_management_console.resource('iam')

for each_user in iam_console.users.all():
    print(each_user.name)

# Boto3 provides two interfaces:
# 1. RESOURCES--
# High-level Object-Oriented API
# work with Python objects instead of raw JSON.
# print(aws_management_console.get_available_resources())

# 2. CLIENT--
# Low-level API
# iam = boto3.client("iam")
# response = iam.list_users()
# print(response)   #returns JSON response