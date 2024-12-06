# **DeckSmith: The Ultimate Blackjack Experience**

Welcome to **DeckSmith**! A Blackjack game that challenges your luck and strategy in equal measure. Whether you’re a seasoned player or a total newbie, **DeckSmith** will immerse you in the world of Blackjack with exciting, high-stakes gameplay. Like *Harvey Specter* would say, **"You don’t play the odds, you play the man,"** but in this game, **you play the cards**.

---

## **About the Game**

**DeckSmith** is an immersive Blackjack game built with Python and Pygame. With a fresh, user-friendly interface and thrilling gameplay, you'll be on the edge of your seat. The dynamic deck, betting options, and dealer challenges make it more than just a game of luck—it’s all about making the right decisions at the right time. **Risk comes from not knowing what you're doing**, as *Harshad Mehta* famously said.

The goal? Reach 21 or get as close as possible without going over, to beat the dealer. Sounds easy? Think again. The real challenge lies in your decisions—*Hit, Stand, or Double?* Sometimes, you have to make the bold move, like *Spider-Man* would say, **"With great power comes great responsibility."**

---

## **How to Play**

1. **Choose Your Bet:**
   - You start with a set amount of money. Choose wisely! You can choose from several options, ranging from modest bets like 50 to high-stakes bets like 5000. Or, if you're feeling lucky, go "All In!" **You can't win the game if you're afraid to bet.** 

2. **Gameplay:**
   - After placing your bet, you and the dealer will be dealt two cards each. Your goal is to get as close to 21 as possible without going over.
   - You can **Hit** (take another card), **Stand** (stick with your hand), or **Double** (double your bet and take exactly one more card).
   - Make your move. **It’s not about the cards, it’s about how you play them,** a motto **Walter White** would surely approve of.

3. **Dealer's Turn:**
   - After you make your decision, the dealer will reveal their hand and play according to standard Blackjack rules. The dealer must hit until they have 17 or more.
   - In a game of high-stakes tension, **you don’t play the odds, you play the dealer**, like *Harshad Mehta* would say, **“I gamble, but I don’t rely on luck.”**

4. **Winning and Losing:**
   - If you beat the dealer’s hand without busting (going over 21), you win! You’ll earn double your bet if you win after doubling.
   - If you bust, you lose your bet. If the dealer busts, you win! **Sometimes you lose, but that’s just the setup for a bigger win,** like *Harvey Specter* always says.

5. **Play Again or Quit:**
   - After each round, you can choose to play again or quit. Just remember, the house always has an edge, but with skill and luck, you might just outsmart the dealer.

---

## **Features**

- **Betting System:** Choose your bet from a range of options, from small wagers to high-risk bets. **You can't win if you don't take calculated risks.** 
- **Hit, Stand, and Double Options:** Make critical decisions that could change the course of the game. **It’s not about the hand you’re dealt, it’s about how you play it.** 
- **Dynamic Card Deck:** Cards are shuffled, and every round is different—expect the unexpected!
- **Realistic Gameplay:** The dealer plays with standard Blackjack rules for added realism. 
- **User Interface (UI):** Designed for ease and engagement, keeping you focused on the game.

---

## **Game Functions**

Here’s a breakdown of all the key functions within **DeckSmith**:

### 1. **`create_deck()`**
   - **Purpose:** Creates a shuffled deck of cards.
   - **Details:** The deck consists of 4 copies of each card (2-10, J, Q, K, A), shuffled to add randomness. **Always expect the unexpected, even in a shuffled deck.**

### 2. **`calculate_hand_value(hand)`**
   - **Purpose:** Calculates the total value of the player’s or dealer’s hand.
   - **Details:** Face cards (J, Q, K) are worth 10, and Ace is 11 unless it would cause the hand to bust, in which case it’s valued at 1. 

### 3. **`display_hands(player_hand, dealer_hand, show_dealer_full_hand=False)`**
   - **Purpose:** Displays both player’s and dealer’s hands on the screen.
   - **Details:** The player’s hand is always visible, but the dealer’s second card stays hidden until after the player’s decision.

### 4. **`draw_button(text, x, y, w, h, color)`**
   - **Purpose:** Draws a clickable button for user interaction.
   - **Details:** Buttons are used for actions like "Hit", "Stand", and "Double". **Remember, ball's in your court**

### 5. **`select_bet(player_money)`**
   - **Purpose:** Allows the player to choose their bet.
   - **Details:** The function displays betting options based on the player’s available funds. **Bet smart—choose when to risk and when to hold back.**

### 6. **`blackjack_game()`**
   - **Purpose:** Runs the entire Blackjack game loop.
   - **Details:** Alternates between the player’s turn and the dealer’s turn, calculating the winner and updating the player’s money. **Play with calculated risks and confidence.**

---

## **Game Tips**

- **Play the Man (or AI), not the odds:** Blackjack isn’t just about the cards—it’s about reading the dealer and knowing when to take calculated risks.
- **Know When to Double:** Doubling your bet can be lucrative, but don’t do it unless the odds are in your favor—especially when you have a total of 10 or 11.
- **Know When to Hit:** Try your best not to hit when you have high total.

---

## **Installation Instructions**

Follow these steps to run **DeckSmith** on your local machine:

# Clone the Repository:
git clone https://github.com/pranhavsb/DeckSmith.git

# Install Required Dependencies:
# DeckSmith uses Pygame, so make sure you have it installed:
pip install pygame

# Run the Game:
# Navigate to the game folder:
cd DeckSmith

# Start the game:
python main.py
