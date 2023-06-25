from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

# 쿨 SMS API 키와 시크릿 키
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# 쿨 SMS 발신자 번호
sender = "01000000000"

# 쿨 SMS 수신자 번호
receiver = "01011111111"

# 쿨 SMS 내용
text = "쿨 SMS 테스트 메시지"

# 쿨 SMS 보내기
cool = Message(api_key, api_secret)

try:
    response = cool.send({
        'to': receiver,
        'from': sender,
        'text': text
    })
    print("쿨 SMS가 성공적으로 전송되었습니다.")
    print("메시지 아이디:", response['message_id'])
except CoolsmsException as e:
    print("쿨 SMS가 전송되지 않았습니다.")
    print("에러 메시지:", e)
