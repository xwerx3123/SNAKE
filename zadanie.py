import pygame
import random
from GameProperties import *

pygame.init()


screen = pygame.display.set_mode((GameProperties.width, GameProperties.height))


clock = pygame.time.Clock()

styl_czcionki = pygame.font.SysFont("comicsans", 30)


def snake(snake_blok, snake_list):
    """Funkcja odpowiadająca z rysowanie naszego węża"""
    for x in snake_list:
        pygame.draw.rect(
            screen, GameProperties.green, (x[0], x[1], snake_blok, snake_blok)
        )


def wiadomosc(msg, kolor, x, y):
    """Wykorzystywana do wyświetlenia wiadomości użytkownikowi"""
    mesg = styl_czcionki.render(msg, True, kolor)
    screen.blit(mesg, (x, y))


def punktacja(score, screen):
    """Wykorzystywana do wyświetlenia końcowej"""
    value = styl_czcionki.render(f"Punktacja:  {score}", True, GameProperties.red)
    screen.blit(value, (GameProperties.width - 250, 10))


def gameloop():
    """
    Pętla główna gry Snake, odpowiadająca za kontrolę stanu gry, renderowanie oraz logikę poruszania węża i kolizji.

    Funkcja obsługuje:
    - Ekran początkowy z instrukcją startu
    - Główne zdarzenia gry (sterowanie wężem, zatrzymanie gry)
    - Kolizje z granicami i samym sobą
    - Logikę wzrostu węża po zjedzeniu jedzenia
    - Wygraną po osiągnięciu określonej długości węża
    - Pauzę gry i restart po przegranej

    Używa globalnych klas/zmiennych:
    - GameProperties – zawiera ustawienia gry (rozmiar ekranu, kolory, prędkość węża)
    - screen – obiekt ekranu Pygame
    - clock – zegar Pygame do kontrolowania liczby klatek
    - funkcji pomocniczych: wiadomosc(), snake(), punktacja()
    """
    
    game_over = False
    game_close = False
    game_pause = False
    game_start = False

    x1 = GameProperties.width / 2
    y1 = GameProperties.height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    dlugosc_snake = 1

    foodx = (
        round(
            random.randrange(0, GameProperties.width - GameProperties.snake_blok) / 10.0
        )
        * 10
    )
    foody = (
        round(
            random.randrange(0, GameProperties.height - GameProperties.snake_blok)
            / 10.0
        )
        * 10
    )

    while not game_start:

        wiadomosc(
            "wcisnij S aby rozpoaczac, wcisnij P aby zatrzymac",
            GameProperties.red,
            GameProperties.width / 5,
            GameProperties.height / 4,
        )
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_start = True

    while not game_over:
        while game_close:
            screen.fill(GameProperties.black)
            wiadomosc(
                "Przegrałeś! Wcisnij G- aby wyjsc albo T- aby zagrac ponownie ",
                GameProperties.red,
                GameProperties.width / 6,
                GameProperties.height / 3,
            )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_t:
                        game_close = False
                        x1, y1 = GameProperties.width // 2, GameProperties.height // 2
                        x1_change, y1_change = 0, 0
                        snake_list = []
                        foodx = (
                            round(
                                random.randrange(
                                    0, GameProperties.width - GameProperties.snake_blok
                                )
                                / 10.0
                            )
                            * 10
                        )
                        foody = (
                            round(
                                random.randrange(
                                    0, GameProperties.height - GameProperties.snake_blok
                                )
                                / 10.0
                            )
                            * 10
                        )

                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -GameProperties.snake_blok
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = GameProperties.snake_blok
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -GameProperties.snake_blok
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = GameProperties.snake_blok
                    x1_change = 0
                elif event.key == pygame.K_p:
                    game_pause = not game_pause

        if game_pause:
            pygame.display.update()
            continue

        if x1 > GameProperties.width or x1 < 0 or y1 > GameProperties.height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(GameProperties.black)
        pygame.draw.rect(
            screen,
            GameProperties.blue,
            (foodx, foody, GameProperties.snake_blok, GameProperties.snake_blok),
        )

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > dlugosc_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        snake(GameProperties.snake_blok, snake_list)
        pygame.display.update()

        punktacja(dlugosc_snake - 1, screen)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = (
                round(
                    random.randrange(
                        0, GameProperties.width - GameProperties.snake_blok
                    )
                    / 10.0
                )
                * 10
            )
            foody = (
                round(
                    random.randrange(
                        0, GameProperties.height - GameProperties.snake_blok
                    )
                    / 10.0
                )
                * 10
            )
            dlugosc_snake += 1

        if dlugosc_snake >= 50:
            wiadomosc(
                "Gratulacje wygrałeś",
                GameProperties.red,
                GameProperties.width / 6,
                GameProperties.height / 3,
            )
            pygame.display.update()
            game_close = True

        clock.tick(GameProperties.snake_speed)

    pygame.quit()
    quit()


gameloop()
