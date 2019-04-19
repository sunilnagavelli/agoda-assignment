import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;

public class Person {

    String name;
    List<Person> friends = new LinkedList<>();

    public void setFriends(List<Person> friends) {
        this.friends = friends;
    }
    public static of(String name) {
        Person p = new Person();
        p.name = name;
    }

    @Override
    public String toString() {
        return name.toString();
    }
    // method to check whether two person are equal or not
    @Override
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }

        if (!Person.class.isAssignableFrom(obj.getClass())) {
            return false;
        }

        final Person other = (Person) obj;
        if ((this.name == null) ? (other.name != null) : !this.name.equals(other.name)) {
            return false;
        }
        return true;
    }
    // method to assign different hash code to each initialized person object
    @Override
    public int hashCode() {
        int hash = 3;
        hash = 53 * hash + (this.name != null ? this.name.hashCode() : 0);
        return hash;
    }

    List<Person> friendsOfFriends() {
        List<Person> friendOfFriends = new LinkedList<>();
        friends.stream().forEach(friend -> {
            friend.friends.stream().filter(friendOfFriend -> friends.contains(friendOfFriend))
                    .forEach(friendOfFriends::add);
        });
        return friendOfFriends;
    }

}
