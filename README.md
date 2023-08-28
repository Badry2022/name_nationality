

```markdown

### Nationalize App

The Nationalize App is a simple Flask web application that predicts the nationality and probability of a given name using the [Nationalize.io API](https://api.nationalize.io/).

### Getting Started

These instructions will guide you through setting up and running the Nationalize App locally on your machine.

### Prerequisites

- Python 3.x
- [Poetry](https://python-poetry.org/)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd nationalize_app
   ```

2. Create a virtual environment (venv) and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # Or, on Windows: venv\Scripts\activate
   ```

3. Install Poetry for managing project dependencies:

   ```bash
   pip install poetry
   ```

4. Install project dependencies using Poetry:

   ```bash
   poetry install
   ```

### Usage

1. Run the Flask application:

   ```bash
   poetry run python app.py
   ```

   The app should now be running locally at `http://localhost:5000`.

2. Open a web browser and navigate to `http://localhost:5000`.

3. Enter a name in the input field and click the "Submit" button to get the predicted nationality and probability.

### Running Tests

You can run unit tests for the Nationalize App using pytest. Make sure you have activated the virtual environment.

```bash
poetry run pytest tests/
```

### Continuous Integration (CI)

This project includes a basic GitHub Actions workflow for continuous integration. It runs the tests whenever changes are pushed to the `main` branch.

### Directory Structure

- `app.py`: The Flask application.
- `templates/`: HTML templates.
- `tests/`: Unit tests.
- `pyproject.toml`: Poetry configuration.
- `README.md`: Project documentation.

## Built With

- [Flask](https://flask.palletsprojects.com/): A micro web framework for Python.
- [Poetry](https://python-poetry.org/): Dependency management and packaging tool.
- [requests](https://pypi.org/project/requests/): A library for making HTTP requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace `<repository_url>` with the actual URL of your Git repository.

This `README.md` provides detailed instructions on setting up and running the Nationalize App, including prerequisites, installation steps, usage instructions, testing, and CI integration.
