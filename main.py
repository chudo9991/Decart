import os
import svg_turtle

file_list = os.listdir("./images")
size = 30
WIDTH = 1920
HEIGHT = 1080

for folder in os.listdir("./src"):
    # print("Обрабатываю: ", folder)
    for file in os.listdir(f"./src/{folder}"):
        if file.endswith(".txt"):
            # print("Обработка: ", file)
            try:
                with open(f"./src/{folder}/{file}", "r") as f:
                    lines = f.readlines()
                    dots = []
                    for line in lines:
                        line = line.replace("(", "")
                        line = line.replace(")", "")
                        line = line.replace("\n", "")
                        line = line.replace(":", ";")
                        line = line.replace(",", ".")
                        line = line.split(";")
                        for i in line:
                            temp = []
                            if i.startswith("-"):
                                i = i.replace("-", "")
                                temp.append(-1 *float(i))
                            elif i.startswith("*"):
                                pass
                            else:
                                temp.append(float(i))
                            # line.append(temp)                
                        dots.append(line)

                # t = turtle.Turtle()
                t = svg_turtle.SvgTurtle(WIDTH, HEIGHT)
                t.ht()
                t.speed(0)
                # клетки
                for x in range(-WIDTH//2, WIDTH//2, size):
                    t.color("grey")
                    t.up()
                    t.goto(x, -HEIGHT//2)
                    t.down()
                    t.goto(x, HEIGHT//2)
                for y in range(-HEIGHT//2, HEIGHT//2, size):
                    t.color("grey")
                    t.up()
                    t.goto(-WIDTH//2, y)
                    t.down()
                    t.goto(WIDTH//2, y)
                
                t.pensize(2)
                t.up()
                t.goto(-WIDTH//2, 0)
                t.down()
                t.goto(WIDTH//2, 0)
                t.up()
                t.goto(0, -HEIGHT//2)
                t.down()
                t.goto(0, HEIGHT//2)        
                
                t.pensize(3)
                t.color("red")
                t.up()
                t.goto(0, -HEIGHT//4)
                t.write(f"Номер: {file.split('.')[0]}. Точек: {len(dots)}", align="center", font=("Arial", 16, "bold"))
                t.goto(float(dots[0][0])*size, float(dots[0][1])*size)


                for elem in dots:
                    if elem[0] == "*":
                        # t.up()
                        pass
                    else:
                        t.down()
                        t.goto(float(elem[0])*size, float(elem[1])*size)
                        # напечатай текст по координатам
                        t.write(f"{elem[0]}, {elem[1]}", font=("Arial", 8, "normal"))

                t.save_as(f"./images/{file.split('.')[0]}.svg")    
                # print(f"Готово: {file}")
            except Exception as e:
                print(f"Error: {file}")
                print(e)
