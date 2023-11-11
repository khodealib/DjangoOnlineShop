import boto3
from django.conf import settings


class BucketManager:
    """**CDN Bucket manager**
    NOTE:
        none of these methods are async. use public interface in tasks.py modules instead.
    """

    def __init__(self):
        """init method
        create connection instance to connect S3 object storage.
        """
        session = boto3.session.Session()
        self.connection = session.client(
            service_name=settings.AWS_SERVICE_NAME,
            aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL
        )

    def get_objects(self) -> dict | None:
        """
        get all object in our bucket, if exist return dict of objects or None.
        """
        result = self.connection.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']
        return None


bucket_manager = BucketManager()
