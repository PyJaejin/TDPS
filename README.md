# TDPS
Thread Disaster Prevention System


nrf52840-evk 보드를 활용해 Thread Network를 구성한다. 

라즈베리파이가 MQTT 프로토콜을 통해 각 노드의 온도 정보를 구독하고,

일정 온도를 초과하면 등록된 사용자에게 메일 발송, PushBullet 메시지를 발송한다.
