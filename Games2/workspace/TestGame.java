		// TODO Auto-generated method stub
	character plains = new character();
	plains.farm(-2,10,5);
	
	character riverside = new character();
	riverside.farm(-3,15,10);
	
	character desert = new character();
	desert.farm(-4,20,15);
	
	character ruins = new character();
	ruins.farm(-5,25,20);
	
	character tundra = new character();
	tundra.farm(-6,30,25);
	
	character ocean = new character();
	ocean.farm(-7,35,30);
	//forest, riverside, desert, ruins, tundra, ocean
int gold = 0;
int lvl = 1;
int exp = 0;
int health = 100;
int armor = 0;
boolean mesDisplay = false;
int regen = 0;
boolean mast = false;
boolean hull = false;
boolean wheel = false;
boolean gunport = false;
System.out.print("Username:");
Scanner scan = new Scanner(System.in);
String username = scan.nextLine();
System.out.print("You're a person who grew up in the rich lands. "
		+ "\nYou're retrieving loot for your queen. "
		+ "\nPirates chase you and the boat goes down and your the only one left. "
		+ "\nA magic portal is on the island and will trade stuff for gold. "
		+ "\nGold is earned from killing monsters.");
System.out.print("(press enter to continue)");
Scanner scan1 = new Scanner(System.in);
String userInput1 = scan1.nextLine();
if(userInput1.equalsIgnoreCase("ee"))
{
	System.out.print("GG you win");
}
else
{	
System.out.print("\nType 'stats' to see stats");	
while(mast == false || hull == false || wheel == false || gunport == false){
if(exp >= 90 + (10 * lvl)){
	exp = exp - (90 + (10 * lvl));
	lvl = lvl + 1;
}
if(lvl == 100 && mesDisplay == false){
	System.out.print("Regen armor available, new biome void, lvl 200+");
	mesDisplay = true;
}//message ends
System.out.print("\nWhere would you like to go?"
		+ "\n Shop, Biomes, or Hospital?");

if(health <= 0){
	gold = gold / 5;
	lvl = lvl - 5;
	if (lvl < 1){
		lvl = 1;
	}
	health = 100;
	System.out.print("\nHealth is " + health + "/" + (95 + (5 * lvl))
			+ "\n You ran out of health and lost.");
	}

Scanner scan2 = new Scanner(System.in);
String userInput2 = scan2.nextLine();
if(userInput2.equalsIgnoreCase("shop") || userInput2.equals("1"))
{
	System.out.print("What would you like Armor, Weapons, or Equipment?");
	Scanner scan3 = new Scanner(System.in);
	String userInput3 = scan3.nextLine();
	if(userInput3.equalsIgnoreCase("armor"))
	{
	if(lvl < 100){	
	System.out.print("Which armor? ");
	System.out.print("Stone(200), Iron(500), Egyptian(1,000), Godly(5,000), Void(50,000)");
	}else{
		System.out.print("Which armor? ");
		System.out.print("Stone(200), Iron(500), Egyptian(1,000), Godly(5,000), Void(50,000)");
		System.out.print(", Regen(10,000)");
	}//>lvl 100	
	Scanner scan6 = new Scanner(System.in);
	String userInput6 = scan6.nextLine();
	if(userInput6.equalsIgnoreCase("test"))
	{
	gold = gold - 10;
	armor = armor + 1;
	System.out.print("Test armor bought");
	}//test armor
	else if(userInput6.equalsIgnoreCase("stone")){
		if(gold >= 200){
		gold = gold - 200;
		armor = armor + 2;
		System.out.print("Stone armor bought");
		}//stone armor
		else{
			System.out.print("Not enough gold");
		}//stone armor ends
	}
	else if(userInput6.equalsIgnoreCase("iron")){
		if(gold >= 500){
		gold = gold - 500;
		armor = armor + 5;
		System.out.print("Iron armor bought");
		}//iron armor
		else{
			System.out.print("Not enough gold");
		}//iron armor ends
	}//gold amount ends
	else if(userInput6.equalsIgnoreCase("egyptian")){
		if(gold >= 1000){
		gold = gold - 1000;
		armor = armor + 15;
		System.out.print("Egyptian armor bought");
	}//egyptian armor
		else{
			System.out.print("Not enough gold");
		}//eg armor ends
	}//gold amount ends
	else if(userInput6.equalsIgnoreCase("godly")){
		if(gold >= 5000){
		gold = gold - 5000;
		armor = armor + 50;
		System.out.print("Godly armor bought");
		}//godly armor
		else{
			System.out.print("Not enough gold");
		}//godly armor ends
	}//gold amount ends
	else if(userInput6.equalsIgnoreCase("void")){
		if(gold >= 50000){
		gold = gold - 50000;
		armor = armor + 100;
		System.out.print("Void armor bought");
		}//void armor
		else{
			System.out.print("Not enough gold");
		}//void armor ends
	}//gold amount ends
	else if(userInput6.equalsIgnoreCase("regen")){
		if(gold >= 10000){
		gold = gold - 100;
		armor = armor + 9999;
		regen = 20;
		System.out.print("Regen armor bought");
		System.out.print("\nYou now get +20 health from every biome done");
		}//regen armor
		else{
			System.out.print("Not enough gold");
		}//regen armor ends
	}//gold amount ends
	else{
		System.out.print("No armor was bought");
	}//which armor ends
	}//armor ends
	else if(userInput3.equalsIgnoreCase("weapons"))
	{
		System.out.print("weapons coming soon");
	}//weapons ends
	else if(userInput3.equalsIgnoreCase("equipment"))
	{
		System.out.print("What equipment would you like? ");
		System.out.print("gunport(5,000), hull(25,000), mast(10,000), wheel(500)");
		Scanner scan7 = new Scanner(System.in);
		String userInput7 = scan7.nextLine();
		if(userInput7.equalsIgnoreCase("gunport")){
			if(gold >= 5000){
				gold = gold - 5000;
				gunport = true;
			}else{
				System.out.print("Not enough money");
			}//not enough money
		}//gun port ends
		else if(userInput7.equalsIgnoreCase("hull")){
			if(gold >= 25000){
				gold = gold - 25000;
				hull = true;
			}else{
				System.out.print("Not enough money");
			}//not enough money
		}//hull ends
		else if(userInput7.equalsIgnoreCase("mast")){
			if(gold >= 10000){
				gold = gold - 10000;
				mast = true;
			}else{
				System.out.print("Not enough money");
			}//not enough money
		}//mast ends
		else if(userInput7.equalsIgnoreCase("wheel")){
			if(gold >= 500){
				gold = gold - 500;
				wheel = true;
			}else{
				System.out.print("Not enough money");
			}//not enough money
		}//wheel ends
		else
		{
		System.out.print("Returning to Main Menu");	
		}//what equipment? ends
	}//equipment ends
	else
	{
		System.out.print("Back to main menu.");	
	}//shop input ends
}//Shop if else ends
else if(userInput2.equalsIgnoreCase("biomes") || userInput2.equals("2"))
{
	if(lvl < 100){
	System.out.print("Where would you like to go?");
	System.out.print("\nPlains lvl 0 "
			+ "\nForest lvl 10 "
			+ "\nRiverside lvl 20 "
			+ "\nDesert lvl 35 "
			+ "\nRuins lvl 50 "
			+ "\nTundra lvl 75"
			+ "\nOcean lvl 100");
	}else{
		System.out.print("Where would you like to go?");
		System.out.print("\nPlains lvl 0 "
				+ "\nForest lvl 10 "
				+ "\nRiverside lvl 20 "
				+ "\nDesert lvl 35 "
				+ "\nRuins lvl 50 "
				+ "\nTundra lvl 75"
				+ "\nOcean lvl 100 "
				+ "\nVoid lvl 200");
	}
Scanner scan4 = new Scanner(System.in);
	String userInput4 = scan4.nextLine();
	if(userInput4.equalsIgnoreCase("plains") || userInput4.equals("1"))
	{
		int damage1 = 2 - armor;
	if(damage1 > 0){
		System.out.print("+10 gold, +10xp, -" + damage1 + " health");
		gold = gold + 10000;
		exp = exp + 10;
		//exp = exp + 58410; //max
		//lvl = lvl + 100;
		}else{
		System.out.print("+10 gold, +10xp, -0 health");
	}//else ends
		if(armor > 2){
		}//no damage taken ends
		else{
			health = health - 2 + armor + regen;
		}//damage ends
	}//plains end
	else if(userInput4.equalsIgnoreCase("forest") || userInput4.equals("2"))
	{
		if(lvl >= 10)
		{
			int damage2 = 5 - armor;
			if(damage2 > 0){
				System.out.print("+15 gold, +15xp, -" + damage2 + " health");
				gold = gold + 10;
				exp = exp + 10;
				}//damage taken
			else{
				System.out.print("+15 gold, +15xp, -0 health");
			}//no damage taken
				if(armor > 5){
				}else{
					health = health - 5 + armor + regen;
				}//damage ends
		}//if > lvl 10 ends
		else
		{
			System.out.print("Not high enough level");
		}//not high enough level	
	}//forest ends
	else if(userInput4.equalsIgnoreCase("riverside") || userInput4.equals("3"))
	{
		if(lvl >= 20)
		{		
			int damage3 = 8 - armor;
			if(damage3 > 0){
				System.out.print("+25 gold, +20xp, -" + damage3 + " health");
				gold = gold + 25;
				exp = exp + 20;
				}else{
				System.out.print("+25 gold, +20xp, -0 health");
			}
				if(armor > 8){
				}else{
					health = health - 8 + armor + regen;
				}//damage ends
		}
		else
		{
			System.out.print("Not high enough level");
		}//not high enough level
	}//riverside ends
	else if(userInput4.equalsIgnoreCase("desert") || userInput4.equals("4"))
	{
		if(lvl >= 35)
		{			
			int damage4 = 10 - armor;
			if(damage4 > 0){
				System.out.print("+35 gold, +25xp, -" + damage4 + " health");
				gold = gold + 35;
				exp = exp + 25;
				}else{
				System.out.print("+35 gold, +25xp, -0 health");
			}
				if(armor > 10){
				}else{
					health = health - 10 + armor + regen;
				}//damage ends
		}
		else
		{
			System.out.print("Not high enough level");
		}//not high enough level
	}//desert ends
	else if(userInput4.equalsIgnoreCase("ruins") || userInput4.equals("5"))
	{
		if(lvl >= 50)
		{			
			int damage5 = 15 - armor;
			if(damage5 > 0){
				System.out.print("+50 gold, +30xp, -" + damage5 + " health");
				gold = gold + 10;
				exp = exp + 10;
				}else{
				System.out.print("+50 gold, +30xp, -0 health");
			}
				if(armor > 15){
				}else{
					health = health - 15 + armor + regen;
				}//damage ends
		}
		else
		{
			System.out.print("Not high enough level");
		}//not high enough level	
	}//ruins ends
	else if(userInput4.equalsIgnoreCase("tundra") || userInput4.equals("6"))
	{
		if(lvl >= 75)
		{			
			int damage6 = 20 - armor;
			if(damage6 > 0){
				System.out.print("+75 gold, +35xp, -" + damage6 + " health");
				gold = gold + 75;
				exp = exp + 35;
				}else{
				System.out.print("+75 gold, +35xp, -0 health");
			}
				if(armor > 20){
				}else{
					health = health - 20 + armor + regen;
				}//damage ends
		}
		else
		{
			System.out.print("Not high enough level");
		}//not high enough level
	}//tundra ends
	else if(userInput4.equalsIgnoreCase("ocean") || userInput4.equals("7"))
	{
		if(lvl >= 100)
		//if(lvl > 0)
		{			
			int damage7 = 30 - armor;
			if(damage7 > 0){
				System.out.print("+100 gold, +40xp, -" + damage7 + " health");
				gold = gold + 100;
				exp = exp + 40;
				//exp = exp + 58410; //max
				}else{
				System.out.print("+100 gold, +40xp, -0 health");
			}
				if(armor > 30){
				}else{
					health = health - 30 + armor + regen;
				}//damage ends
		}
		else
		{
			System.out.print("Not high enough level");
		}//not high enough level
	}//ocean ends
	else if(userInput4.equalsIgnoreCase("void") || userInput4.equals("8"))
	{
		if(lvl >= 200)
		//if(lvl > 0)
		{			
			int damage8 = 10000 - armor;
			if(damage8 > 0){
				System.out.print("+1000 gold, +500xp, -" + damage8 + " health");
				gold = gold + 1000;
				exp = exp + 500;
				}else{
				System.out.print("+1000 gold, +500xp, -0 health");
			}
				if(armor > 10000){
				}else{
					health = health - 10000 + armor + regen;
				}//damage ends
		//lvl = lvl + 5;
		//System.out.print("5 lvls gained");
		}
		else
		{
			if(lvl >= 100)
			{
			System.out.print("Not high enough level");
			}
			else
			{}
		}//not high enough level
	}//ocean ends	
	else
	{
		System.out.print("Back to main menu");
	}//userInput4 ends
}
	else if(userInput2.equalsIgnoreCase("hospital") || userInput2.equals("3"))
		if(health < 95 + (5 * lvl)){
{
	if(gold > 10){
		gold = gold - 10;
		health = 95 + (5 * lvl);
		System.out.print("-10 gold \nMax health");
	}//buy health ends
	else
{
		health = 95 + (5 * lvl);
		System.out.print("Max health");
}//else ends
}//free health
}//max health ends
	else{
	System.out.print("Alreday max health");
}//hospital ends
	else if(userInput2.equalsIgnoreCase("stats"))
{
	System.out.print("gold:" + gold + " health:" + health +" xp:" + exp + "/" + 
(90 + (10*lvl)) + " lvl:" + lvl + " armor:" + armor);
}//stats ends
else
{
}//loops to main menu
}//userInput2 ends
}//while loop ends
//{
System.out.print("You make a boat and a new journey begins.");
System.out.print(" Your boat is doing well \nYou forgot about the pirates."
		+ " Good thing you made a gunport.");