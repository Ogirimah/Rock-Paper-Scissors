# Rock-Paper-Scissors

The rock-paper-scissors task for the Zuri training

The link to the raw code of the Rock-Paper-Scissors game is [this](https://github.com/Ogirimah/Rock-Paper-Scissors/blob/main/main.py "Links to the code")

### How to Play the Game

Rock-Paper-Scissors is a game played between only two people, where they traditionally use their fist to indicate either of the three options available in the game:
* Rock -> Folded fist
* Paper -> Open hand
* Scissors -> Index and middle fingers open, while the remaining fingers are folded

### Rule to Determine the Wminner

The below rules  used to determine the winner based on the choices of the two players:
* If both players show same fist, the game is a tie
* **Rock** breaks **Scissors**
* **Scissors** cuts **Paper**
* **Paper** beats **Rock**

To learn more about how to play the game watch this [video](https://www.youtube.com/watch?v=ND4fd6yScBM "Youtube video").
You can also read more on [wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors)

## Code Implementation

The code pits the **player** against **CPU**, and determines the winner by comparing the input choice of the user with that of the CPU.

The pseudocode of the program is as follows

1. Initialize the program and keep it running
2. Create a list containing the game choices
3. Randomly select a choice for CPU
4. Get choice input for the user
5. Compare user choice with that of CPU
6.  If it is a tie, go back to *step 3*
7.  Print the result
8. Prompt if user wants to play again or quit
9. Stop program from running
