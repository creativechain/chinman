import unittest
import json
import shutil

from chinman import snapshot
from simple_crea_client.client import SteemRemoteBackend, SteemInterface, SteemRPCException

class SnapshotTest(unittest.TestCase):
    def test_list_all_accounts(self):
        backend = SteemRemoteBackend(nodes=["http://test.com"], appbase=True)
        cread = SteemInterface(backend)
        self.assertIsNotNone(snapshot.list_all_accounts(cread))
