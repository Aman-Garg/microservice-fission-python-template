# create fission env
	fission environment create --name python --image fission/python-env 
# create get function & route
	fission function create --name python-add-get --env python --code python-add-get.py
	fission route create --method GET --url /python-add-get --function python-add-get --createingress
# test get
	curl -X GET \
	  'https://fission.lingkcore.com/python-add-get?number1=10&number2=10' 
# create post function & route
	fission function create --name python-add-post --env python --code python-add-post.py
	fission route create --method POST --url /python-add-post --function python-add-post --createingress
# test post
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
	

