using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OhHell
{
    internal class Card
    {
        public static string[] Suits = { "Spades", "Clubs", "Diamonds", "Hearts"};
        public static string[] Values = { "2", "3", "4", "5", "6", "7", "8", "9", 
                                          "10", "Jack", "Queen", "King", "Ace"};

        public string Suit { get; set; }
        public string S_Value { get; set; }      //This is card value as string, king -> K
        public int Value { get; set; }           //This is card value as int, king -> 13

        public Card(int suitIndex, int valueIndex) {
            this.Suit = Suits.ElementAt(suitIndex);
            this.S_Value = Values.ElementAt(valueIndex);
            this.Value = valueIndex + 2;
        }

        public static void populateDeck() {
            for (int i = 0; i < Suits.Count(); i++) {
                for (int j = 0; j < Values.Count(); j++) {
                    Program.availableCards.Add(new Card(i, j));
                }
            }
        } 

    }
}
