from raas_v2.raasv2_client import *

platform_name = "QAPlatform2" # RaaS v2 API Platform Name
platform_key = "apYPfT6HNONpDRUj3CLGWYt7gvIHONpDRUYPfT6Hj" # RaaS v2 API Platform Key

client = RaaSV2Client(platform_name, platform_key)

accounts_client = client.accounts

result = accounts_client.get_all_accounts()

print result