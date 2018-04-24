#
# # Definition of Contacts object
# #     Later: getters & putters
#

#
# # imports
#
import boto3
from botocore.exceptions import ClientError
import pickle
#
# # Customization
#
BUCKET = "dgl-contacts"             # the bucket where DGL Contacts are stored
DOMAIN_NAME = "foolsorknaves.com" # The domain for this instance
print("dglContacts loaded", BUCKET, DOMAIN_NAME)    
#
# # class defs
#
class Contact:
    """class Contact
            first_name, last_name, email, attrs
                atttrs depends on application using the object
    """
    def __init__(self, email,  first_name="",  last_name=""):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.attrs = []    #new empty list of attributes for each contact
        
        
class Contacts:
    def __init__(self,  bucket):
        self.contacts = {}        # Dictionary holding Contacts, key is email
        self.bucket = bucket    # Bucket holding Contacts object

        
    def addContact(self,  Contact):
        print("Add Contact")
        pass
        
    def getContact(self,  Contact):      
        pass
    
    def updateContact(self,  Contact):
        pass

#
# # function defs
#
def getContacts(bucket, file_name):
    """getContacts()
            Gets marshalled Contacts object from S2
            Unmarshalls
            returns Contacts
            
             Boto 3
            
    """
    s3 = boto3.resource('s3') # get S3.Object
    
    bucket = s3.Bucket(BUCKET)
    for obj in bucket.objects.all():
        print(obj.key)
        
    contacts = {}    
   
    try:
         contacts = s3.Object(BUCKET, 'contacts').get()["Body"].read()
    except ClientError:
       print("The object does not exist.")
       createContacts(BUCKET)
     
    return(contacts)  
    
def confirmContact():
        """confirmContact()
                Sends SES email to new contact
        """
        print("In confirmContact")
        pass

def createContacts(bucket):
    
    """
        Create Contacts - put new Contacts object in S3 bucket 'dgl-contacts'
    """
    print("bucket type:",type(bucket))
    
    s3 = boto3.resource('s3')                   # get S3.Object
    
    contacts = Contacts(bucket)               # Contacts object with empty dictionary
    body = pickle.dumps(contacts)           # serialized Contacts object
    try:
        s3.Object(contacts.bucket, 'contacts').put(Body=body)
    except Exception as e:
        print(type(e))
        print(e.args)
        print(e)
        
    
    for obj in contacts.bucket.objects.all():
        print(obj.key) 
