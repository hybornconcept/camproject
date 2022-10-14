import streamlit as st  # pip install streamlit
from deta import Deta

DETA_KEY = "a0336p7l_CroTiVtomMBEP96auViVaMgZeyVjX56U"

deta = Deta(DETA_KEY)


db2 = deta.Base("country_db")


def insert_driver(timestamp, ip, location2, hotspots):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db2.put({"key": timestamp, "ip": ip,  "hotspots": location2, "result": hotspots})
