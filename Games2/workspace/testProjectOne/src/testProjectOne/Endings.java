package testProjectOne;

import java.util.Scanner;

public class Endings {

public static void main(String[] args) {
		// TODO Auto-generated method stub
System.out.print("It was a nice day. Then everything went dark. You wake up in a dark room.");
System.out.print(" You reach a split,\ndo you 1, go left, or 2 go right?");
Scanner scan = new Scanner(System.in);
String userInput = scan.nextLine();
if(userInput.equals("2"))
{
	System.out.print("You went right. ");
	System.out.print("As you go forward there are 3 paths in front of you.");
	System.out.print(" \nDo you go Left 1, Forward 2, or Right 3?");
	Scanner scan2 = new Scanner(System.in);
	String userInput2 = scan2.nextLine();
	if(userInput2.equals("1"))
	{
		System.out.print("You go forward. As you do so you hear faint noises. ");
		Scanner scan3 = new Scanner(System.in);
		String userInput3 = scan3.nextLine();
		if(userInput3.equals("1"))
		{
		//Sees monster	!!!!!!
			System.out.print("You walk into a room, you see the monster, turn around, and run!");
			System.out.print("Left, straight, or Right");
			Scanner scan11 = new Scanner(System.in);
			String userInput11 = scan11.nextLine();
			if(userInput11.equals("1"))
			{
				System.out.print("You reach a split, left or right?");
				Scanner scan12 = new Scanner(System.in);
				String userInput12 = scan12.nextLine();
				if(userInput12.equals("1"))
				{
				System.out.print("You get trapped and die.");
				}
				else if(userInput12.equals("2"))
				{
				System.out.print("You find the end tunnel and the monster doesn't follow you.");	
				}
				else if(userInput12.equals("ee"))
				{
				System.out.print("The monster dies and you win.");	
				}
				else
				{
					System.out.print("That wasn't an option.");
				}
				}
			else if(userInput11.equals("2"))
			{
				System.out.print("You run into a room right into a horde of zombies.");	
//ENDING!!!!!
			}
			else if(userInput11.equals("3"))
			{
				System.out.print("You trip, fall, and die.");	
			}
			else
			{
				System.out.print("That wasn't an option.");	
			}//ending of userInput11
		}
		else if(userInput3.equals("2"))
		{
			System.out.print("You go forward. Left (1) or Right (2)?");
			Scanner scan5 = new Scanner(System.in);
			String userInput5 = scan5.nextLine();
		if(userInput5.equals("1"))
		{
		System.out.print("You find a dead end and turn around.");
		System.out.print(" Do you go straight(1), or right(2)?");
		//!!!!!!!!!!!!!next to easter egg, ending is straight/scan 7
		Scanner scan7 = new Scanner(System.in);
		String userInput7 = scan7.nextLine();
		if(userInput7.equals("1"))
		{
		//good ending	
		System.out.print("You make it out of the cave safe.");
		}
		else if(userInput7.equals("2"))
		{
		System.out.print("You get to a four way do you go left(1), straight(2), or right(3.)");
		//user input 8
		Scanner scan8 = new Scanner(System.in);
		String userInput8 = scan8.nextLine();
		if(userInput8.equals("1"))
		{
//Ending 5!!!!!
		System.out.print("You walk into the dark room right into a horde of zombies.");
		}
		else if(userInput8.equals("2"))
		{
		System.out.print("You reach another 4 way. Left(1), Straight(2), or Right(3).");
		Scanner scan9 = new Scanner(System.in);
		String userInput9 = scan9.nextLine();
		if(userInput9.equals("1"))
		{
		//Knight but continues!!!!!!!!!!code 16
		System.out.print("You find a man with a sword and he will now protect you. ");
		System.out.print("\nYou turn around and see the monster looking around."
				+ " \nWhat do you do? Run(1) Hide(2)");
		Scanner scan16 = new Scanner(System.in);
		String userInput16 = scan16.nextLine();
		if(userInput16.equals("1"))//run
		{
		System.out.print("It hears you running and kills you.");	
		}
		else if(userInput16.equals("2"))//hide
		{
		System.out.print("It sniffs you out and kills you.");	
		} 
		else if(userInput16.equalsIgnoreCase("Jukes"))
		{
			System.out.print("You juke him, leave, and win the game.");
		}
		}
		else if(userInput9.equals("2"))
		{
		//fall to death
			System.out.print("You went left, didn't see it, and fell down a hole to your death.");
		}
		else if(userInput9.equals("3"))
		{	
			System.out.print("You go to a split, do you go right(1) or forward(2.)");	
			Scanner scan10 = new Scanner(System.in);
			String userInput10 = scan10.nextLine();
			if(userInput10.equals("1"))
			{
//ENDING 4!!!!!
			System.out.print("You get back to the start, then a monster comes, traps and kill you.");	
			}
			else if(userInput10.equals("2"))
			{
//ENDING!!!!!
			System.out.print("You were comsumed by the darkness.");	
			}else{System.out.print("That wasn't an option");}
		}
		else
		{
			
		}//ending of userInput9
		}
		else if(userInput.equals("3"))
		{
//ending 6!!!!!
		System.out.print("You walk into a room not seeing the monster and die.");
		}
		else
		{
			System.out.print("That wasn't an option");
		}
		}//ending of userInput 8
		else
		{
		System.out.print("That wasn't an option");	
		}//ending of userInput7
		}
		else if(userInput5.equals("2"))
		{
//ENDING 1!!!!!
		System.out.print("You make it out of the cave safe");
		}
		else
		{
		System.out.print("That wasn't an option");
		}
		}//Input5 ends
		else if(userInput3.equals("3"))
		{
			//!!!!!!!!!! zombie (no knight)
			System.out.print("You walk into the dark room right into a horde of zombies");
		}
		else{
			System.out.print("That wasn't an option");
		}
	}//Input3 Ends
	else if(userInput2.equals("2"))
	{
		System.out.print("You find a man with a sword and he will now protect you. ");
		//Knight!!!!!
		//Knight!!!!!
		System.out.print("\nYou go back to the 4 way, do you go left (1), ");
		System.out.print("forward, back where you started(2), or to the right (3)?");
		Scanner scan4 = new Scanner(System.in);//Knight!!!!!
		String userInput4 = scan4.nextLine();
		if(userInput4.equals("1"))
		{
//ENDING 3!!!!!
		System.out.print("You went left, didn't see it, and fell down a hole to your death.");	
		}
		else if(userInput4.equals("2"))
		{
		System.out.print("You go to a split, do you go right(1) or forward(2)");	
		Scanner scan6 = new Scanner(System.in);
		String userInput6 = scan6.nextLine();
		if(userInput6.equals("1"))
		{
//ENDING 4!!!!!
		System.out.print("You get back to the start, then a monster comes, traps and kill you.");	
		}
		else if(userInput6.equals("2"))
		{
			//ENDING!!!!!
		System.out.print("You were comsumed by the darkness.");	
		}
		else
		{
			System.out.print("That wasn't an option");
		}
		}//Input6 ends
		else if(userInput4.equals("3"))
		{
		System.out.print("You reach a 4 way, do you go left(1), forward(2), or right(3)");
		
		//MONSTER is met here and zombies facing ee2  + knight
		Scanner scan13 = new Scanner(System.in);
		String userInput13 = scan13.nextLine();
		if(userInput13.equals("1"))
		{
		System.out.print("You think the knight can kill the monster, but you both die.");	
		}
		else if(userInput13.equals("2"))
		{
		System.out.print("You find a split left or right");	
		Scanner scan14 = new Scanner(System.in);
		String userInput14 = scan14.nextLine();
		if(userInput14.equals("1"))
		{
		System.out.print("You reach a dead end and the monster kills u both.");	
		}
		else if(userInput14.equals("2"))
		{
		System.out.print("You make it out of the cave safe");
		}
		else if(userInput14.equals("ee"))
		{
		System.out.print("You find the Easter egg, the monster dies, and you both survive.");	
		}
		else
		{
		System.out.print("That wasn't an option");	
		}
		}
		else if(userInput13.equals("3"))
		{
		System.out.print("You walk into a horde of zombies, "
				+ "but the knight kills them all, then the monster comes and kills you.");	
		}
		else
		{
		System.out.print("That wasn't an option");	
		}
		}
		else
		{
		System.out.print("That wasn't an option");	
		}
		}//Input4 ends
	else if(userInput2.equals("3"))
	{
//ENDING 2!!!!!
		System.out.print("You went right, didn't see it, and fell down a hole to your death");
	}
	else
	{
		System.out.print("That wasn't an option");
	}}//Input2 ends
	else if(userInput.equals("ee"))
	{
	System.out.print("You found the secret easter egg ending.");
	}
	else if(userInput.equals("1"))
	{
		System.out.print("You travel left into a darker room.");
//ENDING!!!!!
		System.out.print(" You were consumed by the darkness.");
	}
	else
	{
	System.out.print("That wasn't an option.");
	}
	}//input(1) ends
	}//code ends
//System.out.print();
//Scanner scan = new Scanner(System.in);
//String userInput = scan.nextLine();