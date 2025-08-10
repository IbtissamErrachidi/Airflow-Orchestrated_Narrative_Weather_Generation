import redis

# Initialize Redis client once
r = redis.Redis(host='localhost', port=6379, db=0)

CACHE_DURATION = 15 * 60  # 15 minutes TTL
