using static Label;

class Program
{
    static async Task Main(string[] args)
    {
        var options = new DbContextOptions<TheClassContext>();
        var context = new TheClassContext(options);

        var semester = new Semester
        {

            Year = 2021,
            Label = Fall
        };

        var teachers = new List<Teacher>
        {
            new Teacher
            {
                Name = "Rasmus Lystrom", // utf-8 doesn't seem to work in the latex template
                Title = "Professor",
            },
            new Teacher
            {
                Name = "Paolo Tell",
                Title = "Professor",
            }
        };

        var course = new Course
        {
            Title = "BDSA",
            Semester = semester,
            Teachers = teachers
        };

        foreach (var teacher in teachers)
        {
            teacher.Courses = new List<Course> { course };
        }

        // Untested, might cause an error saying that it cannot track multiple teacher entities
        context.Semesters.Add(semester);
        context.Teachers.AddRange(teachers);
        context.Courses.Add(course);

        await context.SaveChangesAsync();
    }
}