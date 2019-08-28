import uuid
import time
import config

def generate_key(key_obj):

    timestamp = int(time.time())

    uuid_domain = str(timestamp) + str(key_obj["application_id"]) + str(key_obj["user_id"]) + config.BaseConfig.SECRET_KEY

    return str(uuid.uuid3(uuid.NAMESPACE_DNS, uuid_domain))