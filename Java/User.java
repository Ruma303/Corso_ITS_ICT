class User {

    static {
        int numberOfUsers = 0;
    }
    public String name = "";
    public String lastname = "";
    public Integer phoneNumber = 0;

    User(String name, String lastname, Integer phoneNumber) {
        this.name = name;
        this.lastname = lastname;
        this.phoneNumber = phoneNumber;
    }
}
