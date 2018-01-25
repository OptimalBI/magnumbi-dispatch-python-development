import unittest
import magnumbi_depot


class MicroservicesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app_id = 'AUTOTEST',
        cls.client = magnumbi_depot.DispatchClient(
            uri='https://localhost',
            access_key='test',
            secret_key='token',
            port=6883,
            ssl_verify=False
        )

    def test_status_check(self):
        self.assertTrue(self.client.check_status())


if __name__ == '__main__':
    unittest.main()
