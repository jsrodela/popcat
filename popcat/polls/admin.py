from django.contrib import admin
from . import consumers


@admin.action(description='Reset number')
def reset_number(a, b, c):
    consumers.reset_count(0)


admin.site.add_action(reset_number, 'reset_number')
