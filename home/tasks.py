from celery import shared_task

from utils.bucket import bucket_manager


@shared_task
def all_bucket_objects_task():
    buckets = bucket_manager.get_objects()
    return buckets


@shared_task
def delete_object_task(key):
    bucket_manager.delete_object(key)
