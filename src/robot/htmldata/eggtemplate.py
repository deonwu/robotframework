#  Copyright 2008-2015 Nokia Solutions and Networks
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from os.path import abspath, dirname, join, normpath

import pkg_resources

class HtmlTemplate(object):

    def __init__(self, filename):
        #print("f:%s" % filename)
        filename = filename.replace("rebot/../", "")
        self._path = filename

    def __iter__(self):
        data = pkg_resources.resource_string("robot.htmldata", self._path)  
        for line in data.split("\n"):
            yield line.rstrip()
