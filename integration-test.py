import os
import requests;
import unittest
from requests.models import Response;
from sqlalchemy import create_engine;

class Integrationtest(unittest.TestCase ):

    URI = 'postgresql://cs162_user:cs162_password@localhost/cs162'

    def test_valid_expression(self):
        r = requests.post('http://localhost:5000/add', data={'expression':'5+5'})
        self.assertEqual(r.status_code, 200)

    def test_invalid_expression(self):
        r = requests.post('http://localhost:5000/add', data = {'expression': '5--'})
        self.assertNotEqual(r.status_code, 200)

    """
    URI = 'postgresql://cs162_user:cs162_password@localhost/cs162'
    metadata = MetaData()
    engine = create_engine(URI)
    Expression = Table('expression', metadata, autoload=True, autoload_with=engine)
    Session = sessionmaker(engine)
    """

    def test_db(self):
        r = requests.post('http://localhost:5000/add', data={'expression':'100+100'})
        engine = create_engine('postgresql://cs162_user:cs162_password@localhost:8080/cs162', echo = True)

        with engine.connect() as con:
            rs = con.execute("SELECT * FROM Expression WHERE text = '1+1'")
            rows = rs.fetchall()

        self.assertNotEqual(len(rows), 1)

if __name__ == "__main__":
    unittest.main()