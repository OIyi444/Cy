package final_assessment;
import java.util.*;

public class Reminder {
	String time, water, medicine, exercise;
	
	public void Reminder(String time, String water, String medicine, String exercise) {
		this.time = time;
		this.water = water;
		this.medicine = medicine;
		this.exercise = exercise;
	}
	
	public void addReminder() {
		Scanner input = new Scanner(System.in);
		ArrayList<String>StoreReminder;
		
		System.out.println("Enter the time: ");
		String time = input.nextLine();
		
		System.out.println("Enter Leter of water: ");
		String water = input.nextLine();
		
		System.out.println("Enter medicine: ");
		String medicine = input.nextLine();
		
		System.out.println("Enter exercise: ");
		String exercise = input.nextLine();
	}
	
	public void viewReminder() {
		System.out.println("time: " + time);
		System.out.println("water: " + water);
		System.out.println("medicine: " + medicine);
		System.out.println("exercise: " + exercise);
	}
	
	
	public static void main(String [] args) {
		Reminder r = new Reminder();
		Scanner input = new Scanner(System.in);
		
		System.out.println("== Main Menu ==");
		System.out.println("1. add Reminder");
		System.out.println("2. View reminder");
		System.out.println("3. Exit");
		
		while (true) {
			int choice = input.nextInt();
			input.nextLine();
		
			if(choice == 1) {
				r.addReminder();
			}
			else if (choice == 2) {
				r.viewReminder();
			}
			else {
				System.out.println("Thanks for using Dailt Health Tracker ");
				break;
			}
		}
		
	}
}
