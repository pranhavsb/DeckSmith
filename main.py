import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = pygame.display.Info().current_w - 100, pygame.display.Info().current_h - 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emojack")

# Card VAlues
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

card_emojis = {
    '2': '🂲', '3': '🂳', '4': '🂴', '5': '🂵', '6': '🂶', '7': '🂷', '8': '🂸', '9': '🂹', '10': '🂺',
    'J': '🂻', 'Q': '🂽', 'K': '🂾', 'A': '🂡'
}

# Random Deck
def create_deck():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    return deck

# Hand Value
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        value += card_values[card]
        if card == 'A':
            num_aces += 1
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Display hands
def display_hands(player_hand, dealer_hand, show_dealer_full_hand=False):
    font = pygame.font.Font(None, 48)
    player_hand_text = ' '.join([card_emojis[card] for card in player_hand])
    dealer_hand_text = ' '.join([card_emojis[card] for card in dealer_hand])

    player_hand_display = font.render(f"Player: {player_hand_text}  (Total: {calculate_hand_value(player_hand)})", True, (255, 255, 255))

    if show_dealer_full_hand:
        dealer_hand_display = font.render(f"Dealer: {dealer_hand_text}  (Total: {calculate_hand_value(dealer_hand)})", True, (255, 255, 255))
    else:
        dealer_hand_display = font.render(f"Dealer: {dealer_hand_text} ?", True, (255, 255, 255))

    screen.blit(player_hand_display, (50, HEIGHT - 150))
    screen.blit(dealer_hand_display, (50, 50))

# Buttons
def draw_button(text, x, y, w, h, color):
    font = pygame.font.Font(None, 48)
    button_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, button_rect)
    pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
    button_text = font.render(text, True, (0, 0, 0))
    screen.blit(button_text, (x + (w - button_text.get_width()) // 2, y + (h - button_text.get_height()) // 2))
    return button_rect

# Betting
def select_bet(player_money):
    bet = 0
    bet_buttons = {
        50: pygame.Rect(50, HEIGHT - 200, 150, 50),
        100: pygame.Rect(200, HEIGHT - 200, 150, 50),
        1000: pygame.Rect(350, HEIGHT - 200, 150, 50),
        5000: pygame.Rect(500, HEIGHT - 200, 150, 50)
    }

    font = pygame.font.Font(None, 48)
    while bet == 0:
        screen.fill((0, 120, 0))
        bet_text = font.render(f"Choose your bet (You have {player_money} coins)", True, (255, 255, 255))
        screen.blit(bet_text, (50, 50))

        for amount, rect in bet_buttons.items():
            if amount <= player_money:
                pygame.draw.rect(screen, (255, 0, 0), rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 3)
                text = font.render(f"{amount} coins", True, (0, 0, 0))
                screen.blit(text, (rect.x + (rect.width - text.get_width()) // 2, rect.y + (rect.height - text.get_height()) // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for amount, rect in bet_buttons.items():
                    if rect.collidepoint(event.pos) and amount <= player_money:
                        bet = amount
                        return bet
    return bet

# Main game function
def blackjack_game():
    player_money = 10000
    quit_game = False

    while player_money > 0 and not quit_game:
        bet = select_bet(player_money)

        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        game_over = False
        player_busted = False
        dealer_busted = False
        doubled = False

        while not game_over:
            screen.fill((0, 120, 0))

            # Display hands
            display_hands(player_hand, dealer_hand[:1])  # Only show one card of dealer

            # desicions of gambler
            hit_button = draw_button("Hit", 50, HEIGHT - 100, 150, 50, (255, 0, 0))
            stand_button = draw_button("Stand", 250, HEIGHT - 100, 150, 50, (0, 0, 255))
            double_button = draw_button("Double", 450, HEIGHT - 100, 150, 50, (255, 255, 0))

            # Check for button click events
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
                        if calculate_hand_value(dealer_hand) > 21:
                            dealer_busted = True
                        game_over = True
                    elif double_button.collidepoint(event.pos) and not doubled:
                        player_hand.append(deck.pop())
                        doubled = True
                        if calculate_hand_value(player_hand) > 21:
                            player_busted = True
                            game_over = True

            pygame.display.flip()

        # Show dealer's full hand
        display_hands(player_hand, dealer_hand, show_dealer_full_hand=True)
        pygame.display.flip()
        time.sleep(1)  # Delay to show the dealer's cards

        # Determine winner
        player_score = calculate_hand_value(player_hand)
        dealer_score = calculate_hand_value(dealer_hand)

        if player_busted:
            result_text = f"You busted! You lose. Bet: {bet} coins"
            player_money -= bet
        elif dealer_busted:
            result_text = f"Dealer busted! You win. Bet: {bet} coins"
            player_money += bet
        elif player_score > dealer_score:
            result_text = f"You win! Bet: {bet} coins"
            player_money += bet
        elif player_score < dealer_score:
            result_text = f"You lose! Bet: {bet} coins"
            player_money -= bet
        else:
            result_text = f"It's a tie! Bet: {bet} coins"

        # Display result
        font = pygame.font.Font(None, 48)
        result_display = font.render(result_text, True, (255, 255, 255))
        screen.fill((0, 128, 0))
        screen.blit(result_display, (WIDTH // 2 - result_display.get_width() // 2, HEIGHT // 2 - result_display.get_height() // 2))
        pygame.display.flip()
        time.sleep(3)


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
                    break

    pygame.quit()
    print("Game Over")

# Run the game
blackjack_game()
