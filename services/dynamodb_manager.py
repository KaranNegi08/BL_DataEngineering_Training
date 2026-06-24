import boto3
from config.config import TABLE_NAME,REGION
from boto3.dynamodb.conditions import Key

class DynamodbManager:
    def __init__(self):
        self.dynamodb = boto3.resource(
            "dynamodb",
            region_name=REGION
        )

        self.client = boto3.client(
            "dynamodb",
            region_name=REGION
        )

        self.table_name = TABLE_NAME

        self.table = self.dynamodb.Table(
            self.table_name
        )

    
    def create_table(self):
        try:
            table = self.dynamodb.create_table(
            TableName = "TAG",
            KeySchema = [
                {
                    'AttributeName':'TAG_ID',
                    'KeyType':'HASH'
                }
            ],
            AttributeDefinitions = [
                {
                    'AttributeName':'TAG_ID',
                    'AttributeType':'N'
                }
            ],
            BillingMode='PAY_PER_REQUEST'
            )

            table.wait_until_exists()
            print(f"{self.table_name} created successfully..")
        except Exception as e:
            print(e)
        

    def insert_item(self, tag_id,name,city):
        try:
            self.table.put_item(
                Item={
                        "TAG_ID": tag_id,
                        "NAME": name,
                        "CITY": city
                    }
            )
            print(f"{name} Inserted Successfully...")
        except Exception as e:
            print(e)

    def get_item(self, tag_id):
        try:
            response = self.table.get_item(
                Key={
                    "TAG_ID":tag_id
                }
            )
            item = response.get("Item")
            print(item)

        except Exception as e:
            print(e)


    def delete_item(self, tag_id):
        try:
            self.table.delete_item(
                Key={
                    "TAG_ID":tag_id
                }
            )
            print("Item Deleted Successfully..")

        except Exception as e:
            print(e)

    def query_item(self, tag_id):
        try:
            response = self.table.query(
                KeyConditionExpression=
                Key("TAG_ID").eq(tag_id)
            )
            items = response["Items"]
            print(items)
        except Exception as e:
            print(e)

    def scan_table(self):
        try:
            response = self.table.scan()
            items = response["Items"]
            print(items)
            return items
        except Exception as e:
            print(e)