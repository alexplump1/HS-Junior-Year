package testProjectOne;

public class recursion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	System.out.println(fib(40));
	System.out.println(recur(16));
	System.out.println(fib(7));
	
	}
	
	
	public static int recur(int a){
	if(a > 1){
		return a * recur(a - 1);
		
			
		
	}else{
		return 1;
	}
		
	}
public static int fib(int a){
	if(a == 1 || a ==2 ){
		return 1;
	}else{
		return fib(a - 1) + fib(a - 2);
	}
	
}
	
	
}