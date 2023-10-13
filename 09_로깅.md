# 로깅

로깅은 어떤 소프트웨어가 실행될 때 발생하는 이벤트를 추적하는 수단. 

참고자료: <https://docs.python.org/ko/3/howto/logging.html>

로그를 남기기 위해 기본적으로 logging 모듈을 활용할 수 있음.

## 로그 레벨

- DEBUG: 상세한 정보. 보통 문제를 진단할 때.
- INFO: 예상대로 작동하는지에 대한 확인.
- WARNING: 예상치 못한 일이 발생했거나 가까운 미래에 발생할 문제에 대한 표시. 소프트웨어는 여전히 예상대로 작동.
- ERROR: 더욱 심각한 문제로 인해, 소프트웨어가 일부 기능을 수행하지 못할 때.
- CRITICAL: 심각한 에러. 프로그램 자체가 계속 실행되지 않을 수 있음을 나타냄.

## 로그 남기는 방법

- 콘솔에 출력
- 파일에 기록

### 로그 콘솔에 출력

```python
import logging

logging.debug('문제를 진단합니다.') # x
logging.info('예상대로 작동합니다.') # x
logging.warning('미래에는 문제가 될 수도 있습니다.') # WARNING:root:미래에는 문제가 될 수도 있습니다.
logging.error('에러로 인해 일부 기능이 제대로 작동되지 않을 수 있습니다.') # ERROR:root:에러로 인해 일부 기능이 제대로 작동되지 않을 수 있습니다.
logging.critical('심각한 에러로 인해 프로그램이 종료될 수 있습니다.') # CRITICAL:root:심각한 에러로 인해 프로그램이 종료될 수 있습니다.
```

기본 로그 레벨이 WARNING이기 떄문에 debug, info 메시지는 콘솔에 출력되지 않았음.

기본 로그 레벨을 DEBUG로 수정하면 모든 로그 레벨의 메시지가 콘솔에 출력됨.

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug('문제를 진단합니다.') # DEBUG:root:문제를 진단합니다.
logging.info('예상대로 작동합니다.') # INFO:root:예상대로 작동합니다.
logging.warning('미래에는 문제가 될 수도 있습니다.') # WARNING:root:미래에는 문제가 될 수도 있습니다.
logging.error('에러로 인해 일부 기능이 제대로 작동되지 않을 수 있습니다.') # ERROR:root:에러로 인해 일부 기능이 제대로 작동되지 않을 수 있습니다.
logging.critical('심각한 에러로 인해 프로그램이 종료될 수 있습니다.') # CRITICAL:root:심각한 에러로 인해 프로그램이 종료될 수 있습니다.
```

### 로그 메모장에 기록

콘솔에 출력하는 로그는 휘발성임. 메모장 등의 파일에 로그를 기록해야 나중에 문제를 추적할 수 있음.

```python
import logging

logging.basicConfig(filename='my.log', encoding='utf-8', level=logging.DEBUG)

logging.debug('문제를 진단합니다.') # DEBUG:root:문제를 진단합니다.
logging.info('예상대로 작동합니다.') # INFO:root:예상대로 작동합니다.
logging.warning('미래에는 문제가 될 수도 있습니다.') # WARNING:root:미래에는 문제가 될 수도 있습니다.
logging.error('에러로 인해 일부 기능이 제대로 작동되지 않을 수 있습니다.') # ERROR:root:에러로 인해 일부 기능이 제대로 작동되지 않을 수 있습니다.
logging.critical('심각한 에러로 인해 프로그램이 종료될 수 있습니다.') # CRITICAL:root:심각한 에러로 인해 프로그램이 종료될 수 있습니다.
```

위 파이썬 파일을 실행한 경로에 my.log 파일이 생성되고 그 안에 다음과 같은 내용이 담겨있을 것이다.

```log
DEBUG:root:문제를 진단합니다.
INFO:root:예상대로 작동합니다.
WARNING:root:미래에는 문제가 될 수도 있습니다.
ERROR:root:에러로 인해 일부 기능이 제대로 작동되지 않을 수 있습니다.
CRITICAL:root:심각한 에러로 인해 프로그램이 종료될 수 있습니다.
```
