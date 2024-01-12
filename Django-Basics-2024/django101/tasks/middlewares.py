# it executes before view and after view
import time


#  Register in settings - MIDDLEWARE

def measure_time(get_response):
    def middleware(request, *args, **kwargs):
        print('Before view')
        start_time = time.time()
        result = get_response(request, *args, **kwargs)
        time.sleep(2.5)
        print('After view')
        end_time = time.time()

        print(f'Request took {end_time - start_time} sec')

        return result

    return middleware
