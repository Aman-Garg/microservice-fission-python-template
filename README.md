# microservice-fission-python-template
## create fission env
	fission environment create --name python --image fission/python-env 
## create get function & route
	fission function create --name python-add-get --env python --code python-add-get.py
	fission route create --name python-add-get --url /python-add-get --function python-add-get --method GET --createingress
### test get
	curl -X GET \
	  'https://fission.lingkcore.com/python-add-get?number1=10&number2=10' 
# create post function & route
	fission function create --name python-add-post --env python --code python-add-post.py
	fission route create --name python-add-post --url /python-add-post --function python-add-post --method POST --createingress
### test post
	curl -X POST \
	  https://fission.lingkcore.com/python-add-post \
	  -H 'Content-Type: application/json' \
	  -d '{
	  "numbers": [
	  	{ 
	      "number": 1
	    },
	    {
	      "number": 2
	    }
	  ]
	}'


### helpers
	find . -type f -print0 | xargs -0 dos2unix
	

