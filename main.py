from services.dynamodb_manager import DynamodbManager

db = DynamodbManager()

# db.create_table()

# db.insert_item(2,"Raj",23)
# db.delete_item(2)
# db.get_item(1)
db.scan_table()