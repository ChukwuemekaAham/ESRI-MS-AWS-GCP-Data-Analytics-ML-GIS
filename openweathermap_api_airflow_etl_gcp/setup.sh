sudo apt-get update
sudo apt install python3-pip
sudo apt install python3.10-venv
python3 -m venv airflow_env
source airflow_env/bin/activate
sudo pip install apache-airflow
sudo pip install pandas 
sudo pip install gcsfs
sudo pip install s3fs
