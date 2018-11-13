#!/usr/bin/env python
# -*- coding:utf8 -*-

class Page_Info:
    def __init__(self, current_page, all_count, per_page, base_url, show_page=11):
        try:
            self.current_page = int(current_page)
        except Exception:
            self.current_page = 1
        self.per_page = per_page
        page_num, sur_page = divmod(all_count, per_page)
        if sur_page:
            page_num += 1
        self.all_page = page_num
        self.show_page = show_page
        self.base_url = base_url

    def start(self):
        return (self.current_page - 1) * self.per_page


    def end(self):
        return self.current_page * self.per_page


    def pager(self):
        page_list = []

        half = int((self.show_page - 1) / 2)

        if self.all_page < self.show_page:
            begin = 1
            stop = self.all_page + 1
        else:
            if self.current_page <= half:
                begin = 1
                stop = self.show_page + 1
            else:
                if self.current_page + half > self.all_page:
                    begin = self.all_page - self.show_page + 1
                    stop = self.all_page + 1
                else:
                    begin = self.current_page - half
                    stop = self.current_page + half + 1

        if self.current_page <= 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='%s?page=%s'>上一页</a></li>" % (self.base_url, self.current_page - 1,)
        page_list.append(prev)

        for i in range(begin, stop):
            if i == self.current_page:
                temp = "<li class='active'><a  href='%s?page=%s'>%s</a></li>" % (self.base_url, i, i,)
            else:
                temp = "<li><a href='%s?page=%s'>%s</a></li>" % (self.base_url, i, i,)
            page_list.append(temp)

        if self.current_page >= self.all_page:
            nex = "<li><a href='#'>下一页</a></li>"
        else:
            nex = "<li><a href='%s?page=%s'>下一页</a></li>" % (self.base_url, self.current_page + 1,)
        page_list.append(nex)

        return ''.join(page_list)