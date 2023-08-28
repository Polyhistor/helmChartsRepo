from minio import Minio
from urllib.parse import urlparse

def fetch_data_from_minio(distributed_storage_address, minio_access_key, minio_secret_key, bucket_name, object_name):

    # Extract the base URL from the distributed storage address
    parsed_url = urlparse(distributed_storage_address)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}" if parsed_url.scheme else parsed_url.netloc

    print(base_url)

    minio_client = Minio(
        base_url,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False
    )

    data = minio_client.get_object(bucket_name, object_name)
    data_str = ''

    for d in data.stream(32*1024):
        data_str += d.decode()

    return data_str