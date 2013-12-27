# Copyright 2011 OpenStack Foundation
# Copyright 2013 Mirantis, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import testtools
import mock

from troveclient.v1 import dblogs
from troveclient import base


class DBLogTests(testtools.TestCase):

    def setUp(self):
        super(DBLogTests, self).setUp()
        self.orig__init = dblogs.DBLog.__init__
        dblogs.DBLog.__init__ = mock.Mock(return_value=None)
        self.dblog = dblogs.DBLog()
        self.dblog.manager = mock.Mock()

    def tearDown(self):
        super(DBLogTests, self).tearDown()
        dblogs.DBLog.__init__ = self.orig__init

    def test_repr(self):
        self.dblog.name = "dblog-1"
        self.assertEqual('<DBLog: dblog-1>',
                         self.dblog.__repr__())


class DBLogsTest(testtools.TestCase):

    def setUp(self):
        super(DBLogsTest, self).setUp()
        self.orig__init = dblogs.DBLogs.__init__
        dblogs.DBLogs.__init__ = mock.Mock(return_value=None)
        self.dblogs = dblogs.DBLogs()
        self.dblogs.api = mock.Mock()
        self.dblogs.api.client = mock.Mock()
        self.dblogs.resource_class = mock.Mock(return_value="dblog-1")

        self.orig_base_getid = base.getid
        base.getid = mock.Mock(return_value="datastore1")

    def tearDown(self):
        super(DBLogsTest, self).tearDown()
        dblogs.DBLogs.__init__ = self.orig__init
        base.getid = self.orig_base_getid

    def test_list(self):
        def side_effect_func(path, inst, limit, marker):
            return path, inst, limit, marker

        self.dblogs._list = mock.Mock(side_effect=side_effect_func)
        limit = "test-limit"
        marker = "test-marker"
        expected = ("/dblogs", "dblogs", limit, marker)
        self.assertEqual(expected, self.dblogs.list(limit, marker))

    def test_get(self):
        def side_effect_func(path, inst):
            return path, inst

        self.dblogs._get = mock.Mock(side_effect=side_effect_func)
        self.assertEqual(('/dblogs/datastore1',
                          'dblog'),
                         self.dblogs.get(1))
