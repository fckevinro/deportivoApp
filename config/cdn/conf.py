AWS_ACCESS_KEY_ID = 'DO00DMTACREW3MQFDLRP'
AWS_SECRET_ACCESS_KEY ='oFuy0eoiX/IL64rzXqe9YAxNZxmZlxalV6Suq1aEEak'
AWS_STORAGE_BUCKET_NAME = 'deportivo'
AWS_S3_ENDPOINT_URL ='https://nyc3.digitaloceanspaces.com'

AWS_S3_OBJECTS_PARAMETERS = {
    "CacheControl": "max-age=86400"
}
AWS_LOCATION = 'https://deportivo.nyc3.digitaloceanspaces.com'


DEFAULT_FILE_STORAGE = "config.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE= "config.cdn.backends.StaticRootS3Boto3Storage"

