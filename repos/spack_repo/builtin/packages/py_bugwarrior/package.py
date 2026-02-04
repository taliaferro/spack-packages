# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBugwarrior(PythonPackage):
    """a command line utility for updating your local taskwarrior database from your forge issue trackers"""

    homepage = "https://bugwarrior.readthedocs.io/en/latest/"
    pypi = "bugwarrior/bugwarrior-2.1.0.tar.gz"

    maintainers("taliaferro")

    license("GPL-3.0", checked_by="taliaferro")

    version("2.1.0", sha256="8978c2335cb5cf6fcac149b05f6528e8b6087247edeb7a55bcab75c459b24be9")

    depends_on("py-setuptools", type="build")

    depends_on("py-click", type=("run"))
    depends_on("py-dogpile-cache@0.5.3:", type=("run"))
    depends_on("py-jinja2@2.7.2:", type=("run"))
    depends_on("py-lockfile@0.9.1:", type=("run"))
    depends_on("py-pydantic@2:", type=("run"))
    depends_on("py-email-validator@2.0.0:", type=("run"))
    depends_on("py-python-dateutil", type=("run"))
    depends_on("py-requests", type=("run"))
    depends_on("py-taskw@0.8:", type=("run"))
    depends_on("py-tomli", type=("run"), when="^python@:3.10")
