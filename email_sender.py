from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

# Uncomment below lines to configure API key authorization using: partner-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['partner-key'] = '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'

# create an instance of the API class
api_instance = sib_api_v3_sdk.SMTPApi(sib_api_v3_sdk.ApiClient(configuration))
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=[{"email":"bonjou@yopmail.com","name":"John Doe"}], template_id=56, params={"name": "John", "surname": "Doe"}, headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email

try:
    # Send a transactional email
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)