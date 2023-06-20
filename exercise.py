import logging

logging.basicConfig(filename='my.log', encoding='utf-8', level=logging.DEBUG)

logging.debug('문제를 진단합니다.') # DEBUG:root:문제를 진단합니다.
logging.info('예상대로 작동합니다.') # INFO:root:예상대로 작동합니다.
logging.warning('미래에는 문제가 될 수도 있습니다.') # WARNING:root:미래에는 문제가 될 수도 있습니다.
logging.error('에러로 인해 일부 기능이 제대로 작동되지 않을 수 있습니다.') # ERROR:root:에러로 인해 일부 기능이 제대로 작동되지 않을 수 있습니다.
logging.critical('심각한 에러로 인해 프로그램이 종료될 수 있습니다.') # CRITICAL:root:심각한 에러로 인해 프로그램이 종료될 수 있습니다.