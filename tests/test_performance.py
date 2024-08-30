from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_tasks(self):
        self.client.get("/tasks")

# To run this test with 10 concurrent users over a 30-second period, use the following command:
# locust -f test_performance.py --users 10 --spawn-rate 10 --run-time 30s --headless