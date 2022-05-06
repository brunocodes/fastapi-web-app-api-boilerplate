##############################################
###########         venv           ###########
##  Activate Terminal  ##

# PowerShell Setup #
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\Activate.ps1 (Windows PowerShell)
deactivate

# Windows CMD #
python -m venv venv (Windows)
venv\Scripts\activate.bat (Windows CMD)

source ./venv/bin/activate (Linux)

# Install #
pip install -r requirements.txt

# Freeze #
pip freeze > requirements-win10-v1.txt

##############################################
###########        uvicorn         ###########

# Run App #
uvicorn main:app --reload
uvicorn app.main:app --reload

uvicorn --host 0.0.0.0 app.main:app (Run server)
##############################################
##############################################

##############################################
###########        Alembic         ###########
# Alembic Commands #
- Init
alembic init alembic

- import Base & Config - \alembic\env.py

from app.models import Base
from app.config import settings
config.set_main_option("sqlalchemy.url", f'postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}')
target_metadata = Base.metadata

- alembic.ini Config
Deleted link

- Revision
alembic revision -m "Create Initial Tables"
alembic revision --autogenerate -m "First Auto"

- Upgrade
alembic upgrade <#revision/head/+1 || +2>

- Downgrade
alembic downgrade <#revision/-1 || -2/>

____
alembic current
alembic heads
alembic history

##############################################
#######    Add New Linux System User   #######

##############################################
###########     Env Variables      ###########

touch .env
past env's and save
set -o allexport; source /home/<UserName>/.env; set +o allexport
past command at end of .profile 

##############################################
#######   Creating a Systemd service   #######

cd /etc/systemd/system/

- Create File
sudo vi <service name>.service
past config perams

systemctl start <service name>
systemctl restart <service name>

systemctl status <service name>
sudo systemctl enable <service name>

##############################################
###########       Gunicorn         ###########

gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000

##############################################
###########        nginx           ###########
sudo apt install nginx -y
systemctl start nginx

server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _; # replace with specific domain name like sanjeev.com
        
        location / {
                proxy_pass http://localhost:8000;
                proxy_http_version 1.1;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection 'upgrade';
                proxy_set_header Host $http_host;
                proxy_set_header X-NginX-Proxy true;
                proxy_redirect off;
        }

}

- Domain


##############################################
###########       certbot          ###########

https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal

##############################################
###########        Firewall        ###########
sudo ufw status

sudo ufw allow http
sudo ufw allow https
sudo ufw allow ssh
sudo ufw allow 5432    (Open Postgresql) 

##############################################
###########  Initial Installation  ###########

# Set up venv #

python3 -m venv venv (Linux)
source ./venv/bin/activate (Linux)

pip install wheel (Linux)
pip install "fastapi[all]"
pip install SQLAlchemy
pip install psycopg2-binary(Linux) - psycopg2
pip install alembic
pip install "passlib[bcrypt]"
pip install pytest
pip install "python-jose[cryptography]"
pip install httptools
pip install gunicorn
pip install httpx

pip install uvloop (Linux Only)



##############################################
##############################################