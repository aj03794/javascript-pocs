# https://hashedin.com/blog/open-closed-principle-in-python-designing-modules-part-4/

# Background

# Customers are complaining that they don’t receive SMS’es at times. 
# Watertel recommends resending the SMS if the status code is 5xx. 
# Hence we need to extend the sms module to support retries with exponential backoff. 
# The first retry should be immediate, the next retry within 2s, 
# and the third retry within 4s. If it still continues to fail, 
# give up and don’t try further.

# We need something sitting in between our clients and our SmsClient class
# That something can be a derived class of SmsClient


# ----------------------------------------------------

# This is the class we wrote in Part III
# We are not allowed to change this class
class SmsClient:
    def send_sms(self, phone_number, message):
        ...
 
class SmsClientWithRetry(SmsClient):
    def __init__(self, username, password):
        super(SmsClient, self).__init__(username, password)
 
    def send_sms(self, phone_number, message):
        # TODO: Insert retry logic here
        super(SmsClient, self).send_sms(phone_number, message)
        # TODO: Insert retry logic here
 
# Earlier, client was an instance of SmsClient, like this
# client = SmsClient(username, password)
# We now change it to be an instance of SmsClientWithRetry
# As a result, our client developers doesn't have to change 
# They are simply importing client from sms.py
 
client = SmsClientWithRetry(username, password)

# Using inheritance, we got ourselves a way to retry logic w/o modifying the existing
# code that is already known to work