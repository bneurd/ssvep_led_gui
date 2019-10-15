from tornado import template
import tornado.ioloop
import tornado.web
import json
from datetime import datetime


class MyFormHandler(tornado.web.RequestHandler):
    
    def get(self, loc):
        if loc == 'gui':
            self.render("base.html", message=None)
        else:
            config_file = open('config.json')
            res = json.loads(config_file.read())
            config_file.close()
            self.write(res)
    
    def post(self, loc):
        text = self.get_body_argument("config")
        with open('config.json', 'w') as outfile:
            json.dump(text, outfile)
        now = datetime.now()
        self.render("base.html",
                    message="Updated at {}".format(now.strftime("%H:%M:%S")))


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/(esp32)", MyFormHandler),
        (r"/(gui)", MyFormHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path': '.',
            'default_filename': 'config.json'}),
    ], autoreload=True, static_hash_cache=False)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

