#Definition of the job class, with a method to print itself.

class Job:
    def __init__(self, company_name, job_title, send_date, response_date, response):
        self.company_name = company_name
        self.job_title = job_title
        self.send_date = send_date
        self.response_date = response_date
        self.response = response
    
    def print(self):
        print("Company name: " + self.company_name)
        print("Job Title: " + self.job_title)
        print("Date of Application: " + self.send_date)
        print("Date of Response: " + self.response_date)
        print("Response: " + self.response)
