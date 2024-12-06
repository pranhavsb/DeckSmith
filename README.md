# **DeckSmith: The Ultimate Blackjack Experience**

Welcome to **DeckSmith**! A Blackjack game like no other — simple, intuitive, and thrilling, with that perfect balance of luck and strategy. Whether you're a seasoned gambler or a curious beginner, DeckSmith will immerse you in the world of Blackjack in a way that’s both exciting and rewarding. Remember, in the world of Blackjack, it’s all about playing the hand you’re dealt — and like Harvey Specter says, **"You don’t play the odds, you play the man"**.

## **About the Game**

**DeckSmith** is an interactive and fun Blackjack game built using Python and the Pygame library. The game is designed with a fresh, modern look and feel, providing the player with a smooth and engaging experience. With a dynamic deck, various betting options, and a challenge against the dealer, it’s all about making the right decisions at the right time!

The objective? Reach 21, or get as close as possible, without going over, to beat the dealer. Sounds easy? Think again. The challenge lies in your decisions—*Hit, Stand, or Double?* As Harvey would say, **"Sometimes winning is about making the right move at the right time."**

---

## **How to Play**

1. **Choose Your Bet:**
   - You start with a set amount of money. Choose your bet wisely! You can choose from several options, ranging from small amounts like 50 to more substantial bets like 5000. Or, if you're feeling lucky, go "All In!" **You can’t play it safe all the time**, sometimes you have to make that **bold move**, just like Harvey in a courtroom.

2. **Gameplay:**
   - After placing your bet, you and the dealer will be dealt two cards each. Your goal is to get as close to 21 as possible without going over.
   - You can **Hit** (take another card), **Stand** (stick with your hand), or **Double** (double your bet and take exactly one more card).
   - Make your move. **It’s not about the cards, it’s about how you play them**. **Channel your inner Harvey Specter** — **"You’re not a lawyer, you’re a closer!"**

3. **Dealer's Turn:**
   - After you make your decision, the dealer will reveal their hand and play according to the standard Blackjack rules: the dealer will continue to draw cards until their hand totals 17 or more.
   - Like in the courtroom, you’ll have to read your opponent’s moves — **don’t just play the cards, play the situation.**

4. **Winning and Losing:**
   - If you beat the dealer’s hand without busting (going over 21), you win! You’ll earn double your bet if you use the “Double” option and win.
   - If you bust, you lose your bet. If the dealer busts, you win! **Remember, in this game, losing is part of the strategy** — just like in **Suits**, sometimes you lose the battle but win the war.

5. **Play Again or Quit:**
   - After each round, you can choose to play again or quit. Just remember, the house always has an edge, but with skill and luck, you might just outsmart the dealer. **It’s not about winning every hand; it’s about playing your hand the best way you can.**

---

## **Features**

- **Betting System:** Choose your bet from a range of options, from modest wagers to high-risk, high-reward bets. **Like Louis Litt would say, "You can't win the game if you're afraid to bet."**
- **Hit, Stand, and Double Options:** Make critical decisions that could affect your entire game. Sometimes, you have to **play the man**, not the cards, just like in the world of corporate law.
- **Dynamic Card Deck:** Cards are shuffled, so you never know what’s coming next!
- **Realistic Gameplay:** Dealer plays with standard Blackjack rules for added realism. Just like Harvey knows the game, so does the dealer.
- **User Interface (UI):** Designed with simplicity and clarity, ensuring you enjoy your game without distractions.

---

## **Game Functions**

Here’s a breakdown of all the key functions within **DeckSmith**:

### 1. **`create_deck()`**
   - **Purpose:** Creates a shuffled deck of cards.
   - **Details:** The deck consists of 4 copies of each card (2-10, J, Q, K, A), which is shuffled to add randomness. **Just like a good negotiation, you can never predict the outcome, but you can control how you play the hand.**

### 2. **`calculate_hand_value(hand)`**
   - **Purpose:** Calculates the total value of the player’s or dealer’s hand.
   - **Details:** The value of face cards (J, Q, K) is 10, and the Ace (A) is valued at 11, unless that would cause the hand to bust, in which case it is counted as 1. **Play it right — it’s about knowing when to leverage the value of your Ace, just like Harvey knows when to leverage his charm.**

### 3. **`display_hands(player_hand, dealer_hand, show_dealer_full_hand=False)`**
   - **Purpose:** Displays the hands of both the player and the dealer on the screen.
   - **Details:** The player’s hand is always fully visible, but the dealer’s second card is hidden until the player has finished making their decisions. **The power of information — sometimes knowing when to hold back is just as important as knowing when to reveal your cards.**

### 4. **`draw_button(text, x, y, w, h, color)`**
   - **Purpose:** Draws a clickable button on the screen for user interaction.
   - **Details:** Buttons are used for actions like "Hit", "Stand", and "Double". The color and text can be customized. **Just like a lawyer presents the perfect case, every button press is part of your strategy.**

### 5. **`select_bet(player_money)`**
   - **Purpose:** Allows the player to choose their bet for the round.
   - **Details:** The function displays a range of betting options based on the player's available money. The player can choose a predefined amount or go "All In". **Never bet more than you're willing to lose, but never bet too little to miss the big win — play it like Harvey!**

### 6. **`blackjack_game()`**
   - **Purpose:** Runs the entire Blackjack game loop.
   - **Details:** The game alternates between the player’s turn (where they can choose "Hit", "Stand", or "Double") and the dealer’s turn. It then calculates the winner and updates the player’s money. **It’s a game of calculation and timing — just like closing a deal.**

---

## **Game Tips**

- **Play the Man(or AI), not the odds:** Blackjack is a game of strategy and luck. Always keep track of the cards you’ve already seen, and remember, the dealer must hit until they have 17 or more. **Think like Harvey — know when the game is in your favor and take the right risks.**
- **Know When to Double:** Doubling down can be a great way to increase your winnings, but only do so when the odds are in your favor—especially when you have a total of 10 or 11. **Strategize like Louis Litt: Calculate your next move carefully before you go all in.**
- **Keep Your Cool:** Emotional decisions lead to mistakes. Stay calm and calculated when you make your moves. **Just like Jessica Pearson says, "You always have a choice, you just need to make it wisely."**
- **Bet Wisely:** Don’t bet too much in the early rounds unless you’re confident. Betting the minimum allows you to play more rounds and improve your strategy. **Remember, sometimes it’s better to win slowly, but steadily, like Harvey — rather than make a risky, all-in move that could cost you everything.**
Know When to Hold ‘Em:

If your hand is already strong (like a total of 18 or 19), it might be best to stand and let the dealer sweat.
Don't Be Afraid to Double:

If you have a strong hand (say, 10 or 11), doubling your bet could give you a big payout. But keep an eye on your money—gambling too much can make you lose it all.
Avoid Risky Bets:

Betting too high early on could end your game before you even start. Play it safe until you get a feel for the dealer’s strategy.
Card Counting (Sort of):

If you’re really good, try to keep track of high and low cards. This is, of course, against real-world casino rules, but DeckSmith is a friendly way to practice your counting skills.

Make sure you’re not betting all your chips on a single hand. The game is more about consistency and smart betting than pure luck.
---

## **Conclusion**

Whether you're looking for a casual way to pass the time or want to test your Blackjack skills against a challenging dealer, **DeckSmith** has you covered. With its dynamic features, engaging interface, and realistic gameplay, it offers a unique and exciting Blackjack experience that’s easy to pick up but hard to put down.

Just like in **Suits**, it's all about strategy, reading the game, and making the right moves at the right time. So, **grab your cards, don’t forget the suits, and may the luck of the draw be with you**! 🃏

---
