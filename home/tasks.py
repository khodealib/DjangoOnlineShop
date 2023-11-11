from utils.bucket import bucket_manager


def all_bucket_objects_task():
    buckets = bucket_manager.get_objects()
    return buckets
