file = open("a.txt", "w", encoding="utf-8")
file.write("Садок вишневий коло хати,\n"
           "Хрущі над вишнями гудуть,\n"
           "Плугатарі з плугами йдуть,\n"
           "Співають ідучи дівчата,\n"
           "А матері вечерять ждуть.\n"
           "Сім'я вечеря коло хати,\n"
           "Вечірня зіронька встає.\n"
           "Дочка вечерять подає,\n"
           "А мати хоче научати,\n"
           "Так соловейко не дає.\n"
           "Поклала мати коло хати\n"
           "Маленьких діточок своїх;\n"
           "Сама заснула коло їх.\n"
           "Затихло все, тілько дівчата\n"
           "Та соловейко не затих.\n")
file.close()
p = 0
i = 0
with open('a.txt') as f:
    line = f.readlines()
with open('a.txt', 'r') as f:
    with open('b1.txt', 'w') as f1:
        for lines in line:
            p += 1
            if (p % 2 == 0):
                f1.write(lines.upper())
with open('a.txt', 'r') as f:
    with open('b2.txt', 'w') as f2:
        for lines in line:
            i += 1
            if ((i - 1) % 2) == 0:
                lines = lines.lower()
                f2.write(lines)
