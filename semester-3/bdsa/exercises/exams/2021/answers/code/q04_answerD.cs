[Authorize]
[ApiController]
public class AntagonistsController
{
    protected IAntagonistRepository _repository;

    public AntagonistsController(IAntagonistRepository repository)
    {
        _repository = repository;
    }

    [HttpPut("{id}")]
    public Task<ActionResult<bool>> UpdateAntagonist(int id, Antagonist antagonist)
    {
        var status = await _repository.UpdateAntagonist(id, antagonist);

        return Ok(status);
    }
}