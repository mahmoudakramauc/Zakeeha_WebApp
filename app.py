from flask import Flask, render_template
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

deroos = {'active':[
                 {'scholar_name': 'alhabib',
                  'sex': 'm',
                  'topic': 'tazkeya',
                  'location': 'https://goo.gl/maps/zj7RqYZAcqk',
                  'schedule':
                                {'weekly_or_monthly': 'w',
                                 'week_day': 'Mon',
                                 'am_pm': 'PM',
                                 'start_time': '9:00',
                                 'end_time' : '10:00'
                                }
                  },
                 {'scholar_name': 'mo3ez mas3ood',
                  'sex': 'm',
                  'topic': 'tazkeya',
                  'location': 'https://goo.gl/maps/zj7RqYZAcqk',
                  'schedule':
                                {'weekly_or_monthly': 'm',
                                 'week_day': 'Tue',
                                 'am_pm': 'AM',
                                 'start_time': '9:00',
                                 'end_time' : '10:00'
                                }
                  }],

          'inactive':[
                  {'scholar_name': 'amr werdany',
                  'sex': 'm',
                  'topic': 'fiqh',
                  'location': 'https://goo.gl/maps/zj7RqYZAcqk',
                  'schedule':
                                {'weekly_or_monthly': 'm',
                                 'week_day': 'Tue',
                                 'am_pm': 'AM',
                                 'start_time': '9:00',
                                 'end_time' : '10:00'
                                }
                  }]
        }

@app.route('/')
def home():
    return render_template('index.html')

      # return 'zakeeha API v1.0 - This is an attempt to collect information around available/active\n'\
      # 'islamic sessions/seminars and serve them in a RESTful API available for consumption by anyone for free.\n\n'\
      # 'The following is a list of available GET endpoints (so far):\n'\
      # '- /all_deroos (returns all available lists of deroos whether active or not\n'\
      # '- /active_deroos (returns a list of active deroos only\n'\
      # '- /inactive_deroos (return a list of inactive deroos only\n'\
      # '- /scholar_names (retruns a list of names for all available scholars\n'\
      # '- /all_deroos/<scholar_name> returns a list of all deroos by scholar_name'

class all_deroos(Resource):
    def get(self):
        return deroos

class active_deroos(Resource):
    def get(self):
        return deroos['active']

class inactive_deroos(Resource):
    def get(self):
        return deroos['inactive']

class scholar_names(Resource):
    def get(self):
        scholar_names = []
        for dars in (deroos['active'] + deroos['inactive']):
                if dars['scholar_name'] not in scholar_names:
                        scholar_names.append(dars['scholar_name'])

        return scholar_names

class deroos_by_scholar_name(Resource):
    def get(self, scholar_name):
        if scholar_name not in scholar_names.get(self):
            abort(404, message="Scholar {} doesn't exist".format(scholar_name))

        deroos_by_scholar_name = []
        for dars in (deroos['active'] + deroos['inactive']):
            if dars['scholar_name'] == scholar_name:
                deroos_by_scholar_name.append(dars)

        return deroos_by_scholar_name


#api.add_resource(welcome, '/')
api.add_resource(all_deroos, '/all_deroos')
api.add_resource(active_deroos, '/active_deroos')
api.add_resource(inactive_deroos, '/inactive_deroos')
api.add_resource(scholar_names, '/scholar_names')
api.add_resource(deroos_by_scholar_name, '/all_deroos/<scholar_name>')


if __name__ == '__main__':
    app.run(debug=True)