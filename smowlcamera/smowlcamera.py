"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import requests
import string
import sys

from django.contrib.auth.models import User
from django.conf import settings as DJANGO_SETTINGS
from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean, Dict, Float, List, Set, Field, ScopeIds
from xblock.fragment import Fragment

from django.utils.translation import ugettext as _
from django.template import Context, Template

from .utils import render_template, xblock_field_list
from openedx.core.djangoapps.site_configuration.models import SiteConfiguration

from mock import patch, MagicMock, Mock
from xblock.field_data import FieldData, DictFieldData
from xblock.runtime import Runtime

import logging
log = logging.getLogger(__name__)


class SmowlCameraXblock(XBlock):
    """
    XBlock displaying an iframe, with an anonymous ID passed in argument
    """

    # Fields are defined on the class. You can access them in your code as
    # self.<fieldname>.

    # URL format :
    # {iframe_url}/UserID
    NombreEntidad = ""

    display_name = String(
        help=_("SMOWL"),
        display_name=_("Component Display Name"),
        # name that appears in advanced settings studio menu
        default=_("SMOWL CAMERA"),
        scope=Scope.user_state
    )

    smowlcamera_url = String(
        display_name=_("SMOWL ACTIVATED"),
        help=_("PUBLISH to activate SMOWL"),
        default="",
        scope=Scope.settings
    )

    has_author_view = True

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def author_view(self, context=None):
        # Sacamos la entidad solo
        entityName11 = self.course_id.org
        context = {
                'has_settings': False
            }
        if self.check_settings():
            context['has_settings'] = True
            settings = {
                'course_id': str(self.course_id),
                'NombreEntidad': DJANGO_SETTINGS.SMOWL_ENTITY,
                'swlLicenseKey': DJANGO_SETTINGS.SMOWL_KEY,
                'InsertEDXPOST_URL': DJANGO_SETTINGS.SMOWLCAMERA_INSERTEDXPOST_URL,
                'parent': self.parent,
                'has_settings': True
            }
        else:
            lms_base = SiteConfiguration.get_value_for_org(
                self.location.org,
                "LMS_BASE",
                DJANGO_SETTINGS.LMS_BASE
            )
            context['help_url'] = 'https://{}/{}'.format(lms_base, 'contact_form')
            settings = {
                'has_settings': False
            }
        frag = Fragment()
        frag.add_content(render_template(
            '/templates/html/smowlcamera-author.html', context))
        frag.add_css(self.resource_string("static/css/smowlcamera.css"))
        frag.add_javascript(self.resource_string(
            "static/js/src/smowlcamera-author.js"))
        frag.initialize_js('SmowlCameraXblock', json_args=settings)
        return frag


    def student_view(self, context=None):
        """
        The primary view of the SMOWLCAMERA, shown to students
        when viewing courses.
        """

        #runtime = TestRuntime(services={'field-data': DictFieldData({})})
        #block = SmowlCameraXblock(runtime, scope_ids=Mock(spec=ScopeIds))
        #parent = block.get_parent()

        #url_response = self.request.GET

        # student es la id del curso y sirve pa saber si es admin
        student_id = self.xmodule_runtime.anonymous_student_id
        user_id = self.scope_ids.user_id

        # Sacamos la entidad solo
        containerCurso = self.course_id
        entityName11 = self.course_id.org

        #usageID =  self.scope_ids.usage_id

        # usage es el codigo del curso mejor asi
        #usage5555 = self.scope_ids.usage_id

        idUnit2 = self.parent
        idUnit = str(idUnit2).split("@")[-1]
        #idUnit5 = "{0}".format(idUnit)

        # Datos personales del alumno como el username
        #user = User.objects.get(id=self.scope_ids.user_id)
        #m = user.username
        context = {
                'has_settings': False
            }
        if self.check_settings():
            context['has_settings'] = True
            # new_smowlcamera_url = "{0}={1}&course_CourseName={2}".format(self.smowlcamera_url, student_id, course_id)
            new_smowlcamera_url = "{0}={1}&course_Container={2}&course_CourseName={3}&entity_Name={4}".format(
                DJANGO_SETTINGS.SMOWLCAMERA_FULL_URL, user_id, containerCurso, idUnit, DJANGO_SETTINGS.SMOWL_ENTITY)

            settings = {
                'smowlcamera_url': new_smowlcamera_url,
                'has_settings': True
            }
        else:
            settings = {
                'has_settings': False
            }
        
        frag = Fragment()
        frag.add_content(render_template(
            '/templates/html/smowlcamera.html', context))
        frag.add_css(self.resource_string("static/css/smowlcamera.css"))
        frag.add_javascript(self.resource_string(
            "static/js/src/smowlcamera.js"))
        frag.initialize_js('SmowlCameraXblock', json_args=settings)
        return frag

    def studio_view(self, context=None):
        """
        The studio view of the SMOWLCAMERA, with form
        """
        frag = Fragment()
        frag.add_content(render_template(
            '/templates/html/smowlcamera-edit.html'))
        frag.add_javascript(self.resource_string(
            "static/js/src/smowlcamera-edit.js"))
        frag.initialize_js('SmowlCameraXblock')
        return frag

    def check_settings(self):
        return (
            hasattr(DJANGO_SETTINGS, 'SMOWLCAMERA_BASE_URL') and 
            hasattr(DJANGO_SETTINGS, 'SMOWL_KEY') and 
            hasattr(DJANGO_SETTINGS, 'SMOWLCAMERA_FULL_URL') and 
            hasattr(DJANGO_SETTINGS, 'SMOWL_ENTITY') and 
            hasattr(DJANGO_SETTINGS, 'SMOWLCAMERA_INSERTEDXPOST_URL')
            )

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("SmowlCameraXblock",
             """
			 """),
        ]
