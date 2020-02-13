# 1 all time
# 2 today
# 3 a veek ago
# 4 month ago
# datetime.datetime(2020, 2, 6, 19, 40, 29, 872896)
import datetime as dt
import datetime

def get_month_ago(date):
    if date.month == 1:
        return date.replace(month=12,year=date.year-1)
    return date.replace(month=date.month-1)


def get_today():
    return dt.datetime.today()


def get_week_ago(date):
    if date.day > 7:
        return
    return date.replace(day=date.day-7)


# class SearchResult(generic.ListView):
#     model = Post
#     template_name = 'forum/post_list.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         time = self.request.GET.get("t")
#         date_today = datetime.datetime.today()
#         first = date_today.replace(day=1)
#         lastMonth = first - datetime.timedelta(days=1)
#         dates = {
#             '1': dt.timedelta(month=1),
#             '2': dt.timedelta(month=1),
#             '3': dt.timedelta(weeks=1),
#             '4': lastMonth,
#         }
#
#         if '#' in query:
#             return Post.objects.filter(Q(topic__name=query[1:]))
#         return Post.objects.filter(
#             Q(title__icontains=query) | Q(body__icontains=query)
#         )


if __name__ == '__main__':
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    print(today_max)
    print(today_min)
    # print(get_month_ago(dt.datetime.today()))
    # print(get_month_ago(dt.datetime(2020, 1, 6, 19, 40, 29, 872896)))
    # print(get_week_ago(dt.datetime.today()))
    # print(get_week_ago(dt.datetime(2020, 1, 6, 19, 40, 29, 872896)))