import json
import logging

from django.utils import timezone


class DebugInfoFilter(logging.Filter):
    def __init__(self, param=None):
        self.param = param

    def filter(self, record):
        return record.levelname in ('DEBUG', 'INFO')


def prepare_post_data(source_post_info, extra_exclude=None) -> dict:
    if extra_exclude is None:
        extra_exclude = list()
    post_info = source_post_info.copy()
    exclude_fields = ["password", "password2"]
    exclude_fields.extend(extra_exclude)
    for field in exclude_fields:
        post_info.pop(field, None)
    return post_info


def log_record(request, logger_name, message, exclude_fields=None):
    logger = logging.getLogger(f'{logger_name}')
    post_info = prepare_post_data(request.POST, extra_exclude=exclude_fields)
    logger.info(json.dumps(
        {'timestamp': timezone.now().timestamp(), 'message': message, 'headers': request.headers.__dict__,
         'post_info': post_info}))
