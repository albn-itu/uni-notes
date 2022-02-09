public class Gadget
{
    public string Name { get; init; }
    public string Film { get; init; }

    public Gadget(string name, string film)
    {
        if (name == null)
            throw new ArgumentNullException(nameof(name));

        if (film == null)
            throw new ArgumentNullException(nameof(film));

        Name = name;
        Film = film;
    } 
}