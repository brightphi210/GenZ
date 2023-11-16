import os
from supabase import create_client

SUPABASE_BUCKET = "images"

supabase_url = 'https://xknvvscpnjlstbotsslz.supabase.co'

supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhrbnZ2c2Nwbmpsc3Rib3Rzc2x6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDAxNjgwODMsImV4cCI6MjAxNTc0NDA4M30.f4sD37t8-icaQSfJGzI7NA0XzhZj33I3piH1plG4RFU'

supabase = create_client(supabase_url, supabase_key)