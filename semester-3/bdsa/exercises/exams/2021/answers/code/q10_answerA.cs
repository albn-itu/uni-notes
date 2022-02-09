public class Double0Tests
{
    [Theory]
    [InlineData(006, "Alec Trevelyan")]
    [InlineData(007, "James Bond")]
    public void Given_00_Number_Return_Agent(int input, string expected)
    {
        // Arrange
        var agents = new Double0();

        // Act
        var actual = agents.Agent(input);

        // Assert
        Assert.Equal(expected, actual);
    }

    [Fact]
    public void Given_000_Throw_ArgumentOutOfRangeException()
    {
        // Arrange
        var agents = new Double0();

        // Act and assert
        Assert.Throws<ArgumentOutOfRangeException>(() => agents.Agent(000));
    }
}