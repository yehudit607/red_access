import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379
DB = 0
CHARSET = "utf-8"
DECODE_RESPONSE = True

class RedisWords:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = redis.StrictRedis(
                host=REDIS_HOST,
                port=REDIS_PORT,
                db=DB,
                charset=CHARSET,
                decode_responses=DECODE_RESPONSE,
            )
        return cls.instance

    def set_malicious_words(self, words):
        self.instance.set("malicious_words", words)

    def get_malicious_words(self):
        return self.instance.get("malicious_words")

    def set_version(self, version):
        self.instance.set("version", version)

    def get_version(self):
        return self.instance.get("version")
