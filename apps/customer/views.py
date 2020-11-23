from oscar.apps.customer.views import ProfileView

class Profile(ProfileView):
    template_name = 'oscar/customer/profile/profile.html'