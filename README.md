# KakeboAPP

**KakeboAPP** is a personal finance management application based on the traditional Japanese method of Kakeibo. The app allows users to track and analyze their income and expenses, set savings goals, and categorize their finances to gain a clear view of their financial situation.

## Key Features

- **Income and Expense Tracking**: Users can log their financial transactions, categorizing them accordingly.
- **Financial Goal Analysis**: Users can set spending and savings goals, and the app provides visual analysis of their progress.
- **Interactive Dashboard**: A user-friendly dashboard that summarizes key financial metrics, helping users to stay on top of their finances.
- **Monthly Reports**: Generate detailed reports on monthly spending vs. income to identify trends and make informed financial decisions.

KakeboAPP is designed to help users achieve better financial awareness and discipline, ultimately leading to smarter financial decisions and increased savings.

## Installation

To get started with KakeboAPP, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/kakeboapp.git

2. **Navigate to the project directory:**

cd kakeboapp

3. **Set up a virtual environment:**

python3 -m venv myenv
source myenv/bin/activate  #On Windows use `myenv\Scripts\activate`

4. **Install the required dependencies:**

pip install -r requirements.txt

5. **Set up the database:**

	•	Make sure PostgreSQL is installed and running.
	•	Update the database configuration in settings.py as needed.
	•	Run migrations:

    python manage.py migrate

6. **Create a superuser:**

python manage.py createsuperuser

7. **Run the development server:**

python manage.py runserver

## Usage

Once the server is running, you can access the application in your web browser at http://127.0.0.1:8000/.

	•	Admin Panel: To access the Django admin panel, go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials.
	•	Dashboard: Access the main dashboard to manage your income, expenses, and goals.

## Contributing

We welcome contributions to KakeboAPP! If you want to contribute, please follow these steps:

1. **Fork the repository**

2. **Create a new branch for your feature or bugfix:**

git checkout -b feature-name

3.	**Make your changes and commit them:**

git commit -m "Add feature description"

4.	**Push your changes to your forked repository:**

git push origin feature-name

5.	**Open a Pull Request on the original repository.**

## License

KakeboAPP is licensed under the MIT License.

## Contact

- **Email**: info@quintero.cz
