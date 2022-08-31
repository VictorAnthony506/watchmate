from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    # page_size: A numeric value indicating the page size. If set, this overrides the PAGE_SIZE setting. \
        # Defaults to the same value as the PAGE_SIZE settings key.
    page_size = 3   
    page_size_query_param = 'size'
    max_page_size = 10
    
    
class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    

class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = '-created' # '-created' is from new to old WHILE 'created' is from old to new
    cursor_query_param = 'record'