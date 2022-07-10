import web

from service import get_current_date


urls = (
  '/', 'index',
  '/get-current-date', 'get_time',
  '/add-volunteer', 'insert_volunteer'
)


class index:
    def GET(self):
        return "Hello, world!"


class get_time:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return get_current_date()


class insert_volunteer:
    def POST(self):
        web.header('Content-Type', 'application/json')
        input_body = web.data().decode()
        print(input_body)
        web.header('Company', 'Diversify')
        return input_body


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
