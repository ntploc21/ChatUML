# ChatUML

A website that can help you with creating simple UML diagrams for your next project with just one simple message.

This is an MVP Submission to the CinnamonAI Full Stack AI Bootcamp. The purpose of this project is to evaluate the candidates' modelling and engineering skills before the bootcamp.

## Features
Create UML diagrams with just one simple message

## Releases
The application is now [live on the web](https://ntploc21-chatuml.streamlit.app/).

For more information, you can check the web-deploy branch of the repository.

## Demo
(Will be updated soon)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Documentation
### User Manual
(Will be updated soon)

## Technical Overview
This project is built with the following technologies:
### Technologies
- [Python 3.8](https://www.python.org/downloads/release/python-380/) as the main programming language.
- [Streamlit](https://streamlit.io/) for the web application.
- [OpenAI GPT-3](https://openai.com/blog/openai-api/) for the generating the PlantUML code.
- [PlantUML](https://plantuml.com/) for the UML diagram generation from the PlantUML code.
- [Docker](https://www.docker.com/) for the containerization.
- [Sphinx](https://www.sphinx-doc.org/) for the documentation.

### Code Style
This project follows the [PEP 8](https://www.python.org/dev/peps/pep-0008/) code style. The code is also linted with [Flake8](https://flake8.pycqa.org/en/latest/).

### Development
This project used pre-commit hooks to lint the code before committing. The pre-commit hooks are configured in the `.pre-commit-config.yaml` file. The pre-commit hooks are managed by [pre-commit](https://pre-commit.com/).

And I also implemented a CI/CD pipeline for this project. The CI/CD pipeline is managed by [GitHub Actions](https://github.com/ntploc21/ChatUML/blob/main/.github/workflows/build.yml).

## Building
### Manual
1. Clone this repository to your machine.
    ```bash
        git clone https://github.com/ntploc21/ChatUML.git
        cd ChatUML
    ```
2. Run the following command to install the dependencies.
    ```bash
        pip install -r requirements.txt
    ```
3. Finally, run the following command to start the application.
    ```bash
        streamlit run chat-uml/app.py
    ```
4. The application should be running on your machine now. You can access it by going to `http://localhost:8501` on your browser.

### Docker
Make sure you have installed [Docker](https://www.docker.com/) and have your Docker running.
1. Clone this repository to your machine.
    ```bash
        git clone https://github.com/ntploc21/ChatUML.git
        cd ChatUML
    ```
2. Run the following command to build the Docker image.
    ```bash
        docker build -t chat-uml .
    ```
3. Finally, run the following command to start the application.
    ```bash
        docker run -p 8501:8501 chat-uml
    ```
4. The application should be running on your machine now. You can access it by going to `http://localhost:8501` on your browser.

## Project Structure
- `chat-uml/`: The main application folder.
    - `app.py`: The main application file, which contains the Streamlit application.
    - `complete_prompt.py`: The file that help with generating the complete prompt for the GPT-3 API.
    - `uml_generate.py`: The file that help with generating the UML diagram from the GPT-3 API response.
- `prompts/`: The folder that contains the prompt templates for the GPT-3 API.
- `.streamlit/`: The folder that contains the configuration file for the Streamlit application.
- `.flake8`: The configuration file for the Flake8 linter.
- `Dockefile`: The Dockerfile for the application.