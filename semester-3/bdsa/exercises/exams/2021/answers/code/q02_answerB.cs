public enum Label
{
    Fall,
    Spring,
}

public class Semester
{
    [Key]
    public int Id { get; set; }
    
    [Required]
    public int Year { get; set; }

    [Required]
    public Label Label { get; set; }
}

public class Course
{
    [Key]
    public int Id { get; set; }

    [Required]
    public string Title { get; set; }

    public Semester? Semester { get; set; }

    public List<Teacher> Teachers { get; set; }
}

public class Teacher
{
    [Key]
    public string Name { get; set; }

    [Required]
    public string Title { get; set; }

    [EmailAddress]
    public string? Email { get; set; }

    public List<Course> Courses { get; set; }
}

public class TheClassContext : DbContext
{
    public DbSet<Semester> Semesters { get; set; }
    public DbSet<Course> Courses { get; set; }
    public DbSet<Teacher> Teachers { get; set; }

    public TheClassContext(DbContextOptions<TheClassContext> options) : base(options) { }

    protected override void OnModelCreating(ModelBuilder modelBuilder) { 
        modelBuilder.Entity<Semester>()
            .Property(s => s.Label)
            .HasConversion(
                v => v.ToString(),
                v => (Label)Enum.Parse(typeof(Label), v));
    }
}