
# HW | Apache Kafka
Ready to tackle the homework? Then let’s dive in! 🎢

Today, you’ll focus on the practical application of Apache Kafka using the Python API, honing your skills in creating topics, writing data to a topic, and reading it.

Scenario:
Imagine you work for a company developing monitoring systems for the Internet of Things (IoT). The primary goal of the system is to collect data from various sensors installed in several buildings and analyze it in real time to track parameters such as temperature and humidity.

To achieve this, Apache Kafka is used as a messaging platform that efficiently transmits and processes large volumes of data.

Your task is to implement several components of this system using Python and Apache Kafka according to the provided instructions.

Let this assignment broaden your perspective on the world of streaming data! 🧠

Step-by-Step Instructions
1. Creating Topics in Kafka:
Create three topics in Kafka:
Add your name or another identifier to topic names to ensure they are unique.
building_sensors — stores data from all sensors.
temperature_alerts — stores alerts for temperature exceeding permissible levels.
humidity_alerts — stores alerts for humidity levels outside acceptable ranges.
2. Sending Data to Topics:
Write a Python script that simulates a sensor's work and periodically sends randomly generated data (temperature and humidity) to the building_sensors topic.
The data should include:
Sensor ID
Timestamp of data collection
Corresponding readings
Note:
Each script execution should simulate only one sensor. To simulate multiple sensors, the script must be run multiple times.
The sensor ID can be a random constant for a single script run and may change with each new execution.
Temperature values: random between 25 and 45°C.
Humidity values: random between 15% and 85%.
3. Data Processing:
Write a Python script that subscribes to the building_sensors topic, reads messages, and processes the data:
If the temperature exceeds 40°C, generate an alert and send it to the temperature_alerts topic.
If humidity exceeds 80% or drops below 20%, generate an alert and send it to the humidity_alerts topic.
Alerts should include:
Sensor ID
Measurement values
Timestamp
Alert message indicating threshold exceeded.
4. Displaying Final Data:
Write a Python script that subscribes to the temperature_alerts and humidity_alerts topics, reads alerts, and displays the messages on the screen.
Submission and Evaluation Criteria
☝🏻 Mandatory acceptance criteria must be met for mentors to evaluate the homework. If any criteria are not met, the homework will be returned for revision. For clarifications or if stuck, contact your mentor on Slack.

Grading:
Creating 3 topics: 10 points.
Generating sensor data and sending it to building_sensors: 20 points.
Receiving and filtering data from building_sensors: 25 points.
Sending filtered data to temperature_alerts and humidity_alerts: 30 points.
This task builds on previous assignments.
Receiving data from temperature_alerts and humidity_alerts and displaying it: 15 points.
Maximum total points: 100.

Mistakes or shortcomings in execution will reduce the score proportionally, as determined by the mentor.

Important Notes:
💡 You have two approaches for submission and potential revisions:

Accept the first score if it meets or exceeds the passing threshold.
Aim for a higher score through potential revisions based on mentor feedback.
Indicate your chosen approach in the task submission field. If no comment is provided, the mentor will assume the first approach and grade accordingly.

💡 Submit the homework only when fully completed, as the number of submission attempts affects your score. Starting with the third attempt, the maximum possible score is reduced by 5 points per subsequent attempt.

Preparation and Submission Steps
Repository Creation:

Create a public repository named goit-de-hw-05.
Implementation:

Complete the tasks and upload:
Code
Screenshots for each stage in a text document with a brief description.
Required Screenshots:

Three topics shown using [print(topic) for topic in admin_client.list_topics() if "my_name" in topic].
Sensor data generation and simultaneous execution of at least two script instances.
Data processing showing relevant filtered data.
Sending filtered data to respective topics.
Processed and filtered data output.
Archiving:

Create a single archive containing all the code and a text document with screenshots.
Name the archive in the format HW5_LastName.
Submission:

Attach the archive and provide a link to the repository in the submission field of the LMS.
Submission Format
Link to the goit-de-hw-05 repository.
Attached archive named HW5_LastName.





