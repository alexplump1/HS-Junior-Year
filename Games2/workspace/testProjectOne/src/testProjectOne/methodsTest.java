package testProjectOne;

public class methodsTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	int pAttack = 10;
    int eArmor = 5;
    int damage = dealDamage(pAttack, eArmor);
}
public static int dealDamage(int damage, int armor){
    int damageDealt = damage - armor;
    if(damageDealt < 0)
    {
        damageDealt = 0;
    }
    return damageDealt;
}
}