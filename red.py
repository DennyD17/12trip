# coding=utf-8
import string
import random
import redis
from time import sleep

class RedisHandler(object):
    def __init__(self):
        self.is_generator = False
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.pipe = self.redis.pipeline()
        self.message = ''

    def send_message(self):
        self.message = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _
                               in range(10))
        self.pipe.multi()
        self.pipe.setex('generator', 10, 'here')
        self.pipe.set('message', self.message)
        self.pipe.execute()

    def get_message(self):
        self.pipe.multi()
        self.pipe.get('message')
        self.pipe.delete('message')
        result = self.pipe.execute()
        if result[0]:
            self.message = result[0]
        return result[0]

    def add_message_to_error_list(self):
        if random.randint(0, 100) < 6:
            self.redis.lpush('error_list', self.message)

    def become_of_generator(self):
        if not self.redis.get('generator'):
            self.send_message()
            self.is_generator = True


if __name__ == '__main__':
    r = RedisHandler()
    while 1 == 1:
        if r.is_generator:
            r.send_message()
            sleep(5)
        else:
            if r.get_message():
                r.add_message_to_error_list()
            r.become_of_generator()
            sleep(5)




