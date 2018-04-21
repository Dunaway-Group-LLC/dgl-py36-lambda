#
# # AWS Lambda Handler 
#
import boto3

def dglAddContact(event, context): 
    first_name = event["first_name"];
    last_name = event["last_name"]
    email = event["email"]
    reviewer = event["reviewer"] == ("Y" or "y")
    response = "Response: ".format(first_name,last_name,email,reviewer)
    return some_value
