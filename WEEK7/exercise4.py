def printing_list_items(my_list, title=""):

    if len(my_list) > 0:
        print("TITLE : " + title)

    for a in my_list:
        print(a)


x = ["a", "b", "c"]


printing_list_items(x, "List of colors")
