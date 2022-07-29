/*
 This program was not written my junior year of highschool.
 It was written during my last week of my first internship.
 */

namespace OhHell
{
    internal class Program
    {
        // List for cards not in hands
        public static List<Card> availableCards = new List<Card>();
        public static int[] Points = { 0 };

        static void Main(string[] args)
        {
            int numOfOpponents = 0;

            // Getting number of opponent bots
            while (true) {
                Console.Write("How many opponents would you like to play against (1-7): ");
                String userResponse = Console.ReadLine();
                try
                {
                    numOfOpponents = Int32.Parse(userResponse);
                    if (numOfOpponents >= 1 && numOfOpponents <= 7) { break; }
                } catch {}
            }
            
            Play(numOfOpponents + 1);
        }

        private static int startingPlayerIndex = 0;
        private static void Play(int numOfPlayers) {
            // Find how many decks are being used
            int decksUsed = CreateCards(numOfPlayers);
            int cardsUsed = 52 * decksUsed;

            // Rounds up the river
            for (int i = 1; i <= ((cardsUsed-1) / numOfPlayers); i++) {
                ExecuteRound(i, numOfPlayers);
                startingPlayerIndex++;
                CreateCards(numOfPlayers);
            }

            Console.WriteLine("\nGoing Back Down the River\n");

            // Rounds down the river
            for (int i = (cardsUsed-1)/ numOfPlayers; i >= 1; i--) {
                ExecuteRound(i, numOfPlayers);
                startingPlayerIndex++;
                CreateCards(numOfPlayers);
            }
        }

        // Returns how many decks will be used
        private static int CreateCards(int numOfPlayers) {
            int decksNeeded = (numOfPlayers / 9) + 1;

            availableCards.Clear();
            for (int i = 0; i < decksNeeded; i++) {
                Card.populateDeck();
            }

            return decksNeeded;
        }

        public static void ExecuteRound(int startCardCount, int numOfPlayers) {
            // At this point, there are n number of players, while adequate cards where
            // total cards >= trump card + startCardCount * numOfPlayers

            // List of player and bot hands
            List<List<Card>> hands = new List<List<Card>>(numOfPlayers);
            for (int i = 0; i < numOfPlayers; i++) {
                hands.Add(new List<Card>());
            }
            int[] bets = new int[numOfPlayers];

            // Putting cards in each player's hand
            Random rand = new Random();
            for (int i = 0; i < startCardCount; i++) {
                for (int j = 0; j < numOfPlayers; j++) {
                    int removedIndex = rand.Next(availableCards.Count());
                    hands.ElementAt(j).Add(availableCards.ElementAt(removedIndex));
                    availableCards.RemoveAt(removedIndex);
                }
            }

            // Generate Trump Card
            int trumpIndex = rand.Next(availableCards.Count());
            Card trumpCard = availableCards.ElementAt(trumpIndex);
            availableCards.RemoveAt(trumpIndex);

            //Print the trump card
            Console.WriteLine($"Trump card is {trumpCard.S_Value} of {trumpCard.Suit}\n");

            //Print User's card to them
            Console.Write($"Your Cards: ");
            for (int i = 0; i < startCardCount; i++) {
                Card iterCard = hands.ElementAt(0).ElementAt(i);
                Console.Write(iterCard.S_Value + " of " + iterCard.Suit + ", ");
            }
            Console.WriteLine("");

            // Start Betting
            Console.WriteLine($"There are {startCardCount} cards this round");
            for (int i = 0; i < numOfPlayers; i++) {
                int currentPlayer = (startingPlayerIndex + i) % numOfPlayers;
                if (currentPlayer == 0) {
                    // Betting prompt for player
                    while (true)
                    {
                        Console.Write("What will be your bet? ");
                        string userResponse = Console.ReadLine();
                        try {
                            bets[0] = Int32.Parse(userResponse);
                            break;
                        } catch { Console.WriteLine();}
                    }
                } else {
                    // Betting calculation for bots, can be optimized
                    int numOfTrumps = 0;
                    for (int j = 0; j < startCardCount; j++) {
                        if (hands.ElementAt(currentPlayer).ElementAt(j).Suit.Equals(trumpCard.Suit))
                            numOfTrumps++;
                    }
                    bets[currentPlayer] = numOfTrumps / 2;
                    Console.WriteLine($"Player {currentPlayer} bets {bets[currentPlayer]}");
                }
            }

            Console.WriteLine("---  Starting Round  ---");

            // Playing the round
            int startingPlayer = startingPlayerIndex;
            while (hands.ElementAt(0).Count() > 0) {
                string startingSuit = "";
                Card[] currentTrickCards = new Card[numOfPlayers];

                // Iterate through player turns
                for (int i = 0; i < numOfPlayers; i++) {
                    int currentPlayer = (startingPlayer + i) % numOfPlayers;
                    if (currentPlayer == 0) {
                        // Print cards to player
                        Console.WriteLine("Your Cards are: ");
                        for (int j = 0; j < hands.ElementAt(0).Count(); j++) {
                            Card iterCard = hands.ElementAt(0).ElementAt(j);
                            Console.WriteLine($"{j+1}. {iterCard.S_Value} of {iterCard.Suit}");
                        }

                        // Asking user to play card
                        while (true) {
                            Console.Write("Which card would you like to play? ");
                            string userResponse = Console.ReadLine();
                            try {
                                Card choosenCard = hands.ElementAt(0).ElementAt(Int32.Parse(userResponse)-1);
                                if (!startingSuit.Equals("") && !choosenCard.Suit.Equals(startingSuit)) {
                                    throw new InvalidOperationException("");
                                } else if (startingSuit.Equals("")) {
                                    startingSuit = choosenCard.Suit;
                                }
                                currentTrickCards[0] = choosenCard;
                                hands.ElementAt(0).RemoveAt(Int32.Parse(userResponse)-1);
                                break;
                            } catch {}

                            // Printing to user they must select a valid card
                            if (!startingSuit.Equals("")) {
                                Console.WriteLine("You must play a " + startingSuit.Substring(0, startingSuit.Length - 1));
                            }
                            else {
                                Console.WriteLine("Invalid Selection");
                            }
                        }
                        
                    } else {
                        // Choose card for bot, right now it is first (playable) card in hand, can be optimized

                        if (startingSuit.Equals("")) {
                            Card playedCard = hands.ElementAt(currentPlayer).ElementAt(0);
                            hands.ElementAt(currentPlayer).RemoveAt(0);
                            startingSuit = playedCard.Suit;
                            currentTrickCards[currentPlayer] = playedCard;

                            Console.WriteLine($"Player {i} played {playedCard.S_Value} of {playedCard.Suit}");
                        } 
                        else {
                            for (int j = 0; j < hands.ElementAt(currentPlayer).Count; j++) {
                                if (hands.ElementAt(currentPlayer).ElementAt(j).Suit.Equals(startingSuit)) {
                                    Card playedCard = hands.ElementAt(currentPlayer).ElementAt(j);
                                    hands.ElementAt(currentPlayer).RemoveAt(j);
                                    currentTrickCards[currentPlayer] = playedCard;

                                    Console.WriteLine($"Player {i} played {playedCard.S_Value} of {playedCard.Suit}");
                                    j = 100;
                                    break;
                                }
                            }

                            // Suit could not be followed, choose the first card
                            if (currentTrickCards[currentPlayer] == null) {
                                Card playedCard = hands.ElementAt(currentPlayer).ElementAt(0);
                                hands.ElementAt(currentPlayer).RemoveAt(0);
                                currentTrickCards[currentPlayer] = playedCard;

                                Console.WriteLine($"Player {i} played {playedCard.S_Value} of {playedCard.Suit}");
                            }
                        }
                    }
                }

                // Calculate who won the trick
                Card bestCard = currentTrickCards[0];
                int bestCardPlayer = 0;
                for (int i = 1; i < numOfPlayers; i++) {
                    if (isBetterCard(bestCard, currentTrickCards[i], trumpCard.Suit, startingSuit)) {
                        bestCard = currentTrickCards[i];
                        bestCardPlayer = i;
                    }
                }


                Console.WriteLine($"Player {bestCardPlayer} won with a {bestCard.S_Value} of {bestCard.Suit}");
            }

            // Printing scores

        }

        private static bool isBetterCard(Card bestCard, Card newCard, string trumpSuit, string startSuit) {
            if (!bestCard.Suit.Equals(trumpSuit) && newCard.Suit.Equals(trumpSuit)) {
                return true;
            } else if (bestCard.Suit.Equals(trumpSuit) && !newCard.Suit.Equals(trumpSuit)) {
                return false;
            }
            if (!bestCard.Suit.Equals(startSuit) && newCard.Suit.Equals(startSuit)) {
                return true;
            }
            else if (bestCard.Suit.Equals(startSuit) && !newCard.Suit.Equals(startSuit)) {
                return false;
            }

            // Same type (or irrelevant corner case)
            return bestCard.Value < newCard.Value;
        }
    }
}
