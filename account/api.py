from mysite.settings import LOGIN_REDIRECT_URL, LOGIN_URL
from django.contrib.auth import update_session_auth_hash

import json
from django.http import JsonResponse

from .forms import UserUpdateForm, UserPasswordChangeForm

# def password_change_view(request):
#     # if request.method == "POST":
#     #     data = json.loads(request.body)
#     #     old_password = data['oldPassword']
#     #     instance = get_object_or_404(MyUser, id=request.user.id)
#     #     if not (old_password and data['password'] and data['password2']):
#     #         return JsonResponse({'error': 'Wszystkie pola są wymagane.'})
#     #     if check_password(old_password, instance.password):
#     #         print("Stare hasło się zgadza")
#     #         form = UserPasswordChangeForm(data, instance=instance)
#     #         if form.is_valid():
#     #             print("formularz przeszedł walidacje")
#     #             form.save()
#     #             update_session_auth_hash(request, form.user)
#     #             return JsonResponse({'success': 'Hasło zostało zmienione.'})
#     #         else:
#     #             return JsonResponse({'error': 'Podane hasła są różne.'})
#     #     return JsonResponse({'error': 'Podane hasło jest niepoprawne.'})
#     # return render(request, 'account/detail_profile.html', {})
#     return render(request, 'account/detail_profile/password_change.html', {})


# @login_required(login_url=LOGIN_URL)
# def delete_profile_view(request):
#     data = json.loads(request.body)
#     instance = get_object_or_404(MyUser, id=request.user.id)
#     form = UserUpdateForm(data, instance=instance)
#     if form.is_valid():
#         form.save()
#         return JsonResponse({'success': 'Nazwa została zmieniona.'}, status=200)
#     return JsonResponse({"error": 'To pole nie może być puste.'}, status=400)
#     return render(request, 'account/detail_profile/delete.html', {})