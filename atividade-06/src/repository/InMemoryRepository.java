package repository;

import java.util.*;

public class InMemoryRepository<T> implements CrudRepository<T> {
    private final Map<Integer, T> storage = new HashMap<>();
    private int currentId = 1;

    @Override
    public void save(T entity) {
        storage.put(currentId++, entity);
    }

    @Override
    public T findById(int id) {
        return storage.get(id);
    }

    @Override
    public void update(T entity) {
        // Implementação depende da estrutura do objeto
    }

    @Override
    public void delete(int id) {
        storage.remove(id);
    }

    @Override
    public List<T> findAll() {
        return new ArrayList<>(storage.values());
    }
}
