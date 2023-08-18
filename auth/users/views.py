from django.shortcuts import render
from rest_framework import views, viewsets
from rest_framework.views import APIView, Response
from .models import *
from .serializers import *
from .validators import validate_phone_number, code_validartor, invite_code_validator
import re
import random
import time


def home(request):
    return render(request, "index.html", {})

# эндпоинт для создания 4-значного кода


class Authorization(APIView):
    def post(self, request, *args, **kwargs):
        try:
            phone = request.data['phone']
        except KeyError:
            return Response({"error": "номер не передается в запросе"}, 400)

        if validate_phone_number(phone) == False:
            return Response({"error": "неверный формат"}, 400)

        cleaned_number = re.sub(r'[-\s]', '', phone)
        passcode = random.randint(1_000, 9_999)

        try:
            user = User.objects.get(phone_number=cleaned_number)
            # если такой юзер есть, меняю его пароль на новый сгенерированный код
            user.passcode = passcode
            user.save()
        except:
            # так как юзернем совсем не важен, использую passcode как юзернейм
            # но можно конечно убрать полностью поле юзернейм
            # для поля password просто присваиваю passcode
            instance = User(
                username=passcode,
                phone_number=cleaned_number,
                passcode=passcode,
                password=passcode
            )
            instance.save()

            # если такого номера нет, создаю в бд нового и возвращаю статус 201 с кодом
            time.sleep(2)
            return Response({"code": passcode}, 201)

        # спим на 2 секунды
        time.sleep(2)
        # в случае если все прошло гладко и такой юзер есть, статус 200
        return Response({"code": passcode}, 200)


# эндпоинт для проверки 4-значного кода
class Authenticate(APIView):
    def post(self, request, *args, **kwargs):
        # пробую получть данные с запроса
        try:
            code = request.data['code']
            phone = request.data['phone']
        except KeyError:
            return Response({
                "authenticated": False,
                "error": "не найдены ключи в post запросе"
            }, 400)

        # проверяю код на валидицаю (пока только длину)
        if code_validartor(code) == False:
            return Response({
                "authenticated": False,
                "error": "код не прошел валидацию"
            }, 400)

        # сперва провперяю есть ли такой номер в базе
        # если есть, проверяю его passcode с code полученным с post запроса
        try:
            user_instance = User.objects.get(phone_number=phone)
            # если пароли совпадают возвращаю user_id (можно возвращать его uuid, но как тест беру id)
            if user_instance.passcode == int(code):
                return Response({
                    "authenticated": True,
                    "user_id": user_instance.id
                }, 200)
            else:
                return Response(
                    {
                        "authenticated": False,
                        "error": "код проверки неверный"
                    }, 400)

        except:
            return Response(
                {
                    "authenticated": False,
                    "error": 'что-то пошло не так, номер не найден в базе'
                }, 400)


class ActivateInvite(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # юзер который вводит инвайт код
            user_id = request.data['user_id']
            # инвайт код юзера
            invite = request.data['invite']
        except KeyError:
            return Response({
                "error": "не найдены ключи в post запросе"
            })

        try:
            user_instance = User.objects.get(id=user_id)
            if invite_code_validator(invite) == False:
                return Response({
                    "error": "неверный формат инвайт кода"
                }, 400)

            if user_instance.activated_invite_code:
                return Response({
                    "error": "у данного юзера уже активирован инвайт код"
                }, 400)
            else:
                try:
                    invite_owner = User.objects.get(invite_code=invite)
                    user_instance.activated_invite_code = invite
                    user_instance.save()
                    return Response({
                        "success": True,
                    }, 201)
                except:
                    return Response({
                        "error": "нет такого юзера у кого такой инвайт код"
                    }, 400)
        except:
            return Response({
                "error": "юзер с таким айди не найден"
            }, 400)


class GetUserDetail(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user_id = request.data['user_id']
        except KeyError:
            return Response({"error": "не найден ключ в post запросе"})

        try:
            user_instance = User.objects.get(id=user_id)
        except:
            return Response({"error": "нет такого юзера в бд"})

        if user_instance.activated_invite_code:
            referals = User.objects.filter(
                activated_invite_code=user_instance.invite_code)
        else:
            referals = []

        return Response({
            "id": user_instance.id,
            "phone_number": user_instance.phone_number,
            "invite_code": user_instance.invite_code,
            "activated_invite_code": user_instance.activated_invite_code,
            "referals": [
                {
                    'id': x.id,
                    'phone_number': x.phone_number,
                    'activated_invite_code': x.activated_invite_code
                } for x in referals
            ]
        })
