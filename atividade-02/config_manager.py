class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._config = {}
        return cls._instance

    def set(self, key, value):
        self._config[key] = value

    def get(self, key):
        return self._config.get(key, None)

# Testando o Singleton
if __name__ == "__main__":
    manager1 = ConfigManager()
    manager1.set("api_key", "123456")

    manager2 = ConfigManager()
    print(manager2.get("api_key"))  # Deve imprimir: 123456

    print(manager1 is manager2)  # Deve imprimir: True
