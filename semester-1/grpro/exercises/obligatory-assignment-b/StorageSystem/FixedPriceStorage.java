
public class FixedPriceStorage extends PhysicalStorage {
    //int keyCounter;
    
    public FixedPriceStorage(String storageId, double price) {
        super(storageId, price);
        
        //keyCounter = 0;
    }

    @Override
    public void addKeyCardNumber(String cardNumber) {
        super.addKeyCardNumber(cardNumber);
        //keyCounter += 1;

        // If the counre is dividable by 3, aka every third time, increase the price 
        // Less efficient than the method below
        //if (keyCounter % 3 == 0){
        //    price += 1000;
        //}

        if (keyCardNumbers.size() % 3 == 0) {
            // If the size is dividable by 3, aka every third time, increase the price 
            // This is a more efficient alternative to the one above, as this one rellies on the build in autoincrementing variable
            price += 1000;
        }
    }
}

