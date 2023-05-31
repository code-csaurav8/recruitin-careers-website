from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()

    jobs_dict = []

    for row in result.all():
      jobs_dict.append(dict(zip(column_names, row)))
    return jobs_dict

  # result = conn.execute(text("select * from jobs"))
  # result_dicts = []
  # for row in result.all():
  #   result_dicts.append(dict[row])


# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs"))
#     rows = []
#     for row in result.all():
#       rows.append(row._mapping)
