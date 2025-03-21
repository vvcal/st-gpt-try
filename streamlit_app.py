import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# Load credentials from secrets
credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp"])

# Initialize BigQuery client
client = bigquery.Client(credentials=credentials)

st.write("✅ Successfully connected to BigQuery!")
