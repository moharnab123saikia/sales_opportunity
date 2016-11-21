from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder.charts.views import DirectByChartView
from flask_appbuilder.views import ModelView
from app import appbuilder, db
from models import Sentiment

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


class SentimentModelView(ModelView):
    datamodel = SQLAInterface(Sentiment)

class SentimentModelChartView(DirectByChartView):
    datamodel = SQLAInterface(Sentiment)
    chart_title = "feature sentiments"
    # base_filters = "iphone"
    definitions = [
    {
        'label': 'battery sentiment',
        'group': 'phone',
        'series': ['camera']
    }
]

db.create_all()

appbuilder.add_view(SentimentModelView, "List Sentiments", icon="fa-folder-open-o", category="Statistics")
appbuilder.add_view(SentimentModelChartView, "List Sentiment Chart", icon="fa-folder-open-o", category="Statistics")
