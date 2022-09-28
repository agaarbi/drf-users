import redis
import time

r0 = redis.Redis(
    host='localhost',
    port='6379',
    db=0)


def save_token(token, user_id, ttl=180):
    return r0.set(token, user_id, ttl)


def check_token(token):
    return r0.get(token)


def delete_token(token):
    return r0.delete(token)


print(save_token("1a", 1))
print(check_token("1a"))
time.sleep(2)
print(check_token("1a"))
print(delete_token("1a"))
print(check_token("1a"))

# r0.set("name", "ghani")
# r0.mset({"age": 23, "gender": "male"})

# print(r0.get("name"))
# print(r0.get("age"))
# print(r0.get("gender"))

# if (r0.exists("name")):
#     print(r0.get("name"))
# else:
#     print("name key does not exists")

# r0.psetex("name_temp", 1000, "abdul")

# print(r0.get("name_temp"))
# time.sleep(2)
# print(r0.get("name_temp"))

# r0.delete("user_1")
# print(r0.lpush("user_1", "hello1"))
# print(r0.lpush("user_1", "hello2"))
# print(r0.lpush("user_1", "hello3"))
# print(r0.lpush("user_1", "hello4"))
# print(r0.lpush("user_1", "hello5"))

# print(r0.lpop("user_1"))
# print(r0.lpop("user_1"))
# print(r0.lpop("user_1"))
# print(r0.lpop("user_1"))
# print(r0.lpop("user_1"))


# r0.delete("work:queue:ids")
# r0.delete("work:queue:name")
# r0.lpush("work:queue:ids", 101)
# r0.lpush("work:queue:name", "hi")
