
import java.util.Scanner;

public class DateParser {
	
	public static int getMonthAsInt(String monthString) {
  	int monthInt;
  	
  	// Java switch/case statement                                                            	
  	switch (monthString) {
     	case "January":
        	monthInt = 1;
        	break;
     	case "February":
        	monthInt = 2;
        	break;
     	case "March":
        	monthInt = 3;
        	break;
     	case "April":
        	monthInt = 4;
        	break;
     	case "May":
        	monthInt = 5;
        	break;
     	case "June":
        	monthInt = 6;
        	break;
     	case "July":
        	monthInt = 7;
        	break;
     	case "August":
        	monthInt = 8;
        	break;
     	case "September":
        	monthInt = 9;
        	break;
     	case "October":
        	monthInt = 10;
        	break;
     	case "November":
        	monthInt = 11;
        	break;
     	case "December":
        	monthInt = 12;
        	break;
     	default:
     	monthInt = 00;
  	}
  	
  	return monthInt;
     	
  	
  	
   }
   public static void main(String[] args) {

while(true) {
	Scanner scnr = new Scanner(System.in);
	String Date = null;
	
	
	DateParser obj = new DateParser();
  	String monthString;
  	String year;
  	String num;
  	int dayeditint = 0;
  	int yearint = 0;
  	

  	System.out.println("Enter a date: ");
  	Date = scnr.nextLine();
  	scnr.nextLine();
  	 
  	
  	
  	if (Date == "-1") {
		break;
	}else {
  		
  		String NameSplit [] = Date.split(" ");
  		monthString = NameSplit[0];
  		num = NameSplit[1];
  		year = NameSplit[2];

  		

  		int monthInt = obj.getMonthAsInt(monthString);
  		
  		
  		int comma = num.indexOf( "," );
  		
  		while (monthInt == 0 || comma == -1){
  	        	System.out.println("Enter a valid month: ");
  	        	monthString = scnr.nextLine();
  	        	scnr.next();
  	        	if(monthString.equals("-1")){
  	        		break;
  	        	}
  	        	comma = num.indexOf( "," );
  	        	

  	   } 
  		String dayedit = num.substring(0, num.length()-1);
  		
  		
  		
  		try {
  	     	dayeditint = Integer.valueOf(dayedit);
  	     	yearint = Integer.valueOf(year);
  	     	
 	
  	  	}catch (Exception NumberFormatException ){ 
  	     	System.out.println("Not Valid Date Inputs. ");
  	     	

  	  		
  	  	} 
  	
  		
  		
  		System.out.println(monthInt+"/"+ dayeditint + "/" + yearint);
  		
  		
  		
  	}
  	}
   }
}



  	
  	
  	
  	
  	
  	
  	
