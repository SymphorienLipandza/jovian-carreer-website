from sqlalchemy import create_engine,text
import sqlalchemy

db_connection_string="mysql+pymysql://hvslemvpkocef897bqa0:pscale_pw_jibsEUoohqH6V3haw7YP1OylaAFG29dkMXffXd6oef3@us-west.connect.psdb.cloud/ecolinkcareers?charset=utf8mb4"

engine=create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca":"/etc/ssl/cert.pem"
    }
  }
)

def load_jobs_from_db():
  with engine.connect() as conn: 
    result = conn.execute(text("select * from jobs"))
    jobs=[]
    for  row in result.all():
      jobs.append(row._asdict())
    return jobs

print(sqlalchemy.__version__)

