from django.utils.translation import ugettext_lazy as _

from rest_framework.pagination import CursorPagination


class TaskPagination(CursorPagination):
    cursor_query_param = "cursor"
    cursor_query_description = _("The pagination cursor value.")
    page_size = 10
    invalid_cursor_message = _("Invalid cursor")
    ordering = "-id"
    page_size_query_param = "results_per_page"
    max_page_size = 10
    offset_cutoff = 1000
