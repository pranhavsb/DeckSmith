import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = pygame.display.Info().current_w - 100, pygame.display.Info().current_h - 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emojack, A Blackjack Game")

# Card values
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
card_emojis = {card: f"[{card}]" for card in card_values.keys()}  # Placeholder emoji

# Functions
def create_deck():
    deck = list(card_values.keys()) * 4
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = sum(card_values[card] for card in hand)
    num_aces = hand.count('A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def display_hands(player_hand, dealer_hand, show_dealer_full_hand=False):
    font = pygame.font.Font(None, 48)
    player_hand_text = ' '.join(card_emojis[card] for card in player_hand)
    dealer_hand_text = ' '.join(card_emojis[card] for card in dealer_hand if show_dealer_full_hand or card == dealer_hand[0])
    player_hand_display = font.render(f"Player: {player_hand_text} (Total: {calculate_hand_value(player_hand)})", True, (255, 255, 255))
    dealer_hand_display = font.render(f"Dealer: {dealer_hand_text} (Total: {'?' if not show_dealer_full_hand else calculate_hand_value(dealer_hand)})", True, (255, 255, 255))
    screen.blit(player_hand_display, (50, HEIGHT - 150))
    screen.blit(dealer_hand_display, (50, 50))

def draw_button(text, x, y, w, h, color):
    font = pygame.font.Font(None, 48)
    button_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, button_rect)
    pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
    button_text = font.render(text, True, (0, 0, 0))
    screen.blit(button_text, (x + (w - button_text.get_width()) // 2, y + (h - button_text.get_height()) // 2))
    return button_rect

def select_bet(player_money):
    font = pygame.font.Font(None, 48)
    bet = 0
    while bet == 0:
        screen.fill((0, 120, 0))
        bet_text = font.render(f"Choose your bet (You have {player_money} coins)", True, (255, 255, 255))
        screen.blit(bet_text, (50, 50))
        bets = {
            50: draw_button("50", 50, HEIGHT - 200, 150, 50, (255, 0, 0)),
            100: draw_button("100", 250, HEIGHT - 200, 150, 50, (0, 0, 255)),
            500: draw_button("500", 450, HEIGHT - 200, 150, 50, (255, 255, 0)),
            1000: draw_button("1000", 650, HEIGHT - 200, 150, 50, (0, 255, 0)),
            2000: draw_button("2000", 850, HEIGHT - 200, 150, 50, (255, 128, 0)),
            5000: draw_button("5000", 1050, HEIGHT - 200, 150, 50, (128, 0, 255)),
            player_money: draw_button("All In", 1250, HEIGHT - 200, 150, 50, (255, 0, 255)),
        }
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for amount, rect in bets.items():
                    if rect.collidepoint(event.pos) and amount <= player_money:
                        return amount
    return bet


def blackjack_game():
    player_money = 10000
    quit_game = False

    while player_money > 0 and not quit_game:
        bet = select_bet(player_money)
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        game_over, player_busted, doubled = False, False, False

        while not game_over:
            screen.fill((0, 120, 0))
            display_hands(player_hand, dealer_hand[:1])
            hit_button = draw_button("Hit", 50, HEIGHT - 100, 150, 50, (255, 0, 0))
            stand_button = draw_button("Stand", 250, HEIGHT - 100, 150, 50, (0, 0, 255))
            double_button = draw_button("Double", 450, HEIGHT - 100, 150, 50, (255, 255, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit_game = True
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hit_button.collidepoint(event.pos):
                        player_hand.append(deck.pop())
                        if calculate_hand_value(player_hand) > 21:
                            player_busted = True
                            game_over = True
                    elif stand_button.collidepoint(event.pos):
                        while calculate_hand_value(dealer_hand) < 17:
                            dealer_hand.append(deck.pop())
                        game_over = True
                    elif double_button.collidepoint(event.pos) and not doubled and player_money >= bet:
                        # Double the bet and deduct it from player money immediaty
                        doubled = True

                        bet *= 2  # Double bro's bet

                        # Adda card to the player and end bro's turn
                        player_hand.append(deck.pop())
                        if calculate_hand_value(player_hand) > 21:
                            player_busted = True
                        game_over = True

        # Dealer plays if the game isn't already over and plays like a real person(doesnt hit if value is above 17)
        while calculate_hand_value(dealer_hand) < 17 and not player_busted:
            dealer_hand.append(deck.pop())

        # Display results
        screen.fill((0, 120, 0))
        display_hands(player_hand, dealer_hand, True)
        player_score, dealer_score = calculate_hand_value(player_hand), calculate_hand_value(dealer_hand)

        if player_busted:
            result_text = f"You busted! Lost {bet} coins."
            player_money -= bet  # player doubled loss
        elif dealer_score > 21 or player_score > dealer_score:
            result_text = f"You win! Gained {bet} coins."
            player_money += bet  # player doubled profit
        elif player_score == dealer_score:
            result_text = "It's a tie (push)!"
        else:
            result_text = f"You lose! Lost {bet} coins."
            player_money -= bet  # player doubled loss

        font = pygame.font.Font(None, 48)
        result_display = font.render(result_text, True, (255, 255, 255))
        screen.blit(result_display, (WIDTH // 2 - result_display.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        time.sleep(3)

        if player_money <= 0:
            break
        continue_button = draw_button("Play Again", 50, HEIGHT - 100, 150, 50, (0, 255, 0))
        quit_button = draw_button("Quit", 250, HEIGHT - 100, 150, 50, (255, 0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint(event.pos):
                    break
                elif quit_button.collidepoint(event.pos):
                    quit_game = True

    pygame.quit()
    print("Game Over")
blackjack_game()

blackjack_game()
