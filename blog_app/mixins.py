from django.shortcuts import redirect


class CustomLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated :
            return redirect('accounts_app:login')
        return super().dispatch(request, *args, **kwargs)
        