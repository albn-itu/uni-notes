public class Album {}

public interface IAlbumPersistanceBase
{
    Album? Get(int id);
}

// 2 Interfaces are better than one and then having to implement a method as unsupported
public interface IAlbumPersistanceSettable : IAlbumPersistanceBase {
    void Set(int id, Album album);
}

// Since we have 2 interfaces now and the AlbumService acts exactly like the IAlbumPersistanceBase, we might as well implement the interface
// Alternatively we could create a seperate interface
public class AlbumService : IAlbumPersistanceBase
{
    protected IAlbumPersistanceSettable _cache;

    protected IAlbumPersistanceBase _repository;

    public AlbumService(IAlbumPersistanceSettable cache, IAlbumPersistanceBase repository)
    {
        _cache = cache;
        _repository = repository;
    }

    public Album? Get(int id)
    {
        var album = _cache.Get(id);

        if (album == null)
        {
            album = _repository.Get(id);

            if (album != null)
            {
                _cache.Set(id, album);
            }
        }

        return album;
    }
}


public class AlbumCache : IAlbumPersistanceSettable
{
    public Album? Get(int id) => ...;
    public void Set(int id, Album album) => ...;
}

public class AlbumRepository : IAlbumPersistanceBase
{
    public Album? Get(int id) { ... }
}