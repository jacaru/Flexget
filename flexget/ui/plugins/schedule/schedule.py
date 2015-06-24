from __future__ import unicode_literals, division, absolute_import

from flexget.ui import register_plugin, register_js, Blueprint, register_menu

schedule = Blueprint('schedule', __name__)
register_plugin(schedule)

schedule.register_angular_route(
    'schedules',
    url=schedule.url_prefix,
    template_url='index.html',
    controller='SchedulesCtrl',
)

register_js('schedules', 'js/schedules.js', bp=schedule)

register_menu(schedule.url_prefix, 'Schedule', icon='fa fa-calendar')
