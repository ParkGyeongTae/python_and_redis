import os
import pprint

# 환경변수를 안이쁘게 출력 방법
# print(os.environ)

# 환경변수를 이쁘게 출력하는 방법
# for key, value in os.environ.items():
#     print('{}: {}'.format(key, value))

# 환경변수를 딕셔너리로 출력하는 방법
env_dict = {}

for key, value in os.environ.items():
    env_dict.setdefault(key, value)

pprint.pprint(env_dict)