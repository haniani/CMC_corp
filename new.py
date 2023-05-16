import json
import os
import re

dir_name = "."
table_head = "filepath;платформа;дата публикации (для промежутков год);дата рождения;название группы;тип записи;пост или комментарий (ответ);количество токенов\n"


total_words = 0
total_posts_not_empty = 0

head_open = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n\
<html>\n\
<head>\n\
\n"

with open("table.csv", "a+") as table:
    table.write(str(table_head))

table_line = ""

for root, dirs, files in os.walk(dir_name):
  for file_posts in files:
    if file_posts.endswith(".json"):
        with open(file_posts) as file:
            with open("table.csv", "a+") as table:
                data = json.load(file)
                birthday = "<meta content=\"" + "" + " \" name=\"birthday\"/>\n"
                group_name = "<meta content=\"" + data["name"] + " \"name=\"group\"/>\n"
                post_type = "<meta content=\"" + "пост" + " \"name=\"type\"/>\n"
                audience_age = "<meta content=\"н-возраст\" name=\"audience_age\"/>\n"
                audience_level = "<meta content=\"н-уровень\" name=\"audience_level\"/>\n"
                audience_size = "<meta content=\"большая\" name=\"audience_size\"/>\n"
                close_head = "</head>\n<body>\n <p>"
                close_body = "</p>\n</body>\n</html>"
                for i in data["messages"]:
                    posts = i["text_entities"]
                    post_date = "<meta content=\"" + i['date'] + "\" name=\"date\"/>\n"
                    for k in posts:
                        post = k["text"]
                        if len(post)>1:
                            words = post.split(" ")
                            total_posts_not_empty +=1
                            total_words_post = len(words)
                            total_words += len(words)
                            print(total_words)
                            new_file = "{}.xml".format(total_posts_not_empty)
                            with open(new_file, "w") as f:
                                f.write(str(head_open))
                                f.write(str(birthday))
                                f.write(str(post_date))
                                f.write(str(group_name))
                                f.write(str(post_type))
                                f.write(str(audience_age))
                                f.write(str(audience_level))
                                f.write(str(audience_size))
                                f.write(str(close_head))
                                f.write(str(post))
                                f.write(str(close_body))

                                date_post = i['date']
                                if date_post != 0:
                                    date_post == date_post
                                else:
                                    date_post = 0

                                post_n = re.sub("^\\s+|\n|\r|\\s+$", '', post)
                                post_n_n = re.sub(";", ',', post_n)
                                if len(post_n_n) > 1:
                                    post_n_n_n = post_n_n
                                else:
                                    continue

                                table_line = "texts/telegram/"+ str(total_posts_not_empty) + ";" + "telegram" + ";" + str(date_post) + ";" + "" + ";" + data["name"] + ";"+ "пост" + ";"+ post_n_n_n + ";" + str(total_words_post) + "\n"
                                table.write(str(table_line))
                        else:
                            continue

    else:
        continue
        print("###")

table.close()
print("Завершено")
exit()