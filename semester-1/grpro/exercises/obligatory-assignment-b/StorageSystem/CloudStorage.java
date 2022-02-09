
/**
 * Write a description of class CloudStorage here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class CloudStorage extends Storage
{
    private int sizeGB;
    private String accessKey;

    public CloudStorage(String storageId, int sizeGB, String accessKey)
    {
        super(storageId, (sizeGB * 0.15));

        this.sizeGB = sizeGB;
        this.accessKey = accessKey;
    }

    public void display() {
        super.display();

        System.out.println("Cloud space: " + sizeGB + "GB");
        System.out.println("Access key: " + accessKey);
    }
}
