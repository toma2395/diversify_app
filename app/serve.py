import web
import json

from service import get_current_date, get_all_volunteers, create_volunteer, get_one_volunteer_by_id


urls = (
  '/', 'index',
  '/get-current-date', 'get_time',
  '/volunteer', 'volunteer',
  '/volunteer/(.+)', 'volunteer_listing'
)


class index:
    def GET(self):
        return "Hello, world!"


class get_time:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return get_current_date()


class volunteer:
    def POST(self):
        web.header('Content-Type', 'application/json')
        input_body = web.data().decode()
        print(input_body)
        web.header('Company', 'Diversify')
        data = json.loads(input_body)
        try:
            response = create_volunteer(data['name'], data['surname'], data['city'], data['country'])
        except KeyError:
            web.badrequest()
            return json.dumps({"error_message": "wrong body"})
        web.created()
        return response

    def GET(self):
        web.header('Content-Type', 'application/json')
        return get_all_volunteers()


class volunteer_listing:
    def GET(self, user_id):
        web.header('Content-Type', 'application/json')
        return get_one_volunteer_by_id(user_id)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
