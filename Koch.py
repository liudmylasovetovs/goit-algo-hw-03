import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def draw_koch_snowflake(t, order, size):
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

def main():
    # Введення рівня рекурсії від користувача
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Створення вікна та об'єкта черепашки
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Сніжинка Коха")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(2)
    snowflake_turtle.color("blue")

    # Позначення початку черепашки
    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    # Виклик функції для створення повної сніжинки Коха
    draw_koch_snowflake(snowflake_turtle, order, 300)

    # Закриття вікна при кліку
    wn.exitonclick()

if __name__ == "__main__":
    main()
