#!/usr/bin/env python

from setuptools import find_namespace_packages, setup

package_name = "soda-core-redshift"
package_version = "3.5.5"
description = "Soda Core Redshift Package"

requires = [f"soda-core=={package_version}", "boto3", "psycopg2-binary>=2.8.5, <3.0"]
# TODO Fix the params
setup(
    name=package_name,
    version=package_version,
    install_requires=requires,
    packages=find_namespace_packages(include=["soda*"]),
)
