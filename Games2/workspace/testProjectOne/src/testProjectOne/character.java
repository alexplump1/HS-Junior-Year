package testProjectOne;

public class character {
int health;
int exp;
int gold;

public character()
{
	health = 100;
	exp = 0;
	gold = 0;
}

public void farm(int changeHealth, int changeExp, int changeGold)
{
health = health + changeHealth;
exp = exp + changeExp;
gold = gold + changeGold;

}//public viod ends
}
