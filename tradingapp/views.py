from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . models import User_profile
from . forms import ProfileForm, form_validation_error
from django.views import View

from django.contrib import messages

# Create your views here.
@login_required
def Dashboard_view(request):
    context = {}
    return render(request,"tradingapp/dashboard.html",context )


@method_decorator(login_required(login_url='login'), name='dispatch')
class User_profile_view(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = User_profile.objects.get_or_create(user=request.user)
        return super(User_profile_view, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, "tradingapp/user_profile.html", context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('user_profile')