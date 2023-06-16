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


def load_job_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"),
                          {"id": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return (rows[0]._asdict())
