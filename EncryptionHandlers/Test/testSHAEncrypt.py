import unittest
from EncryptionHandlers.SHAHandler import GetSHAEncryption

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.handler = GetSHAEncryption()

    def testSHA132(self):
        message = "hello"
        expectedresult = "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"
        result = self.handler.sha1Handler(message)
        self.assertEqual(result, expectedresult)

    def testSHA224(self):
        message = "hello"
        expectedresult = "ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193"
        result = self.handler.sha224Handler(message)
        self.assertEqual(result, expectedresult)

    def testSHA256(self):
        message = "hello"
        expectedresult = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        result = self.handler.sha256Handler(message)
        self.assertEqual(result, expectedresult)

    def testSHA384(self):
        message = "hello"
        expectedresult = "59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f"
        result = self.handler.sha384Handler(message)
        self.assertEqual(result, expectedresult)

    def testSHA512(self):
        message = "hello"
        expectedresult = "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043"
        result = self.handler.sha512Handler(message)
        self.assertEqual(result, expectedresult)

if __name__ == '__main__':
    unittest.main()
