package testProjectOne;

import java.util.Scanner;

public class loops {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
int x = 0;
for(int i = 0;i<=100;i=i+2)
{
System.out.print(i+", ");}
//Tricky loop begins
Scanner scan = new Scanner(System.in);
int largest = 0;
int userInput = scan.nextInt();
while(userInput != 0)
{
if(userInput < largest)
{
	largest = userInput;
}
userInput = scan.nextInt();
if(userInput == 0)
{
System.out.print(largest);
}
	
}//while loop ends
}}