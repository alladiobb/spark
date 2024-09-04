### install [pyspark]

```shell
#root
/Users/alladiobb

#verify python
python3 --version

#install & create new env
#project [location]

pip install virtualenv
#virtualenv [nome do enviroment]
virtualenv venvSpark

#activate
source venv/bin/activate

#deactivate
deactivate

#localizar as vens
find ~/ -name "virtualenv"
#padrão ubuntu: ~/.local/share/virtualenvs

#pip install
pip install -r requirements.txt 