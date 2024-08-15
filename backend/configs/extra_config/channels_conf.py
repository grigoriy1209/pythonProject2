CHANNELS_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "host": [("redis", 6379)],
        },
    },
}
