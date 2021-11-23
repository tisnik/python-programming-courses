# Vykreslení čar s různým sklonem
for i in range(1, 90, 5):
    # převod ze stupňů na radiány
    angle = math.radians(i)
    radius = 150
    # výpočet koncových bodů úseček
    x = radius * math.sin(math.radians(i))
    y = radius * math.cos(math.radians(i))
    # vykreslení jedné úsečky
    pygame.draw.line(display, WHITE, (WIDTH-1, 0), (WIDTH-x, y))
