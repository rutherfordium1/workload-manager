from locust import HttpUser, task, constant
import random

class QuickstartUser(HttpUser):
	wait_time = constant(0)
    host = "http://example.com"

   	@task(5)
    def test_get_method(self):
        self.client.get("/articles/?article_id=1")

   	@task
    def test_post_method(self):
        self.client.post("/articles/", {
			"title" : "A Title",
			"content" : "content!",
			"author_name" : "Mario",
        })

	@task
	def test_put_method(self):
		self.client.put("/articles/", {
			"id" : "3",
			"title" : "Title is Updated!",
			"content" : f"Your lucky number: {random.randint(0,9)}!",
			"author_name" : "Mario 2",
		})

    def on_start(self):
        self.client.post("/login", {"username":"foo", "password":"bar"})
