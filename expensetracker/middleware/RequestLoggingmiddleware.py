#import request logs model that we created
from tracker.models import RequestLogs




class RequestLogging:
    #we will create constructor for responses

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_info = request
        #print(vars(request_info))
        #print(request_info.path,request_info.method)
        RequestLogs.objects.create(
            request_info = vars(request_info),
            request_type = request_info.method ,
            request_method = request_info.path 
        )
        print(self.get_response(request))

        return self.get_response(request)
    