import java.util.*;

public class unique{
    public static void main(String[] args){
	System.out.println("Hello,java!\n");
	String myword = "This is a java test";
	char[] mychar = {'T','h','i','s'};
	System.out.println(myword+" size is " + myword.length());
	System.out.println(myword.toCharArray()[0]);

	Map<Character, Integer> container = new HashMap<Character, Integer>(myword.length());
	for(Character i : myword.toCharArray()){
	    System.out.println(i);
	    if(container.containsKey(i)){
		System.out.println("this is not a unique");
		break;
	    }else{
		container.put(i,1);
	    }
	}
	
    }
}
