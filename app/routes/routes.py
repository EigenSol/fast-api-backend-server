async def welcome_function(request):
    return "Wellcome Api  is Running"
async def add_product_function(request):
    return [{"id" : 1 , "name": "Product 1"} , {"id" : 2 , "name": "Product 2"}]
async def get_product_function(request):
    return {"id": 1, "name": "Product 1"}
async def delete_product_function(request):
    return {"message": "Product deleted successfully"}
async def update_product_function(request):
    return {"message": "Product updated successfully"}

async def records(req):
    # get count 
    count = req.query_parm.get('count')
    if not count : return "sending all records...."
    return f"sunding {count} records only."



routes =  [
    { 'method': 'Get', 'path': '/welcome', 'handler' : welcome_function },
    { 'method': 'Get', 'path': '/products', 'handler' : add_product_function },
    { 'method': 'Get', 'path': '/products/{id}', 'handler' : get_product_function },
    { 'method': 'Delete', 'path': '/products/{id}', 'handler' : delete_product_function },
    { 'method': 'Put', 'path': '/products/{id}', 'handler' : update_product_function },
    { 'method': 'GET', 'path': '/records', 'handler': records  },

]