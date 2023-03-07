import boto3
TableName= "Newtable"
Primary_Column_Name="UID"
Primary_key=1
columns=["Name","Value"]
dynamodb = boto3.resource('dynamodb')
Primary_key=3
table = dynamodb.Table('MyTable')
response= table.delete_item(
     key={
    Primary_Column_Name:Primary_key
    }
)
response
