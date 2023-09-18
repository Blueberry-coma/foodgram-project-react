from rest_framework.pagination import PageNumberPagination

from utils import constants


class CustomPagination(PageNumberPagination):
    page_size = constants.DEFAULT_PAGE_SIZE
    page_size_query_param = 'limit'
    max_page_size = constants.DEFAULT_MAX_PAGE_SIZE
