# https://hashedin.com/blog/inheritance-versus-composition-in-python-designing-modules-part-5/

# Create MilioClient interface with the same interface as our original SmsClient

class MilioClient:
    def __init__(self, url, access_token):
        self.url = url
        self.access_token = access_token
 
    def send_sms(self, phone_number, message):
        # Similar to send_sms method in SmsClient
        # Difference would be in the implementation of _make_request
        # We will have different JSON response, 
        # and different request parameters
        print("Milio Client: Sending Message '%s' to Phone %s" 
                 % (message, phone_number))

# -------------------------------------------------

# 1) Should MilioClient extend SmsClient?
# No, they both they are making network calls, isn't much commonality
# The request params are different, the response format is different

# 2) Should MilioClient extend SmsClientWithRetry?
# Maybe, the retry logic is reusable and common between the two
# Can reuse that logic using inheritance; but it isn't the right way to reuse
# Will discuss this later

# Inheritance vs Composition
# The reason why we can't inherit the SmsClientWithRetry class is that the constructor
# of the class expects a username and password
# We don't have that for Milio
# This conflict is largely b/c we made a mistake in the earlier chapter - we chose
# to build new logic using inheritance
# Will refactor code and using Composition instead of inheritance

# -------------------------------------------------

# This makes the intent of the class clear
# We don't change anything else in the class
class WatertelSmsClient(object):
    def send_sms(self, phone_number, message):
    ...
 
# This is our new class to send sms using Milio's APi 
class MilioSmsClient(object):
    def send_sms(self, phone_number, message):
    ...
 
class SmsClientWithRetry(object):
    def __init__(self, sms_client):
        self.delegate = sms_client
 
    def send_sms(self, phone_number, message): 
        # Insert start of retry loop 
        self.delegate.send_sms(phone_number, message)
        # Insert end of retry loop
 
_watertel_client = SmsClient(url, username, password) 
# Here, we are passing watertel_client 
# But we could pass an object of MilioClient, 
# and that would still give us retry behaviour
sms_client = SmsClientWithRetry(_watertel_client)


# -------------------------------------------------

# Logic to Split Traffic

# Generate a random number between 1 and 100
# Will get an 80/20 split btwn implementations

# -------------------------------------------------

# Introducing a Router Class

# Where should we put this logic? Cannot change the existing client implementations
# Can't put th logic in `MilioSmsClient` or `WatertelSmsClient` - that logic doesn't belong there

# We need to create an intermediate class that is used by all existing clients
# This class decides to split the logic between the two clients
# Will call it `SmsRouter`

class SmsRouter:
    def send_sms(self, phone_number, message):
        # Generate random number
        # Between 1-80? Call send_sms method in SmsClient
        # Between 80-100? Call send_sms method in MilioClient
        pass


class SmsRouter:
    def __init__(self, milio_url, milio_access_token,
                       watertel_url, watertel_username, watertel_password):
        self.milio = MilioSmsClient(milio_url, milio_access_token)
        self.watertel = WatertelSmsClient(watertel_url, watertel_username, watertel_password)


# Could simplify this further to
class SmsRouter:
    def __init__(self, milio, watertel):
        self.milio = milio
        self.watertel = watertel
    

# Removing hardcoded percentages
class SmsRouter:
    def __init__(self, milio, milio_percentage, watertel, watertel_percentage):
        self.milio = milio
        self.milio_percentage = milio_percentage
        self.watertel = watertel
        self.watertel_percentage = watertel_percentage


# -------------------------------------------------

# Generalizing SmsRouter

# Generalize by passing a list of sms providers

class SmsRouter:
    def __init__(self, providers):
        '''Providers is a list of tuples, each tuple having a provider and a percentage
           providers = [(watertel, 80), (milio, 20)]'''
        self.providers = providers
    
    def _pick_provider(self):
        # Pick up a provided on the basis of the percentages provided
        # For now, we will pick a random one
        return self.providers[randint(0, 1)][0]
     
    def send_sms(self, phone_number, message):
        provider = self._pick_provider()
        provider.send_sms(phone_number, message)

# With this version of SmsRouter, we can now provide multiple implementations
# and the router will intelligently delegate to the right router


# -------------------------------------------------

# Using our SmsRouter

# First, create the concrete implementations
watertel = SmsClient("https://watertel.example.com", "username", "password")
milio = MilioClient("https://milio.example.com", "secret_access_token")

# Create a router with an 80/20 split
sms = SmsRouter([(watertel, 80), (milio, 20)])

# Calling the send_sms in a loop will on an average 
# send the messages using the percentages provided
for x in range(1, 10):
    sms.send_sms("99866%s" % (x * 5, ), "Test message %s" % x)
