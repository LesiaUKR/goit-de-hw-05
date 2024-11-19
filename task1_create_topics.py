from kafka.admin import KafkaAdminClient, NewTopic
from configs import kafka_config
from colorama import Fore, Style, init

# Ініціалізація colorama для коректного відображення кольорів
init(autoreset=True)

# Створення клієнта Kafka
admin_client = KafkaAdminClient(
    bootstrap_servers=kafka_config['bootstrap_servers'],
    security_protocol=kafka_config['security_protocol'],
    sasl_mechanism=kafka_config['sasl_mechanism'],
    sasl_plain_username=kafka_config['username'],
    sasl_plain_password=kafka_config['password']
)

# Ім'я користувача для унікальних топіків
my_name = "lesiaukr"

# Визначення трьох топіків
topics = [
    NewTopic(name=f'{my_name}_building_sensors', num_partitions=1, replication_factor=1),
    NewTopic(name=f'{my_name}_temperature_alerts', num_partitions=1, replication_factor=1),
    NewTopic(name=f'{my_name}_humidity_alerts', num_partitions=1, replication_factor=1)
]

# Отримуємо список існуючих топіків
existing_topics = admin_client.list_topics()

# Фільтруємо ті топіки, які ще не створені
topics_to_create = [
    topic for topic in topics if topic.name not in existing_topics
]

# Створюємо нові топіки, якщо є що створювати
if topics_to_create:
    try:
        admin_client.create_topics(new_topics=topics_to_create, validate_only=False)
        print(Fore.GREEN + "Topics created successfully:")
        for topic in topics_to_create:
            print(Fore.YELLOW + f"  - {topic.name}")
    except Exception as e:
        print(Fore.RED + f"An error occurred during topic creation: {e}")
else:
    print(Fore.CYAN + "All topics already exist.")

# Виведення всіх наявних топіків
print(Fore.MAGENTA + "\n==== Available topics on the broker ====")
for topic in existing_topics:
    if topic in [t.name for t in topics]:  # Перевірка, чи це щойно створений топік
        print(Fore.GREEN + f"✅ {topic} (newly created)")
    else:
        print(Fore.WHITE + f"ℹ️  {topic}")

# Закриття зв'язку з клієнтом
admin_client.close()


