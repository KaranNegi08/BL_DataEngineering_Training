import boto3 
from botocore.exceptions import ClientError

#OPEN MANAGEMENT CONSOLE
aws_management_console = boto3.session.Session(profile_name="default")
# print(aws_management_console.region_name)
#OPEN IAM CONSOLE
s3_console = aws_management_console.client( service_name = "s3")
# try:
#     response = s3_console.create_bucket(
#         Bucket='testing-s3-bucket-demo2026',
#         CreateBucketConfiguration={
#             'LocationConstraint': 'eu-north-1'
#         }
#     )
#     print("Bucket Created Successfully")

# except ClientError as e:
#     print(e)

# data_upload = s3_console.upload_file(r'C:\Users\Asus\aws_cli\sales.csv','testing-s3-bucket-demo2026', 'sales.csv')

# file_download = s3_console.download_file('testing-s3-bucket-demo2026', 'sales.csv',r'D:\BOTO3_FILES\sales.csv')

# import json
# data= {'age': 22}
# data = json.dumps(data).encode('UTF-8')
# write_file = s3_console.put_object(Body=data,Bucket= 'testing-s3-bucket-demo2026', Key='new_file2')

# get_file = s3_console.get_object(Bucket= 'testing-s3-bucket-demo2026', Key='sales.csv')
# data = get_file['Body'].read()
# print(data)


# delete_obj = s3_console.delete_object(Bucket='testing-s3-bucket-demo2026',Key='new_file2')

list_files = s3_console.list_objects_v2(
    Bucket = 'testing-s3-bucket-demo2026'
    
)

for key in list_files['Contents']:
    print(key)