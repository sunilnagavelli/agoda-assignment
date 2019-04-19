import java.util.Arrays;

public class Test {

    public static void main(String[] args) {
        Person sunil = Person.of("Sunil");
        Person abhilash = Person.of("Abhilash");
        Person ravteja = Person.of("Raviteja");

        sunil.setFriends(Arrays.asList(abhilash, raviteja));
    }

}