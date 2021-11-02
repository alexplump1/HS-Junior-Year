package testProjectOne;

import java.util.Scanner;

public class Scamming {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.print("Enter your name: ");
Scanner scan = new Scanner(System.in);
String userInput = scan.nextLine();
System.out.print("Hello " + userInput);
System.out.println("\nWhat is your favorite color " + userInput + "?");
Scanner scan2 = new Scanner(System.in);
String userInput2 = scan2.nextLine();
if(userInput2.equalsIgnoreCase("green")){ 	 
    System.out.println("That's my favorite color too.");
}else{
	System.out.println(userInput2 + " is a cool color");
}
Scanner scan3 = new Scanner(System.in);
String userInput3 = scan3.nextLine();
if(userInput3.equals("1")){
System.out.print("1 is real neat");
}
else{
	System.out.print(userInput3 + " is undifined");
}}}
