# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTaskw(PythonPackage):
    """A python API for the taskwarrior command line tool"""

    homepage = "https://github.com/ralphbean/taskw"
    pypi = "taskw/taskw-2.0.0.tar.gz"

    maintainers("taliaferro")

    license("GPL-3.0", checked_by="taliaferro")

    version("2.0.0", sha256="1109bdf9bde7a9b32a5007a302c878303ff65188b64225ac74a3289a4c548bdd")

    depends_on("py-setuptools", type="build")

    depends_on("py-pytz", type="run")
    depends_on("py-python-dateutil", type="run")
    depends_on("py-kitchen", type="run")
