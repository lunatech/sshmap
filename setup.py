#!/usr/bin/env python
import os
from setuptools import setup
"""
 Copyright (c) 2010 Yahoo! Inc. All rights reserved.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License. See accompanying LICENSE file.
"""

setup(
  name="sshmap",
  version="0.2.0",
  author="Dwight Hubbard",
  author_email="dhubbard@yahoo-inc.com",
  url="http://www.yahoo.com",
  license="LICENSE.txt",
  packages=["sshmap"],
  scripts=["sshmap"],
  long_description=open('README.txt').read(),
  description="A SSH Multiplexer desgined to use ssh to perform map/reduce like operations",
  requires=['paramiko'],
)
