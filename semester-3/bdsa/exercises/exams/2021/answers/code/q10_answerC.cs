using Moq;

public class Tests
{
    [Fact]
    public void Test()
    {
        var gadget = new Gadget("Milk bottle grenades", "The Living Daylights");

        var fake = new Mock<IQService>();
        fake.Setup(x => x.GetRandom()).Returns(gadget);

        IQService service = mock.Object;
    }
}