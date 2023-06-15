import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result:
      jobs.append(row._asdict())
  return (jobs)
