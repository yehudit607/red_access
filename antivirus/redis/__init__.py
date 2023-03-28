import redis


class RedisWords:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = redis.StrictRedis(
                host="localhost",
                port=6379,
                db=0,
                charset="utf-8",
                decode_responses=True,
            )
        return cls.instance

