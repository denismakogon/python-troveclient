#   Copyright 2011 OpenStack Foundation
#   Copyright 2013 Mirantis, Inc.
#   All Rights Reserved.
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

from troveclient import base
#from troveclient.openstack.common.apiclient import exceptions


class DBLog(base.Resource):
    """
    Backup is a resource used to hold backup information.
    """

    def __repr__(self):
        return "<DBLog: %s>" % self.name


class DBLogs(base.ManagerWithFind):

    resource_class = DBLog

    def create(self, name, instance):
        """
        Create a new backup from the given instance.
        """
        body = {
            "dblog": {
                "file": name,
                "instance": instance
            }
        }
        return self._create("/dblog", body, "dblog")

    def list(self, limit=None, marker=None):
        """
        Get a list of all logs files per datastore.

        :rtype: list of :class:`DBLogs`.
        """
        return self._list("/dblogs",
                          "dblogs", limit, marker)

    def get(self, datastore):
        """
        Get a list of log file for specific datastore.

        :rtype: :class:`DBLog`
        """
        return self._get("/dblogs/%s" % base.getid(datastore),
                         "dblog")
