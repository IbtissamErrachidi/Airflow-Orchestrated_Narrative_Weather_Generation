import redis

# Initialize Redis client once
r = redis.Redis(host='airflow_weather-redis-1', port=6379, db=0)
#r = redis.Redis(host='localhost', port=6379, db=0) for local testing


CACHE_DURATION = 15 * 60  # 15 minutes TTL
