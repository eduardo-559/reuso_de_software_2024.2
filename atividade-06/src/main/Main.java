package main;

import repository.InMemoryRepository;
import repository.InFileRepository;
import entities.Produto;
import entities.Cliente;

public class Main {
    public static void main(String[] args) {
        // Teste com Produto em Memória
        InMemoryRepository<Produto> produtoRepo = new InMemoryRepository<>();
        produtoRepo.save(new Produto("Laptop", 3000.0));
        produtoRepo.save(new Produto("Mouse", 50.0));

        System.out.println("Produtos em Memória:");
        produtoRepo.findAll().forEach(System.out::println);

        // Teste com Cliente usando Arquivo
        InFileRepository<Cliente> clienteRepo = new InFileRepository<>("clientes.json");
        clienteRepo.save(new Cliente("João Silva", "joao@email.com"));
        clienteRepo.save(new Cliente("Maria Oliveira", "maria@email.com"));

        System.out.println("Clientes no Arquivo:");
        clienteRepo.findAll().forEach(System.out::println);
    }
}
