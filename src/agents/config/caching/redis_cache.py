# Use Redis as cache

with Cache.redis(redis_url="redis://localhost:6379/0") as cache:
    user.initiate_chat(assistant, message=coding_task, cache=cache)