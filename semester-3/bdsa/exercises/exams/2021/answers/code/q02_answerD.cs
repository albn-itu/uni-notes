using static Label;

class Program
{
    static async Task Main(string[] args)
    {
        var options = new DbContextOptions<TheClassContext>();
        var context = new TheClassContext(options);

        // Retrieve courses teached by Tell projecting anon type Title and Year
        var courses = await context.Courses
            .Where(c => c.Teachers.Any(t => t.Name == "Tell"))
            .Select(c => new { c.Title, c.Semester.Year })
            .ToListAsync();

        // Retrieve courses teached by Tell projecting anon type Title and Year using linq
        var courses = await (from c in context.Courses
                              where c.Teachers.Any(t => t.Name == "Tell")
                              select new { c.Title, c.Semester.Year })
                              .ToListAsync();
    }
}