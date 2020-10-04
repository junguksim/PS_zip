import re

def solution(word, pages):
    answer = 0
    meta_parser = re.compile('<meta(.+?)/>')
    a_parser = re.compile('<a(.+?)>')
    word = str.lower(word)
    page_points = dict()
    page_lst = []
    page_list = []
    for p in pages:
        meta_tags = meta_parser.findall(p)
        lower_p = str.lower(p)
        default_point = re.sub('[^a-z]+', ".", lower_p).split('.').count(word)
        url = meta_tags[0].split('"https://')[1][:-1]
        a_tags = a_parser.findall(p)
        page_list.append(url)
        links = list(map(lambda x: (x.split('https://')[1]).split(" ")[0][:-1], a_tags))
        page_lst.append([url, links])
        if url not in page_points:
            page_points[url] = [default_point, 0]
        else:
            page_points[url][0] += default_point
    for p in page_lst:
        url = p[0]
        links = p[1]
        print(url, links)
        for link in links:
            if link not in page_points:
                continue
            else:
                page_points[link][1] += page_points[url][0] / len(links)
    print(page_points)
    return page_list.index(sorted(page_points.items(), key=(lambda x: sum(x[1])), reverse=True)[0][0])

print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))