import unittest
import pytest
from app import app

class Test(unittest.TestCase):
    
    def setUp(self):
        
        app.config['TESTING']= True
        self.app = app.test_client()
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION']= False
        
    def test_login(self):
        
        response = self.app.post('/', data= dict(username="XYZ", password="admin"), follow_redirects=True)
        self.assertIn(b'@XYZ', response.data)
