[Route("[controller]")]
[ApiController]
public class GeniusController : ControllerBase {
    private readonly GeniusRepository _geniusRepository;

    public GeniusController(GeniusRepository geniusRepository) {
        _geniusRepository = geniusRepository;
    }

    [HttpPut]
    public async Task<IActionResult> Put(int Id, [FromBody] Genius genius) {
        await _geniusRepository.Update(genius);
        return Ok();
    }
}

public class GeniusControllerTests {
    private GeniusController _geniusController;
    private Genius _genius;

    [SetUp]
    public void Setup() {
        _genius = new Genius {
            Id = 1,
            Name = "Genius 1",
            Description = "Genius 1 description"
        };

        _repository = new GeniusRepository();
        _geniusController = new GeniusController();
    }

    [Test]
    public async Task Put_Should_Update_Genius() {
        // Add Genius to repository
        await _repository.Add(_genius);

        // Updated genius
        var updatedGenius = new Genius {
            Id = 1,
            Name = "Genius 1 updated",
            Description = "Genius 1 description updated"
        };

        await _geniusController.Put(updatedGenius);

        var genius = await _repository.Get(_genius.Id);
        Assert.AreEqual(updatedGenius.Name, genius.Name);
    }

    [Test]
    public async Task Put_Should_Return_Ok() {
        // Add Genius to repository
        await _repository.Add(_genius);

        // Updated genius
        var updatedGenius = new Genius {
            Id = 1,
            Name = "Genius 1 updated",
            Description = "Genius 1 description updated"
        };

        var result = await _geniusController.Put(updatedGenius);

        Assert.IsInstanceOf<OkResult>(result);
    }
}