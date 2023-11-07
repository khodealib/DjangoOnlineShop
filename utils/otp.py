from kavenegar import KavenegarAPI, APIException, HTTPException

from DjangoOnlineShop import settings


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_APIKEY)
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f'کد تایید شما: {code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def send_otp_code_fake(phone_number, code):
    print(f'phone number: {phone_number} - code: {code}')
