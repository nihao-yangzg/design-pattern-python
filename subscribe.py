#encoding=utf-8

###-----------------------------------------###
###            订阅模式                     ###
###       producer每生成一条消息            ###
###       consumer便自动收到该消息          ###
###-----------------------------------------###

class Producer(object):
    def __init__(self):
        self.subscribes = []
        self.message = None

    def set_message(self, message):
        self.message = message
        self.notify()
    
    def notify(self):
        for item in self.subscribes:
            item.receive_message(self.message)


class Consumer(object):
    def __init__(self):
        self.message = None

    def receive_message(self, message):
        self.message = message

    def subscribe(self, producer):
        producer.subscribes.append(self)


if __name__ == '__main__':
    producer = Producer()
    consumers = list()
    for i in xrange(5):
        consumer = Consumer()
        consumer.subscribe(producer)
        consumers.append(consumer)

    producer.set_message('hello, every one')

    for item in consumers:
        print item.message
       
