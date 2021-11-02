package testProjectOne;

import java.util.Scanner;

public class tictactoe {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner scan = new Scanner(System.in);
String square1 = scan.nextLine();
int[][] array = new int[3][3];

for(int x = 0; x < array.length; x++){
for(int y = 0; y < array[x].length; y++){
array[0][0]=1;
array[1][0]=2;
array[2][0]=3;
array[0][1]=4;
array[1][1]=5;
array[2][1]=6;
array[0][2]=7;
array[1][2]=8;
array[2][2]=9;


System.out.print("Where would you like to go?");
Scanner scan1 = new Scanner(System.in);
int move1 = scan1.nextInt();
while(move1 < 1 || move1 > 9){
	 if(move1 == 1)
{
		 
}
else if(move1 == 2)
{
	
}
else if(move1 == 3)
{
	
}
else if(move1 == 4)
{
	
}
else if(move1 == 5)
{
	
}
else if(move1 == 6)
{
	
}
else if(move1 == 7)
{
	
}
else if(move1 == 8)
{
	
}
else if(move1 == 9)
{
	
}
else
{
	System.out.print("Incorrect move, try again.");
}//else ends
}//while loop ends

}//y ends
}//x ends
}//main string

	
}
//class ends