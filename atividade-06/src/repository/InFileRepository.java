package repository;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.io.*;
import java.lang.reflect.Type;
import java.util.*;

public class InFileRepository<T> implements CrudRepository<T> {
    private final String filePath;
    private final Gson gson = new Gson();
    private final Type listType = new TypeToken<List<T>>() {}.getType();

    public InFileRepository(String filePath) {
        this.filePath = filePath;
    }

    @Override
    public void save(T entity) {
        List<T> entities = findAll();
        entities.add(entity);
        try (Writer writer = new FileWriter(filePath)) {
            gson.toJson(entities, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public List<T> findAll() {
        try (Reader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, listType);
        } catch (IOException e) {
            return new ArrayList<>();
        }
    }

    @Override
    public T findById(int id) {
        List<T> entities = findAll();
        if (id >= 0 && id < entities.size()) {
            return entities.get(id);
        }
        return null;
    }

    @Override
    public void update(T entity) {}

    @Override
    public void delete(int id) {
        List<T> entities = findAll();
        if (id >= 0 && id < entities.size()) {
            entities.remove(id);
            try (Writer writer = new FileWriter(filePath)) {
                gson.toJson(entities, writer);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
