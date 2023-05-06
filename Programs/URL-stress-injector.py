import os
import stressinjector as injector


if __name__ == '__main__':
    injector.URLStress(url='http://0.0.0.0:5002/')  # Stress test GET calls

    # Stress test POST calls, also supports PUT, and DELETE
    sample_data = {'headers': {'Authorization': 'Bearer %s' % os.environ.get('TOKEN')}}
    injector.URLStress(
      url='http://0.0.0.0:5002/',
      request_type=injector.RequestType.post,
      **sample_data
    )
