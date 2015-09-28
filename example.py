import tornado.ioloop
import tornado_dns


def main():
    io_loop = tornado.ioloop.IOLoop.instance()

    def success(addresses):
        print 'addresses: %s' % (addresses,)
        io_loop.stop()

    def errback(code):
        print tornado_dns.errors.describe(code)
        io_loop.stop()

    # use DNS compression pointer mutation
    # for more info goto https://gist.github.com/klzgrad/f124065c0616022b65e5
    # use  use_compress=True enable it ~
    tornado_dns.lookup("www.facebook.com", success, errback, timeout=5000, server="8.8.8.8", use_compress=True)
    io_loop.start()


if __name__ == '__main__':
    main()
