# Exploding Kittens Game

This Python program simulates a part of the popular game *Exploding Kittens* with three players. In particular, it implements the Cat cards (MoniCat, DaniCat, TomiCat, and NicoCat), which allow a player to steal a card from another player when two identical Cat cards are played. Additionally, the program handles the game mechanics of playing cards like Skip, Favor, and managing the Exploding Kitten cards.

This project was developed for the *Introduction to Programming* course during the second semester of 2019 as part of my first year in Civil Engineering at the Pontificia Universidad Católica de Chile.

## Features

- Handle a deck of cards containing Skip, Favor, Exploding Kitten, and Cat cards.
- Simulate player turns where players can choose to play cards or draw from the deck.
- Implement the Cat card stealing mechanism.
- Manage the game flow, ending when two players draw an Exploding Kitten.
- Save game state in an output file.

## How to Run

1. Make sure you have Python installed (version 3.x).
2. Clone this repository or download the files.
3. Run the program with:

```bash
python main.py
```

### Input Format

The program expects the following inputs:

1. Deck: A string of cards separated by commas. Example:

```
"Skip,Favor,ToMiCat,Skip,Skip,MoniCat,Favor,DaniCAt,Skip,ToMiCat,NicoCat,DaniCAt"
```

2. Player Names: A string of three player names separated by commas. Example:

```
"Nicolás,Mónica,Daniela"
```

3. Player Hands: Each player's hand consists of 6 cards, provided as individual strings. Example:

```
"Skip,Favor,Skip,NicoCat,MoniCat,Favor"
```

4. Commands: The game accepts these commands:

Robar: The current player draws a card from the deck.
Jugar: The player chooses to play a card. Additional inputs specify which card to play.
Imprimir Estado: Prints the current game state.

#### Example of Execution

Input:

```
Deck: "Skip,Favor,ToMiCat,Skip,MoniCat,Favor,DaniCAt,NicoCat"
Player Names: "Nicolás,Mónica,Daniela"
Hands:  "Skip,Favor,Skip,NicoCat,MoniCat,Favor"
        "Favor,TomiCat,Skip,TomiCat,MoniCat"
        "MoniCat,DaniCat,Skip,DaniCat,Favor"
Command: Jugar
Card: Skip
```

Output:

```
Nicolás ha jugado Skip
```

#### Special Cases

If a player draws an Exploding Kitten, the program prints "X ha explotado" and that player is out of the game.
If two players explode, the game ends with a message declaring the winner:
```
El juego ha terminado
Daniela ha ganado
```

### Game State Output Example

```
Cartas restantes: 10
Mano Nicolás: ['Favor', 'Skip', 'NicoCat', 'MoniCat']
Mano Mónica: ['Favor', 'TomiCat', 'Skip', 'MoniCat']
Mano Daniela: ['MoniCat', 'DaniCat', 'Skip', 'Favor']
```

If a player explodes, their hand will be replaced with KABOOM!:

```
Cartas restantes: 5
Mano Nicolás: KABOOM!
Mano Mónica: ['Favor', 'TomiCat', 'Skip']
Mano Daniela: ['MoniCat', 'DaniCat', 'Skip', 'Favor']
```

### Conclusion

This program simulates part of the game Exploding Kittens by handling player actions such as drawing, playing cards, and dealing with Exploding Kitten cards. The project demonstrates basic game logic and handling reading/writing files in Python.
