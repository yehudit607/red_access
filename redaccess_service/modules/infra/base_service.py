from functools import wraps
from unittest.mock import MagicMock

from modules.infra.logger import get_session_logger

logger = get_session_logger()


class BaseService:
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if attr is not callable or isinstance(attr, MagicMock):
            return attr

        @wraps(name)
        def wrapped_function(*args, **kwargs):
            # future use:
            # 1. check permissions
            # 2. check function execution time
            # 3. send signals
            # 4. metrics
            try:
                result = attr(*args, **kwargs)
                return result
            except Exception as e:
                class_name = type(self).__name__
                method_name = attr.__name__
                e = self.exception_handler(e)
                logger.exception(
                    "collection call exception",
                    e,
                    extra={
                        "collection": class_name,
                        "method": method_name,
                        "arguments": args,
                    },
                )
                raise e

        return wrapped_function

    def exception_handler(self, e):
        return e
