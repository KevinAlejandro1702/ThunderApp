from django.views import View
from ThunderApp.models import Users
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class UsersView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if (id > 0):
            users = list(Users.objects.filter(id=id).values())
            if (len(users)>0):
                user = users[0]
                datos = {'message': 'Success', 'user': user}
            else:
                datos = {'message': 'User not found!'}
            return JsonResponse(datos)
        else:
            users = list(Users.objects.values())
            if len(users) > 0:
                datos = {'users': users}
            else:
                datos = {'message': 'Users not found'}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        Users.objects.create(id=jd['id'], lastName=jd['lastName'], firstName=jd['firstName'],
                             birthDate=jd['birthDate'], address=jd['address'], phone=jd['phone'], role=jd['role'], isActive=jd['isActive'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)


    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(Users.objects.filter(id=id).values())
        if len(users) > 0:
            user = Users.objects.get(id=id)
            user.id = jd['id']
            user.lastName = jd['lastName']
            user.firstName = jd['firstName']
            user.birthDate = jd['birthDate']
            user.address = jd['address']
            user.phone = jd['phone']
            user.role = jd['role']
            user.isActive = jd['isActive']
            user.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "User not found..."}
        return JsonResponse(datos)


    def delete(self, request, id):
        users = list(Users.objects.filter(id=id).values())
        if len(users) > 0:
            Users.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "User not found..."}
        return JsonResponse(datos)
