# python-cloud-foundry-watson

## login
cf api https://api.ng.bluemix.net
cf login

## create app
cf push --no-start
cf bs myapp "Tone Analyzer-qs"
cf env myapp
export VCAP_SERVICES='JSON'

## ssh
https://docs.cloudfoundry.org/devguide/deploy-apps/ssh-apps.html
cf ssh MY-AWESOME-APP -i 2

## test webservice
curl -H "Content-Type: application/json" -X POST localhost:9099/tone -d '{"text": "funny happy joy love"}'

## links
http://www.textfixer.com/tools/remove-line-breaks.php
https://www.ibm.com/watson/developercloud/doc/index.html
