from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from flask import Blueprint, Response

VIEWS_BLUEPRINT = Blueprint('{{cookiecutter.project_slug}}', '{{cookiecutter.project_slug}}.views')


@VIEWS_BLUEPRINT.route('/status', methods=['GET'])
def status():
    status_dict = {
        'status': 'ok',
        'components': {
            # if you have anything else you wish to validate is running place it here
        }
    }
    return Response(json.dumps(status_dict), status=200, content_type='application/json')
