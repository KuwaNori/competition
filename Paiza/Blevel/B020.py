# ネットサーフィン
N = int(input())
pages = []
log = []
current_page_no = -1
for i in range(N):
    string = input()
    if string == "use the back button":
        current_page_no -= 1
        log.append(pages[current_page_no])
    else:
        page_name = string[6:]
        current_page_no += 1
        pages.insert(current_page_no, page_name)
        log.append(pages[current_page_no])
for l in log:
    print(l)
