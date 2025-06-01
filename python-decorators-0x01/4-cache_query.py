import sqlite3
import functools

# Global cache dictionary
query_cache = {}

# Decorator to manage DB connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator to cache query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("Fetching from cache...")
            return query_cache[query]
        print("Executing and caching query...")
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call caches the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call retrieves result from cache
users_again = fetch_users_with_cache(query="SELECT * FROM users")

print(users_again)
