"""Setup for iframe XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='smowlcamera-id-xblock',
    version='73.1',
    description='SMOWL CAMERA',
    packages=[
        'smowlcamera',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'smowlcamera = smowlcamera:IframeWithAnonymousIDXBlock',
        ],
        "lms.djangoapp": [
            "smowlcamera = smowlcamera.apps:SmowlCameraConfig",
        ],
        "cms.djangoapp": [
            "smowlcamera = smowlcamera.apps:SmowlCameraConfig",
        ]
    },
    package_data=package_data(
        "smowlcamera", ["static", "templates", "public"]),
)
