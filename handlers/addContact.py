#
# # AWS Lambda Handler 
#
import boto3
import addContact-classes

def addContact(event, context): 
    
    first_name = event['queryStringParameters']["first_name"];
    last_name = event['queryStringParameters']["last_name"]
    email = event['queryStringParameters']["email"]
    reviewer = event['queryStringParameters']["reviewer"] == ("Y" or "y") # True if == Y or y
    product = event['queryStringParameters']["product"]
    
    print(first_name," / ",last_name," / ",email," / ",reviewer," / ",product)
    return {}
