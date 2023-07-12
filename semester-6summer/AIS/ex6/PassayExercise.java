import java.util.ArrayList;
import java.util.List;

import org.passay.CharacterRule;
import org.passay.EnglishCharacterData;
import org.passay.LengthRule;
import org.passay.Rule;
import org.passay.PasswordData;
import org.passay.PasswordValidator;
import org.passay.RuleResult;

public class PassayExercise {
    public static void main(String[] args) {
        
	List<Rule> rules = new ArrayList<>();        
	//Rule 1: Password length should be in between 15-25
	rules.add(new LengthRule(15, 25));

	//TODO: rules in the exercise document     
        
	PasswordValidator validator = new PasswordValidator(rules);        
	PasswordData password = new PasswordData(args[0]);        
	RuleResult result = validator.validate(password);
        
	if(result.isValid()){
	    System.out.println("Password validated.");
	} else {
	    System.out.println("Invalid Password: " + validator.getMessages(result));            
        }
    }
}
