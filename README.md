##Deploy instructions

If no virtualenv exists, first create one:
`$ cd [PROJECT_DIR]`
`$ virtualenv env`

Activate the virtualenv
`$ source env/bin/activate`

Install requirements
`$ pip install -t lib -r requirements.txt`

Test locally
`$ dev_appserver.py app.yaml`

Now deploy to google cloud
`$ gcloud app deploy app.yaml`