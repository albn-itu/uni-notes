
public class Storage
{
    protected String storageId;
    protected double price;

    public Storage(String storageId, double price) {
        this.storageId = storageId;
        this.price = price;
    }

    /* Show storage info */
    public void display() {
        System.out.println(" ** STORAGE INFO ** ");
        System.out.println("ID: " + storageId);
        System.out.println("Price: " + price);
    }
}
