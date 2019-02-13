FROM python:3.6
RUN apt-get update && apt-get -y install libyajl-dev
ENV PIPENV_VENV_IN_PROJECT=1
RUN pip install pipenv
WORKDIR /chinman
ADD Pipfile Pipfile.lock /chinman/
RUN pipenv install
ADD . /chinman/
ENTRYPOINT ["pipenv", "run", "python", "-m", "chinman"]
