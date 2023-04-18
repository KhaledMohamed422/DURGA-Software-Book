from django.http import HttpResponse


class ExecutionFlowMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        print('call 1')
        print('This line added at pre-processing of request')
        response = self.get_response(request)
        print('This line added at post-processing of request')
        return response

# Middleware application to show information saying application under maintenance
class AppMaintenanceMiddleware(object): 
    def __init__(self,get_response): 
        self.get_response=get_response 
 
    def __call__(self,request): 
        print('call 2')
        return HttpResponse('<h1>Currently Application under maintenance... plz try after 2 days!!!')
    

# Middleware application to show meaningful response if view function raises any error
class ErrorMessageMiddleware(object): 
    def __init__(self,get_response): 
        self.get_response=get_response 
 
    def __call__(self,request):
        print('call 3') 
        return self.get_response(request) 
 
    def process_exception(self,request,exception): 
        return HttpResponse('<h1>Currently we are facing some technical problems plz try after some time!!!</h1>')